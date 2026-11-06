// Global counter for the hidden gems (assets/js/gems.js).
//
// GET  /api/gems             -> {"total": n}
// POST /api/gems {"egg": id} -> {"total": n}   one find, counted once per browser
//
// Stores nothing about the visitor: each row is just which gem and when.
// The "once per browser" part is the browser's own localStorage, so a
// determined person can inflate the number; the per-minute cap below keeps
// that to a trickle instead of a flood.

const EGGS = new Set(['online', 'typed', 'lost'])
const PER_MINUTE = 30

function json (body, status = 200, cache = 'no-store') {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'content-type': 'application/json', 'cache-control': cache }
  })
}

async function total (db) {
  const row = await db.prepare('SELECT COUNT(*) AS n FROM finds').first()
  return row ? row.n : 0
}

export async function onRequestGet ({ env }) {
  return json({ total: await total(env.GEMS) }, 200, 'public, max-age=15')
}

export async function onRequestPost ({ request, env }) {
  // Only the site's own pages may count a find.
  const origin = request.headers.get('origin')
  if (origin !== new URL(request.url).origin) return json({ error: 'origin' }, 403)

  let egg
  try {
    egg = (await request.json()).egg
  } catch (e) {
    return json({ error: 'body' }, 400)
  }
  if (!EGGS.has(egg)) return json({ error: 'egg' }, 400)

  const db = env.GEMS
  const now = Math.floor(Date.now() / 1000)
  const recent = await db.prepare('SELECT COUNT(*) AS n FROM finds WHERE at > ?').bind(now - 60).first()
  if (recent && recent.n >= PER_MINUTE) {
    return json({ total: await total(db), limited: true }, 429)
  }
  await db.prepare('INSERT INTO finds (egg, at) VALUES (?, ?)').bind(egg, now).run()
  return json({ total: await total(db) })
}
