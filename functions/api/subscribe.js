// Blog email subscription (card blog-email-subscription). Max 2026-11-13:
// "we should have an email subscription for people who sign up for it".
//
//   POST /api/subscribe                   form post: email=...&p=/blog/   -> 200, always the same words
//   GET  /api/subscribe?confirm=<token>   the link in the confirmation email
//   GET  /api/subscribe?unsubscribe=<token>  the link in the footer of every email
//
// Double opt-in: a signup is `pending` and gets exactly one email, the confirmation. Only a
// confirmed row is ever sent a post. The homelab CronJob picks pending rows up through the D1
// API and the mailer sends them as the Max Draco persona, so this Function never sends mail and
// holds no mail credential.
//
// CAN-SPAM (FTC guide, read 2026-11-13; registry entry fed-can-spam): the opt-out link has to
// keep working for at least 30 days after a message is sent, so a row is never deleted here and
// a second click on the same link still answers. Acting on it is immediate.
//
// Anyone can post to this, so: the Origin must be ours, the address is validated and clipped,
// a per-minute cap stops a flood, and the answer never differs between a new address and one
// already on the list (otherwise the form is an address-checker for strangers).
//
// Stored: the address, the page the form was on, and timestamps. No IP, no user agent, no name.

export const HOSTS = new Set(['maxdraco.com', 'www.maxdraco.com'])
const PER_MINUTE = 60
const MAX_EMAIL = 254          // RFC 5321 maximum
const MAX_PATH = 128

// Deliberately simple and strict: one @, no spaces, a dot in the domain. A real address that
// this refuses can still write to the contact address; a wrong one that it accepts bounces
// silently and sits in the table forever.
const EMAIL = /^[^\s@,;:<>()[\]\\"]{1,64}@[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+$/

export function cleanEmail (raw) {
  if (typeof raw !== 'string') return null
  const v = raw.trim().toLowerCase()
  if (!v || v.length > MAX_EMAIL) return null
  return EMAIL.test(v) ? v : null
}

export function cleanPath (raw) {
  if (typeof raw !== 'string') return null
  const v = raw.split('?')[0].split('#')[0]
  if (!v.startsWith('/')) return null          // only our own paths, never a full URL
  return v.slice(0, MAX_PATH)
}

export function newToken () {
  const b = new Uint8Array(24)
  crypto.getRandomValues(b)
  return btoa(String.fromCharCode(...b)).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
}

// One sentence, whatever happened, so the form cannot be used to test addresses.
export function answer () {
  return 'Thanks. If that address can receive mail, a confirmation is on its way. ' +
         'The list only starts once you click the link in it.'
}

function page (title, body, status = 200) {
  return new Response(
    `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">` +
    `<meta name="robots" content="noindex"><title>${title} | Max Draco</title>` +
    `<body style="font:16px/1.5 system-ui,sans-serif;max-width:34rem;margin:4rem auto;padding:0 1rem">` +
    `<h1 style="font-size:1.3rem">${title}</h1><p>${body}</p><p><a href="/blog/">Back to the blog</a></p>`,
    { status, headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' } })
}

function notFound () {
  return page('That link has expired', 'We could not match that link. If you were trying to unsubscribe, ' +
    'reply to any of the emails and it will be done by hand.', 404)
}

async function overCap (db, now) {
  const minute = Math.floor(now / 60)
  const row = await db.prepare('SELECT n FROM signup_rate WHERE minute = ?').bind(minute).first()
  if (row && row.n >= PER_MINUTE) return true
  await db.prepare(
    'INSERT INTO signup_rate (minute, n) VALUES (?, 1) ON CONFLICT(minute) DO UPDATE SET n = n + 1'
  ).bind(minute).run()
  return false
}

export async function onRequestPost ({ request, env }) {
  const origin = request.headers.get('origin') || ''
  let host = ''
  try { host = new URL(origin).hostname } catch { host = '' }
  if (!HOSTS.has(host)) return new Response('no', { status: 403 })

  const db = env.SUBS
  const now = Math.floor(Date.now() / 1000)
  if (await overCap(db, now)) return new Response('slow down', { status: 429 })

  const form = await request.formData()
  const email = cleanEmail(form.get('email'))
  const path = cleanPath(form.get('p'))

  // Same answer either way, so only do the work when the address is usable and new.
  if (email) {
    const seen = await db.prepare('SELECT status FROM subscribers WHERE email = ?').bind(email).first()
    if (!seen) {
      await db.prepare(
        'INSERT INTO subscribers (email, token, created_at, source_path) VALUES (?, ?, ?, ?)'
      ).bind(email, newToken(), now, path).run()
    }
    // Already pending, confirmed or unsubscribed: leave the row exactly as it is. Someone who
    // unsubscribed does not get quietly put back on by a form post.
  }
  return new Response(answer(), { status: 200, headers: { 'content-type': 'text/plain; charset=utf-8' } })
}

export async function onRequestGet ({ request, env }) {
  const url = new URL(request.url)
  const confirm = url.searchParams.get('confirm')
  const unsub = url.searchParams.get('unsubscribe')
  const token = confirm || unsub
  if (!token) return notFound()

  const db = env.SUBS
  const now = Math.floor(Date.now() / 1000)
  const row = await db.prepare('SELECT email, status FROM subscribers WHERE token = ?').bind(token).first()
  if (!row) return notFound()

  if (unsub) {
    if (row.status !== 'unsubscribed') {
      await db.prepare("UPDATE subscribers SET status = 'unsubscribed', unsubscribed_at = ? WHERE token = ?")
        .bind(now, token).run()
    }
    // A second click is not an error: the link has to keep working.
    return page('You are unsubscribed', 'You will not be emailed again. Nothing else was deleted, ' +
      'because the record is what shows you asked to be on the list in the first place.')
  }

  if (row.status === 'pending') {
    await db.prepare("UPDATE subscribers SET status = 'confirmed', confirmed_at = ? WHERE token = ?")
      .bind(now, token).run()
  }
  if (row.status === 'unsubscribed') {
    return page('You had unsubscribed', 'That address asked to be taken off the list, so this link ' +
      'does not put it back. Use the form on the blog if you want to sign up again.')
  }
  return page('You are on the list', 'You will get an email when there is a new post, and every one ' +
    'of them has an unsubscribe link at the bottom.')
}
