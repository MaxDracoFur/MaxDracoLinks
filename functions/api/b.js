// First-party page beacon (static/js/beacon.js), card site-beacon-first-party.
//
// POST /api/b   text/plain JSON from navigator.sendBeacon on maxdraco.com, cds. or hack.
//               -> 204, always (the browser ignores the answer; errors are not a signal
//               worth giving a stranger).
//
// Stored per row: when, kind (view / out / err), host, path, referrer host + path (no
// query string), ?ref= / utm_* tags, Cloudflare's country code, mobile|desktop, and for
// views the engaged seconds and scroll depth. NOT stored: IP address, user agent, any
// identifier. The homelab CronJob homelab/site-beacon pulls rows out through the D1 API
// and deletes them after 35 days.
//
// Anyone can POST here, so every field is treated as hostile: host must be one of ours
// and match the Origin header, strings are cut short, and a global per-minute cap keeps
// a flood from filling the database.

export const HOSTS = new Set(['maxdraco.com', 'www.maxdraco.com', 'cds.maxdraco.com', 'hack.maxdraco.com'])
const PER_MINUTE = 300
const MAX_BODY = 8192
const MAX_EVENTS = 20

function clip (v, n) {
  if (typeof v !== 'string') return null
  // Control characters would break the one-line log format downstream.
  const s = v.replace(/[\u0000-\u001f\u007f]/g, ' ').trim()
  return s ? s.slice(0, n) : null
}

function int (v, lo, hi) {
  const n = Math.round(Number(v))
  if (!Number.isFinite(n)) return null
  return Math.min(hi, Math.max(lo, n))
}

function cleanPath (p) {
  const s = clip(p, 300)
  if (!s || s[0] !== '/') return null
  return s.split('?')[0].split('#')[0]
}

// "https://www.google.com/search?q=x" -> ["www.google.com", "/search"]
export function splitReferrer (r) {
  const s = clip(r, 500)
  if (!s) return [null, null]
  try {
    const u = new URL(s)
    if (u.protocol !== 'http:' && u.protocol !== 'https:') return [null, null]
    return [u.hostname.toLowerCase().slice(0, 120), u.pathname.slice(0, 200)]
  } catch (e) {
    return [null, null]
  }
}

export function deviceClass (ua) {
  if (!ua) return null
  return /Mobi|Android|iPhone|iPad|iPod/i.test(ua) ? 'mobile' : 'desktop'
}

// Body + request facts -> rows for the events table, or [] for anything that isn't ours.
export function toRows (body, { origin, country, ua, now }) {
  if (!body || typeof body !== 'object' || body.v !== 1) return []
  const host = clip(body.h, 64)
  if (!host || !HOSTS.has(host)) return []
  if (origin !== 'https://' + host) return []
  const path = cleanPath(body.p)
  if (!path) return []

  const [refHost, refPath] = splitReferrer(body.r)
  const tags = body.t && typeof body.t === 'object' ? body.t : {}
  const base = {
    at: now,
    host,
    path,
    ref_host: refHost,
    ref_path: refPath,
    tag_ref: clip(tags.ref, 64),
    utm_source: clip(tags.utm_source, 64),
    utm_medium: clip(tags.utm_medium, 64),
    utm_campaign: clip(tags.utm_campaign, 64),
    country: clip(country, 2),
    device: deviceClass(ua)
  }

  const cont = int(body.c, 0, 1000) || 0
  const rows = [{
    ...base,
    kind: body.nf ? 'notfound' : 'view',
    cont,
    engaged_ms: int(body.ms, 0, 6 * 3600 * 1000),
    scroll_pct: int(body.sc, 0, 100),
    target: null,
    detail: null
  }]

  const events = Array.isArray(body.e) ? body.e.slice(0, MAX_EVENTS) : []
  for (const ev of events) {
    if (!ev || typeof ev !== 'object') continue
    if (ev.k === 'out') {
      const target = clip(ev.u, 200)
      if (target) rows.push({ ...base, kind: 'out', cont, engaged_ms: null, scroll_pct: null, target, detail: null })
    } else if (ev.k === 'err') {
      const msg = clip(ev.m, 200)
      if (!msg) continue
      const file = clip(ev.f, 120) || ''
      const line = int(ev.l, 0, 1e7) || 0
      rows.push({ ...base, kind: 'err', cont, engaged_ms: null, scroll_pct: null, target: (file + ':' + line).slice(0, 200), detail: msg })
    }
  }
  return rows
}

const COLS = ['at', 'kind', 'cont', 'host', 'path', 'ref_host', 'ref_path', 'tag_ref', 'utm_source', 'utm_medium',
  'utm_campaign', 'country', 'device', 'engaged_ms', 'scroll_pct', 'target', 'detail']
const INSERT = 'INSERT INTO events (' + COLS.join(', ') + ') VALUES (' + COLS.map(() => '?').join(', ') + ')'

function done () {
  return new Response(null, { status: 204, headers: { 'cache-control': 'no-store' } })
}

export async function onRequestPost ({ request, env }) {
  const text = await request.text()
  if (text.length > MAX_BODY) return done()
  let body
  try { body = JSON.parse(text) } catch (e) { return done() }

  const now = Math.floor(Date.now() / 1000)
  const rows = toRows(body, {
    origin: request.headers.get('origin'),
    country: request.cf && request.cf.country,
    ua: request.headers.get('user-agent'),
    now
  })
  if (!rows.length) return done()

  const db = env.BEACON
  const recent = await db.prepare('SELECT COUNT(*) AS n FROM events WHERE at > ?').bind(now - 60).first()
  if (recent && recent.n >= PER_MINUTE) {
    await db.prepare('UPDATE dropped SET n = n + ? WHERE id = 1').bind(rows.length).run()
    return done()
  }
  await db.batch(rows.map(r => db.prepare(INSERT).bind(...COLS.map(c => r[c] ?? null))))
  return done()
}

// Anything else (GET, preflight) gets the same empty answer.
export async function onRequest () {
  return done()
}
