// node --test tools/test_beacon.mjs   (card site-beacon-first-party)
// Written from the requirements: only our hosts, Origin must match, no query strings kept,
// hostile input clipped, nothing identifying stored.
import { test } from 'node:test'
import assert from 'node:assert/strict'
import { toRows, splitReferrer, deviceClass } from '../functions/api/b.js'

const meta = { origin: 'https://maxdraco.com', country: 'US', ua: 'Mozilla/5.0 (iPhone) Mobile', now: 1000 }
const view = (over = {}) => ({ v: 1, c: 0, h: 'maxdraco.com', p: '/blog/', r: '', t: {}, nf: 0, ms: 5000, sc: 80, e: [], ...over })

test('a page view becomes one view row with engaged time and scroll', () => {
  const rows = toRows(view(), meta)
  assert.equal(rows.length, 1)
  assert.equal(rows[0].kind, 'view')
  assert.equal(rows[0].engaged_ms, 5000)
  assert.equal(rows[0].scroll_pct, 80)
  assert.equal(rows[0].device, 'mobile')
  assert.equal(rows[0].country, 'US')
})

test('nothing identifying is in a row', () => {
  const row = toRows(view(), meta)[0]
  for (const k of Object.keys(row)) assert.ok(!/ip|ua|agent|id/.test(k), k)
  assert.ok(!JSON.stringify(row).includes('iPhone'))
})

test('foreign host, mismatched Origin or wrong version is dropped', () => {
  assert.deepEqual(toRows(view({ h: 'evil.example' }), { ...meta, origin: 'https://evil.example' }), [])
  assert.deepEqual(toRows(view({ h: 'cds.maxdraco.com' }), meta), [])
  assert.deepEqual(toRows(view(), { ...meta, origin: null }), [])
  assert.deepEqual(toRows(view({ v: 2 }), meta), [])
  assert.deepEqual(toRows(null, meta), [])
})

test('cds and hack count when their own Origin sends them', () => {
  assert.equal(toRows(view({ h: 'cds.maxdraco.com' }), { ...meta, origin: 'https://cds.maxdraco.com' }).length, 1)
  assert.equal(toRows(view({ h: 'hack.maxdraco.com' }), { ...meta, origin: 'https://hack.maxdraco.com' }).length, 1)
})

test('referrer keeps host and path, never the query', () => {
  assert.deepEqual(splitReferrer('https://www.google.com/search?q=max+draco'), ['www.google.com', '/search'])
  assert.deepEqual(splitReferrer('android-app://com.slack'), [null, null])
  assert.deepEqual(splitReferrer('not a url'), [null, null])
  const row = toRows(view({ r: 'https://Bsky.app/profile/x?token=secret' }), meta)[0]
  assert.equal(row.ref_host, 'bsky.app')
  assert.ok(!JSON.stringify(row).includes('secret'))
})

test('path loses query and fragment; a path that is not absolute is dropped', () => {
  assert.equal(toRows(view({ p: '/blog/?email=a@b.c#x' }), meta)[0].path, '/blog/')
  assert.deepEqual(toRows(view({ p: 'blog' }), meta), [])
})

test('tags are kept, clipped to 64 chars', () => {
  const row = toRows(view({ t: { ref: 'bluesky', utm_source: 'x'.repeat(500), other: 'dropped' } }), meta)[0]
  assert.equal(row.tag_ref, 'bluesky')
  assert.equal(row.utm_source.length, 64)
  assert.ok(!('other' in row))
})

test('a 404 page view is kind notfound', () => {
  assert.equal(toRows(view({ nf: 1 }), meta)[0].kind, 'notfound')
})

test('outbound clicks and errors become their own rows; at most 20 events', () => {
  const e = [{ k: 'out', u: 'bsky.app/profile/maxdraco.com' }, { k: 'err', m: 'boom\nline2', f: '/js/gems.js', l: 12 }, { k: 'junk' }]
  const rows = toRows(view({ e }), meta)
  assert.deepEqual(rows.map(r => r.kind), ['view', 'out', 'err'])
  assert.equal(rows[1].target, 'bsky.app/profile/maxdraco.com')
  assert.equal(rows[2].target, '/js/gems.js:12')
  assert.equal(rows[2].detail, 'boom line2')
  const many = Array.from({ length: 50 }, () => ({ k: 'out', u: 'a.example/' }))
  assert.equal(toRows(view({ e: many }), meta).length, 21)
})

test('numbers are clamped, junk numbers become null', () => {
  const row = toRows(view({ ms: 1e12, sc: 900 }), meta)[0]
  assert.equal(row.engaged_ms, 6 * 3600 * 1000)
  assert.equal(row.scroll_pct, 100)
  assert.equal(toRows(view({ ms: 'abc' }), meta)[0].engaged_ms, null)
})

test('continuation sends carry cont > 0', () => {
  assert.equal(toRows(view({ c: 2 }), meta)[0].cont, 2)
})

test('device class only', () => {
  assert.equal(deviceClass('Mozilla/5.0 (Macintosh)'), 'desktop')
  assert.equal(deviceClass(''), null)
})
