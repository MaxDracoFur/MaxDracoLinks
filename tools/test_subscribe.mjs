// node --test tools/test_subscribe.mjs   (card blog-email-subscription)
//
// Written from the requirements before the Function existed:
// - Double opt-in: a signup is `pending` and is never mailed anything but one confirmation.
// - CAN-SPAM (FTC guide, read 2026-11-13): the opt-out link keeps working, and acting on it is
//   immediate. The registry entry is fed-can-spam.
// - The form is public, so every field is hostile: addresses are validated and clipped, and a
//   per-minute cap stops a flood.
// - Nobody can use the form to find out whether an address is already on the list: the answer
//   is the same either way.
// - Only the address, the page it came from and the timestamps are stored. No IP, no user agent.
import { test } from 'node:test'
import assert from 'node:assert/strict'
import { cleanEmail, cleanPath, newToken, answer, onRequestPost, onRequestGet } from '../functions/api/subscribe.js'

// A fake D1: enough of .prepare().bind().first()/run() for the Function under test.
function fakeDB (rows = []) {
  const db = { rows, calls: [] }
  db.prepare = (sql) => ({
    bind: (...args) => ({
      first: async () => {
        db.calls.push({ sql, args })
        if (/FROM subscribers WHERE email/.test(sql)) return db.rows.find(r => r.email === args[0]) || null
        if (/FROM subscribers WHERE token/.test(sql)) return db.rows.find(r => r.token === args[0]) || null
        if (/FROM signup_rate/.test(sql)) return { n: db.minuteCount ?? 0 }
        return null
      },
      run: async () => {
        db.calls.push({ sql, args })
        if (/INSERT INTO subscribers/.test(sql)) {
          db.rows.push({ email: args[0], token: args[1], created_at: args[2], source_path: args[3], status: 'pending' })
        }
        if (/UPDATE subscribers SET status = 'confirmed'/.test(sql)) {
          const r = db.rows.find(x => x.token === args[args.length - 1]); if (r) { r.status = 'confirmed'; r.confirmed_at = args[0] }
        }
        if (/UPDATE subscribers SET status = 'unsubscribed'/.test(sql)) {
          const r = db.rows.find(x => x.token === args[args.length - 1]); if (r) { r.status = 'unsubscribed'; r.unsubscribed_at = args[0] }
        }
        return { success: true }
      }
    })
  })
  return db
}

const post = (body, db, origin = 'https://maxdraco.com') => onRequestPost({
  request: new Request('https://maxdraco.com/api/subscribe', {
    method: 'POST',
    headers: { 'content-type': 'application/x-www-form-urlencoded', origin },
    body
  }),
  env: { SUBS: db }
})

const get = (qs, db) => onRequestGet({
  request: new Request('https://maxdraco.com/api/subscribe' + qs),
  env: { SUBS: db }
})

test('an address is trimmed and lower-cased before it is stored', () => {
  assert.equal(cleanEmail('  Max@Example.COM '), 'max@example.com')
})

test('rubbish addresses are refused', () => {
  for (const bad of ['', 'nope', 'a@', '@b.com', 'a b@c.com', 'a@b', 'a@b.c d', null, 'x'.repeat(250) + '@b.com']) {
    assert.equal(cleanEmail(bad), null, String(bad))
  }
})

test('a signup is stored as pending, with the page it came from and no identifying fields', async () => {
  const db = fakeDB()
  await post('email=Reader%40Example.com&p=/blog/', db)
  assert.equal(db.rows.length, 1)
  assert.equal(db.rows[0].email, 'reader@example.com')
  assert.equal(db.rows[0].status, 'pending')
  assert.equal(db.rows[0].source_path, '/blog/')
  const stored = JSON.stringify(db.calls)
  assert.ok(!/ip|user-?agent|cf-connecting/i.test(stored), 'nothing identifying is written')
})

test('the reply is the same whether or not the address is already on the list', async () => {
  const a = await post('email=new%40example.com', fakeDB())
  const b = await post('email=old%40example.com', fakeDB([{ email: 'old@example.com', token: 't1', status: 'confirmed' }]))
  assert.equal(a.status, b.status)
  assert.equal(await a.clone().text(), await b.clone().text())
})

test('an existing address is not given a second row or a new token', async () => {
  const db = fakeDB([{ email: 'old@example.com', token: 't1', status: 'confirmed' }])
  await post('email=old%40example.com', db)
  assert.equal(db.rows.length, 1)
  assert.equal(db.rows[0].token, 't1')
})

test('a flood is capped', async () => {
  const db = fakeDB(); db.minuteCount = 1000
  const r = await post('email=flood%40example.com', db)
  assert.equal(r.status, 429)
  assert.equal(db.rows.length, 0)
})

test('a post from another site is refused', async () => {
  const db = fakeDB()
  const r = await post('email=x%40example.com', db, 'https://evil.example')
  assert.equal(r.status, 403)
  assert.equal(db.rows.length, 0)
})

test('confirming marks the row confirmed and says so', async () => {
  const db = fakeDB([{ email: 'a@example.com', token: 'tok1', status: 'pending' }])
  const r = await get('?confirm=tok1', db)
  assert.equal(r.status, 200)
  assert.equal(db.rows[0].status, 'confirmed')
  assert.ok(typeof db.rows[0].confirmed_at === 'number')
})

test('unsubscribing works immediately, and works again afterwards', async () => {
  const db = fakeDB([{ email: 'a@example.com', token: 'tok1', status: 'confirmed' }])
  const first = await get('?unsubscribe=tok1', db)
  assert.equal(first.status, 200)
  assert.equal(db.rows[0].status, 'unsubscribed')
  const again = await get('?unsubscribe=tok1', db)
  assert.equal(again.status, 200, 'a second click still answers, it does not 404')
})

test('an unsubscribed address is never silently resurrected by the form', async () => {
  const db = fakeDB([{ email: 'gone@example.com', token: 'tok1', status: 'unsubscribed' }])
  await post('email=gone%40example.com', db)
  assert.equal(db.rows[0].status, 'unsubscribed')
})

test('an unknown or missing token is refused, and never says which addresses exist', async () => {
  const db = fakeDB([{ email: 'a@example.com', token: 'tok1', status: 'pending' }])
  for (const qs of ['?confirm=nope', '?unsubscribe=nope', '?confirm=', '']) {
    const r = await get(qs, db)
    assert.equal(r.status, 404, qs)
    assert.ok(!(await r.text()).includes('a@example.com'))
  }
})

test('tokens are long, URL-safe and not repeated', () => {
  const seen = new Set()
  for (let i = 0; i < 200; i++) {
    const t = newToken()
    assert.match(t, /^[A-Za-z0-9_-]{24,}$/)
    assert.ok(!seen.has(t)); seen.add(t)
  }
})

test('the source path is clipped and loses any query string', () => {
  assert.equal(cleanPath('/blog/?utm_source=x'), '/blog/')
  assert.equal(cleanPath('/' + 'a'.repeat(500)).length <= 128, true)
  assert.equal(cleanPath('https://evil.example/x'), null)
  assert.equal(cleanPath(null), null)
})

test('answer() never leaks whether an address is known', () => {
  assert.equal(answer(true), answer(false))
})
