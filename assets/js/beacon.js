/*
  First-party page beacon for maxdraco.com, cds.maxdraco.com and hack.maxdraco.com
  (card site-beacon-first-party). Fills the gaps Cloudflare Web Analytics leaves:
  how long a page was actually read, how far down, which outbound links get clicked,
  ?ref= / utm_* tags, JavaScript errors from our own scripts, and 404 hits with the
  page that linked to them.

  What it does NOT do: no cookies, no localStorage/sessionStorage, no ID of any kind,
  nothing that links one page view to another. The server keeps no IP address and no
  user agent (only "mobile"/"desktop" and Cloudflare's country code). Skipped entirely
  when the browser sends Global Privacy Control or Do Not Track, or is automated.

  Visitors in the EU/EEA, the UK and Switzerland: nothing runs. Their cookie rules (ePrivacy
  Directive Art. 5(3), UK PECR reg. 6) cover scripts that read the browser and send it back even
  without cookies (EDPB Guidelines 2/2023 par. 33), and Max chose an always-on beacon over a
  consent prompt. So the script first asks GET /api/b?g=1, which answers "1" only when
  Cloudflare places the visitor outside those countries; until then it reads nothing.

  One request each time the tab is hidden or closed (sendBeacon). The first carries c=0;
  if the reader comes back to the tab, the next one carries c=1, 2... with only the time
  and events since the last send, so the server counts one view but all of the reading. Hugo publishes an unfingerprinted copy at https://maxdraco.com/js/beacon.js so the
  other two sites can load the same file.
*/
(function () {
  'use strict'
  var nav = navigator
  if (nav.webdriver || nav.globalPrivacyControl || nav.doNotTrack === '1' || window.doNotTrack === '1') return
  if (!nav.sendBeacon || !window.Blob || !window.fetch) return

  // Local `wrangler pages dev` posts to itself; every real page posts to maxdraco.com.
  var ENDPOINT = /^(localhost|127\.0\.0\.1)$/.test(location.hostname) ? '/api/b' : 'https://maxdraco.com/api/b'

  // Location gate (see the header): any answer but "1", or no answer, means stay off.
  fetch(ENDPOINT + '?g=1', { credentials: 'omit', cache: 'no-store' })
    .then(function (r) { return r.ok ? r.text() : '' })
    .then(function (t) { if (t === '1') run() }, function () {})

  function run () {
    var TAGS = ['ref', 'utm_source', 'utm_medium', 'utm_campaign']
    var MAX_EVENTS = 20
    var loc = window.location
    var start = Date.now()
    var visibleSince = document.visibilityState === 'visible' ? start : null
    var engagedMs = 0
    var maxScroll = 0
    var events = []
    var seq = 0

    function tags () {
      var out = {}
      try {
        var q = new URLSearchParams(loc.search)
        for (var i = 0; i < TAGS.length; i++) {
          var v = q.get(TAGS[i])
          if (v) out[TAGS[i]] = v.slice(0, 64)
        }
      } catch (e) {}
      return out
    }

    function scrollPct () {
      var doc = document.documentElement
      var seen = (window.scrollY || doc.scrollTop || 0) + window.innerHeight
      var total = Math.max(doc.scrollHeight, 1)
      return Math.min(100, Math.round(seen / total * 100))
    }

    function push (ev) { if (events.length < MAX_EVENTS) events.push(ev) }

    window.addEventListener('scroll', function () {
      var p = scrollPct()
      if (p > maxScroll) maxScroll = p
    }, { passive: true })

    // Outbound clicks: host + path of the link only (no query string).
    document.addEventListener('click', function (e) {
      var a = e.target && e.target.closest ? e.target.closest('a[href]') : null
      if (!a) return
      var u
      try { u = new URL(a.href, loc.href) } catch (err) { return }
      if (u.protocol !== 'http:' && u.protocol !== 'https:') return
      if (u.hostname === loc.hostname) return
      push({ k: 'out', u: u.hostname + u.pathname })
    }, true)

    // Errors from our own scripts only; extension and third-party noise is dropped here.
    window.addEventListener('error', function (e) {
      var file = e.filename || ''
      var own = /^https:\/\/((www|cds|hack)\.)?maxdraco\.com\//.test(file) || file.indexOf(loc.origin + '/') === 0
      if (!own) return
      var path = file.replace(/^https?:\/\/[^/]+/, '').split('?')[0]
      push({ k: 'err', m: String(e.message || '').slice(0, 200), f: path.slice(0, 120), l: e.lineno || 0 })
    })

    function flush () {
      if (visibleSince !== null) { engagedMs += Date.now() - visibleSince; visibleSince = null }
      var p = scrollPct()
      if (p > maxScroll) maxScroll = p
      if (seq > 0 && engagedMs < 1000 && !events.length) return
      var body = {
        v: 1,
        c: seq,
        h: loc.hostname,
        p: loc.pathname,
        r: document.referrer || '',
        t: tags(),
        nf: document.querySelector('[data-beacon-404]') ? 1 : 0,
        ms: Math.min(engagedMs, 6 * 3600 * 1000),
        sc: maxScroll,
        e: events
      }
      try {
        nav.sendBeacon(ENDPOINT, new Blob([JSON.stringify(body)], { type: 'text/plain' }))
      } catch (e) {}
      seq++
      events = []
      engagedMs = 0
    }

    document.addEventListener('visibilitychange', function () {
      if (document.visibilityState === 'hidden') flush()
      else if (visibleSince === null) visibleSince = Date.now()
    })
    window.addEventListener('pagehide', flush)
    // A tab restored from the back/forward cache is a new view of the page.
    window.addEventListener('pageshow', function (e) {
      if (!e.persisted) return
      seq = 0
      events = []
      engagedMs = 0
      maxScroll = 0
      visibleSince = Date.now()
    })
  }
})()
