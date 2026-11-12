// Site search for maxdraco.com (card maxdraco-dictionary, Max 2026-11-11).
// Reads /search-index.json (built by Hugo from layouts/index.searchindex.json: published pages only)
// and suggests pages as you type. No third-party service: the index and matcher are both here.
//
// The header box is an ARIA 1.2 combobox (list autocomplete): Down/Up move through the
// suggestions, Enter opens the highlighted one (or the full results page), Escape closes then
// clears. /search/?q= renders the full result list with the same matcher, and is where the form
// goes without JavaScript.
(function () {
  "use strict";
  var MAX_SUGGEST = 8;
  var index = null;
  var loading = null;

  function norm(s) {
    return (s || "").toLowerCase().normalize("NFKD").replace(/[̀-ͯ]/g, "")
      .replace(/[^a-z0-9.()\-:]+/g, " ").trim();
  }
  function words(s) { return norm(s).split(/[\s\-:]+/).filter(Boolean); }

  function load() {
    if (index) return Promise.resolve(index);
    if (!loading) {
      loading = fetch("/search-index.json", { credentials: "omit" })
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function (d) {
          index = (d.pages || []).map(function (p) {
            return { p: p, title: norm(p.t), tw: words(p.t), kw: words(p.w + " " + p.k), sw: words(p.s) };
          });
          return index;
        })
        .catch(function (e) { loading = null; throw e; });
    }
    return loading;
  }

  // At most one edit (insert, delete, substitute, or swap of neighbours) between a and b.
  function near(a, b) {
    if (a === b) return true;
    var la = a.length, lb = b.length;
    if (Math.abs(la - lb) > 1) return false;
    var i = 0;
    while (i < la && i < lb && a[i] === b[i]) i++;
    if (la === lb) {
      return a.slice(i + 1) === b.slice(i + 1) ||
        (a[i] === b[i + 1] && a[i + 1] === b[i] && a.slice(i + 2) === b.slice(i + 2));
    }
    return la > lb ? a.slice(i + 1) === b.slice(i) : a.slice(i) === b.slice(i + 1);
  }

  function tokenScore(e, t) {
    var best = 0, i, w;
    for (i = 0; i < e.tw.length; i++) {
      w = e.tw[i];
      if (w === t) best = Math.max(best, 40);
      else if (w.indexOf(t) === 0) best = Math.max(best, 30);
      else if (t.length >= 4 && near(w.slice(0, t.length), t)) best = Math.max(best, 12);
    }
    if (best < 20 && e.title.indexOf(t) >= 0) best = 20;
    for (i = 0; i < e.kw.length && best < 15; i++) if (e.kw[i].indexOf(t) === 0) best = 15;
    for (i = 0; i < e.sw.length && best < 8; i++) if (e.sw[i].indexOf(t) === 0) best = 8;
    return best;
  }

  function search(q) {
    var toks = words(q), nq = norm(q), out = [];
    if (!toks.length || !index) return out;
    index.forEach(function (e) {
      var total = 0;
      for (var i = 0; i < toks.length; i++) {
        var s = tokenScore(e, toks[i]);
        if (!s) return;               // every word must match somewhere
        total += s;
      }
      if (e.title === nq) total += 60;
      else if (e.title.indexOf(nq) === 0) total += 30;
      out.push({ e: e, s: total });
    });
    out.sort(function (a, b) { return b.s - a.s || a.e.p.t.localeCompare(b.e.p.t); });
    return out.map(function (r) { return r.e.p; });
  }

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  function combobox(form) {
    var input = form.querySelector("[role=combobox]");
    var list = document.getElementById(input.getAttribute("aria-controls"));
    var status = form.querySelector("[role=status]");
    var items = [], active = -1, seq = 0;

    function setOpen(open) {
      list.hidden = !open;
      input.setAttribute("aria-expanded", open ? "true" : "false");
      if (!open) setActive(-1);
    }
    function setActive(i) {
      if (active >= 0 && list.children[active]) list.children[active].setAttribute("aria-selected", "false");
      active = i;
      if (i >= 0 && list.children[i]) {
        var li = list.children[i];
        li.setAttribute("aria-selected", "true");
        input.setAttribute("aria-activedescendant", li.id);
        li.scrollIntoView({ block: "nearest" });
      } else {
        input.removeAttribute("aria-activedescendant");
      }
    }
    function render(q) {
      var mine = ++seq;
      if (!norm(q)) { list.textContent = ""; items = []; setOpen(false); status.textContent = ""; return; }
      load().then(function () {
        if (mine !== seq) return;
        items = search(q).slice(0, MAX_SUGGEST);
        list.textContent = "";
        items.forEach(function (p, i) {
          var li = el("li", "ds-search-opt");
          li.id = input.id + "-opt-" + i;
          li.setAttribute("role", "option");
          li.setAttribute("aria-selected", "false");
          li.appendChild(el("span", "ds-search-title", p.t));
          li.appendChild(el("span", "ds-search-kind", p.k));
          li.addEventListener("mousedown", function (ev) { ev.preventDefault(); });
          li.addEventListener("click", function () { location.href = p.u; });
          list.appendChild(li);
        });
        if (!items.length) {
          var none = el("li", "ds-search-none", "No pages match. Press Enter to search anyway.");
          none.setAttribute("role", "option");
          none.setAttribute("aria-disabled", "true");
          none.id = input.id + "-none";
          list.appendChild(none);
        }
        active = -1;
        setOpen(true);
        status.textContent = items.length ? items.length + (items.length === 1 ? " suggestion" : " suggestions") +
          ", use the arrow keys to choose" : "No suggestions";
      }, function () {
        if (mine !== seq) return;
        status.textContent = "Search is unavailable right now. Press Enter to try the results page.";
      });
    }

    input.addEventListener("input", function () { render(input.value); });
    input.addEventListener("focus", function () { load().catch(function () {}); });
    input.addEventListener("keydown", function (ev) {
      var open = !list.hidden && items.length;
      if (ev.key === "ArrowDown") {
        ev.preventDefault();
        if (list.hidden && input.value) { render(input.value); return; }
        if (open) setActive(active + 1 >= items.length ? 0 : active + 1);
      } else if (ev.key === "ArrowUp") {
        ev.preventDefault();
        if (open) setActive(active <= 0 ? items.length - 1 : active - 1);
      } else if (ev.key === "Enter") {
        if (open && active >= 0) { ev.preventDefault(); location.href = items[active].u; }
      } else if (ev.key === "Escape") {
        if (!list.hidden) { ev.preventDefault(); setOpen(false); }
        else if (input.value) { ev.preventDefault(); input.value = ""; render(""); }
      } else if (ev.key === "Tab") {
        setOpen(false);
      }
    });
    input.addEventListener("blur", function () { setOpen(false); });
  }

  function resultsPage(root) {
    var q = new URLSearchParams(location.search).get("q") || "";
    var box = document.getElementById("site-search");
    if (box && q) box.value = q;
    var heading = root.querySelector("[data-search-heading]");
    var ol = root.querySelector("[data-search-results]");
    if (!q.trim()) { heading.textContent = "Type in the search box to find a page."; return; }
    load().then(function () {
      var hits = search(q);
      heading.textContent = hits.length ? hits.length + (hits.length === 1 ? " page matches " : " pages match ") +
        "“" + q + "”" : "No pages match “" + q + "”.";
      hits.forEach(function (p) {
        var li = el("li", "ds-search-result");
        var a = el("a", null, p.t);
        a.href = p.u;
        li.appendChild(a);
        li.appendChild(el("span", "ds-search-kind", p.k));
        if (p.s) li.appendChild(el("p", "ds-meta", p.s));
        ol.appendChild(li);
      });
    }, function () { heading.textContent = "Search is unavailable right now."; });
  }

  document.querySelectorAll("form.ds-search").forEach(combobox);
  var page = document.querySelector("[data-search-page]");
  if (page) resultsPage(page);
})();
