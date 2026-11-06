// Hidden gems. Three are hidden on the site; nothing shows until a visitor
// finds one. After that a gem floats top-right on every page with the global
// count of finds (functions/api/gems.js) and how many of the three they have.
//
// Where they are (the repo is public and this file is one view-source away,
// so there is no point hiding the list here):
//   online  click the green "Online" light in the status bar 3 times quickly
//   typed   type "draco" anywhere on a page (not inside a text field)
//   lost    the faint gem on the 404 page
//
// What the browser keeps: localStorage "gems.found" = the ids found, on this
// origin only. No cookie, no id, nothing sent but which gem was found.
(function () {
  var KEY = 'gems.found'
  var EGGS = ['online', 'typed', 'lost']
  var API = '/api/gems'
  var still = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches
  var hud, totalEl, mineEl, panel, shown = null

  function load () {
    try {
      var v = JSON.parse(localStorage.getItem(KEY) || '[]')
      return Array.isArray(v) ? v.filter(function (e) { return EGGS.indexOf(e) >= 0 }) : []
    } catch (e) { return [] }
  }
  function save (list) { try { localStorage.setItem(KEY, JSON.stringify(list)) } catch (e) {} }

  var GEM = '<svg viewBox="0 0 40 36" aria-hidden="true" class="gem-svg">' +
    '<polygon class="f1" points="8,2 32,2 40,12 0,12"/>' +
    '<polygon class="f2" points="0,12 40,12 20,36"/>' +
    '<polygon class="f3" points="8,2 14,12 20,2"/>' +
    '<polygon class="f3" points="20,2 26,12 32,2"/>' +
    '<polygon class="f4" points="14,12 26,12 20,36"/>' +
    '<polygon class="f5" points="0,12 14,12 20,36"/>' +
    '<polyline class="edge" points="8,2 32,2 40,12 20,36 0,12 8,2"/>' +
    '</svg>'

  function fmt (n) { return Number(n).toLocaleString('en-US') }

  function build () {
    if (hud) return
    hud = document.createElement('div')
    hud.className = 'gem-hud'
    hud.innerHTML =
      '<button type="button" class="gem-btn" aria-expanded="false" aria-controls="gem-panel">' +
        '<span class="gem-float">' + GEM + '</span>' +
        '<span class="gem-total" aria-live="polite">?</span>' +
        '<span class="gem-mine"></span>' +
      '</button>' +
      '<div class="gem-panel" id="gem-panel" hidden>' +
        '<p class="gem-panel-head">Hidden gems</p>' +
        '<p class="gem-panel-mine"></p>' +
        '<p class="gem-panel-total"></p>' +
      '</div>'
    document.body.appendChild(hud)
    totalEl = hud.querySelector('.gem-total')
    mineEl = hud.querySelector('.gem-mine')
    panel = hud.querySelector('.gem-panel')
    var btn = hud.querySelector('.gem-btn')
    btn.addEventListener('click', function () {
      var open = panel.hidden
      panel.hidden = !open
      btn.setAttribute('aria-expanded', String(open))
    })
    document.addEventListener('click', function (e) {
      if (!panel.hidden && !hud.contains(e.target)) {
        panel.hidden = true
        btn.setAttribute('aria-expanded', 'false')
      }
    })
    if (!still) {
      hud.animate([
        { transform: 'scale(0) rotate(-30deg)', opacity: 0 },
        { transform: 'scale(1.3) rotate(8deg)', opacity: 1, offset: 0.6 },
        { transform: 'scale(1) rotate(0)', opacity: 1 }
      ], { duration: 520, easing: 'cubic-bezier(.2,.9,.3,1.3)' })
    }
  }

  function paint (found, total) {
    build()
    mineEl.textContent = found.length + '/' + EGGS.length
    var left = EGGS.length - found.length
    hud.querySelector('.gem-panel-mine').textContent =
      'You found ' + found.length + ' of ' + EGGS.length + '.' +
      (left ? ' ' + left + ' still hidden somewhere on this site.' : ' That is all of them.')
    if (total != null) {
      hud.querySelector('.gem-panel-total').textContent =
        'Found ' + fmt(total) + ' ' + (total === 1 ? 'time' : 'times') + ' by everyone so far.'
      tick(total)
    }
    hud.querySelector('.gem-btn').setAttribute('aria-label',
      'Hidden gems: you found ' + found.length + ' of ' + EGGS.length +
      (total != null ? ', ' + fmt(total) + ' finds by everyone' : ''))
  }

  // Count up from what is on screen to the new total.
  function tick (to) {
    var from = shown == null ? to : shown
    shown = to
    if (still || from === to) { totalEl.textContent = fmt(to); return }
    var start = performance.now(), dur = 600
    ;(function step (t) {
      var k = Math.min(1, (t - start) / dur)
      totalEl.textContent = fmt(Math.round(from + (to - from) * (1 - Math.pow(1 - k, 3))))
      if (k < 1) requestAnimationFrame(step)
    })(start)
  }

  // A damage number: pops out of the gem, arcs up and away, drops and fades.
  function pop (text) {
    if (!hud) return
    var n = document.createElement('span')
    n.className = 'gem-pop'
    n.textContent = text
    hud.appendChild(n)
    if (still) { setTimeout(function () { n.remove() }, 900); return }
    var dx = -30 - Math.random() * 40
    n.animate([
      { transform: 'translate(0,0) scale(0.4)', opacity: 0 },
      { transform: 'translate(' + dx * 0.35 + 'px,-34px) scale(1.6)', opacity: 1, offset: 0.18 },
      { transform: 'translate(' + dx * 0.7 + 'px,-46px) scale(1.15)', opacity: 1, offset: 0.45 },
      { transform: 'translate(' + dx + 'px,10px) scale(1)', opacity: 0 }
    ], { duration: 1100, easing: 'cubic-bezier(.25,.7,.5,1)' }).onfinish = function () { n.remove() }
    hud.querySelector('.gem-float').animate([
      { transform: 'scale(1)' }, { transform: 'scale(1.35) rotate(-10deg)' }, { transform: 'scale(1)' }
    ], { duration: 320, easing: 'ease-out' })
  }

  function get () {
    return fetch(API, { headers: { accept: 'application/json' } })
      .then(function (r) { return r.ok ? r.json() : null })
      .then(function (d) { return d && typeof d.total === 'number' ? d.total : null })
      .catch(function () { return null })
  }

  function find (egg) {
    var found = load()
    if (found.indexOf(egg) >= 0) {
      // Already yours: the gem just nods.
      if (hud && !still) {
        hud.querySelector('.gem-float').animate([
          { transform: 'rotate(0)' }, { transform: 'rotate(-14deg)' },
          { transform: 'rotate(10deg)' }, { transform: 'rotate(0)' }
        ], { duration: 400 })
      }
      return
    }
    found.push(egg)
    save(found)
    paint(found, null)
    pop('+1')
    fetch(API, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ egg: egg })
    })
      .then(function (r) { return r.json() })
      .then(function (d) { return d && typeof d.total === 'number' ? d.total : null })
      .catch(function () { return null })
      .then(function (total) { paint(found, total) })
  }

  // ---- the hiding places ----------------------------------------------------

  // online: the status bar light, 3 clicks within 1.5 s.
  var clicks = []
  document.addEventListener('click', function (e) {
    var dot = e.target.closest && e.target.closest('.ds-online')
    if (!dot) return
    var now = Date.now()
    clicks = clicks.filter(function (t) { return now - t < 1500 })
    clicks.push(now)
    if (clicks.length >= 3) { clicks = []; find('online') }
  })

  // typed: "draco" typed outside any text field.
  var typed = ''
  document.addEventListener('keydown', function (e) {
    var t = e.target
    if (e.metaKey || e.ctrlKey || e.altKey) return
    if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return
    if (!e.key || e.key.length !== 1) return
    typed = (typed + e.key.toLowerCase()).slice(-5)
    if (typed === 'draco') { typed = ''; find('typed') }
  })

  // lost: the faint gem on the 404 page.
  document.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('[data-gem="lost"]')) find('lost')
  })

  // Returning finders see their gem on every page.
  var found = load()
  if (found.length) {
    paint(found, null)
    get().then(function (total) { paint(load(), total) })
  }
})()
