/* The Fix: Nico Paz deep dive. Interactive layer: scatter lab, shot filters, animated move,
   scroll reveals and a compare picker. No libraries. Respects prefers-reduced-motion. */
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var RM = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var NS = "http://www.w3.org/2000/svg";
  var C = { paper: "#E8E4DA", shade: "#DCD7CB", ink: "#121212", soft: "#6E6A62", sig: "#FF5A1F", grey: "#8F8A80" };

  // Serie A 2025/26, attacking midfielders (FotMob league stats): name, tackles/90, total tackles, dribbles/90, ball won final third/90
  var AMS = [["Nico Paz", 2.8, 91, 2.2, 0.8], ["Fabio Miretti", 2.8, 19, 1.0, 1.9], ["Junior Messias", 2.7, 20, 2.7, 1.1],
    ["Mattéo Tramoni", 1.8, 32, 0.4, 1.0], ["Lassana Coulibaly", 1.6, 48, 0.8, 0.5], ["Nicola Zalewski", 1.4, 29, 1.3, 0.4],
    ["Jens Odgaard", 1.4, 21, 0.5, 0.8], ["Stephan El Shaarawy", 1.4, 10, 1.6, 0.7], ["Weston McKennie", 1.3, 40, 0.5, 0.4],
    ["Eljif Elmas", 1.2, 24, 0.7, 0.5], ["Edon Zhegrova", 1.2, 5, 5.1, 1.2], ["Ruben Loftus-Cheek", 1.1, 14, 1.0, 0.4],
    ["Lazar Samardžić", 1.1, 12, 1.2, 0.9], ["Charles De Ketelaere", 1.0, 24, 2.0, 0.8], ["Arthur Atta", 0.9, 27, 2.2, 0.5],
    ["Giovanni Fabbian", 0.9, 12, 0.5, 0.2], ["Gaetano Oristanio", 0.9, 9, 1.6, 0.5], ["Matías Soulé", 0.8, 19, 1.5, 1.6],
    ["Kamaldeen Sulemana", 0.8, 9, 2.0, 0.5], ["Omri Gandelman", 0.8, 9, 0.2, 0.5], ["Lorenzo Pellegrini", 0.7, 12, 0.3, 0.4],
    ["Paulo Dybala", 0.7, 10, 1.3, 0.9]];
  var STATS = { t: { i: 1, max: 3.2, label: "TACKLES PER 90", short: "tackles" },
                d: { i: 3, max: 5.6, label: "DRIBBLES PER 90", short: "dribbles" },
                f: { i: 4, max: 2.2, label: "BALL WON IN FINAL THIRD PER 90", short: "won in final third" } };
  function mins(a) { return a[0] === "Nico Paz" ? 2882 : a[2] / a[1] * 90; }
  function el(tag, attrs, parent) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function median(arr) { var s = arr.slice().sort(function (a, b) { return a - b; }); var m = s.length / 2; return s.length % 2 ? s[Math.floor(m)] : (s[m - 1] + s[m]) / 2; }

  /* ---------- shared tooltip ---------- */
  var tip = document.getElementById("tip");
  function showTip(t, x, y) {
    if (!tip) return; tip.textContent = t; tip.classList.add("on");
    var w = tip.offsetWidth, h = tip.offsetHeight, L = Math.min(window.innerWidth - w - 8, x + 14), T = y - h - 14;
    if (T < 8) T = y + 18; tip.style.left = L + "px"; tip.style.top = T + "px";
  }
  function hideTip() { if (tip) tip.classList.remove("on"); }
  function bindTip(node, txtFn) {
    node.setAttribute("tabindex", "0");
    node.addEventListener("pointerenter", function (e) { showTip(txtFn(), e.clientX, e.clientY); });
    node.addEventListener("pointermove", function (e) { showTip(txtFn(), e.clientX, e.clientY); });
    node.addEventListener("pointerleave", hideTip);
    node.addEventListener("click", function (e) { showTip(txtFn(), e.clientX, e.clientY); e.stopPropagation(); });
    node.addEventListener("focus", function () { var r = node.getBoundingClientRect(); showTip(txtFn(), r.right, r.top); });
    node.addEventListener("blur", hideTip);
  }
  // static SVG titles -> instant tooltips
  document.querySelectorAll("svg title").forEach(function (ti) {
    var n = ti.parentNode, txt = ti.textContent; n.setAttribute("aria-label", txt); ti.remove();
    bindTip(n, function () { return txt; });
  });
  document.addEventListener("click", hideTip);
  window.addEventListener("scroll", hideTip, { passive: true });

  /* ---------- compare picker state ---------- */
  var compare = "";
  var listeners = [];
  function setCompare(name) { compare = name; listeners.forEach(function (f) { f(); }); }

  /* ---------- 1. scatter lab ---------- */
  var lab = document.getElementById("scatterLab");
  if (lab) {
    var W = 1000, H = 720, x0 = 80, x1 = 960, y0 = 30, y1 = 640;
    var svg = el("svg", { viewBox: "0 0 " + W + " " + H, role: "img", "aria-label": "Interactive scatter of the 22 Serie A attacking midfielders" });
    lab.querySelector(".chart").appendChild(svg);
    var gq = el("g", {}, svg), gAxes = el("g", {}, svg), gDots = el("g", {}, svg);
    var xs = lab.querySelector("[name=x]"), ys = lab.querySelector("[name=y]"), slider = lab.querySelector("[name=min]");
    var out = lab.querySelector(".mins"), cnt = lab.querySelector(".count");
    var dots = AMS.map(function (a) {
      var g = el("g", { class: "pt" + (a[0] === "Nico Paz" ? " paz" : "") }, gDots);
      var r = 6 + 18 * Math.sqrt(mins(a) / 3000);
      if (a[0] === "Nico Paz") el("circle", { r: r + 4, fill: C.ink }, g);
      el("circle", { r: r, fill: a[0] === "Nico Paz" ? C.sig : C.grey, "fill-opacity": a[0] === "Nico Paz" ? 1 : 0.75, stroke: C.paper, "stroke-width": 2 }, g);
      var t = el("text", { x: -(r + 12), y: 9, "text-anchor": "end", class: a[0] === "Nico Paz" ? "pazlab" : "nmlab" }, g);
      t.textContent = a[0] === "Nico Paz" ? "PAZ" : a[0].split(" ").slice(-1)[0];
      bindTip(g, function () {
        var X = STATS[xs.value], Y = STATS[ys.value];
        return a[0] + ": " + a[X.i] + " " + X.short + ", " + a[Y.i] + " " + Y.short + " per 90, about " + Math.round(mins(a) / 10) * 10 + " min";
      });
      return { a: a, g: g, r: r };
    });
    function draw() {
      var X = STATS[xs.value], Y = STATS[ys.value], minM = +slider.value;
      out.textContent = minM === 0 ? "everyone" : minM.toLocaleString("en-GB") + "+ minutes";
      function px(v) { return x0 + (x1 - x0) * v / X.max; }
      function py(v) { return y1 - (y1 - y0) * v / Y.max; }
      var mx = median(AMS.map(function (a) { return a[X.i]; })), my = median(AMS.map(function (a) { return a[Y.i]; }));
      gq.innerHTML = ""; gAxes.innerHTML = "";
      el("rect", { x: px(mx), y: y0, width: x1 - px(mx), height: py(my) - y0, fill: C.sig, "fill-opacity": 0.1 }, gq);
      var ql = el("text", { x: x1 - 8, y: y0 + 22, "text-anchor": "end", class: "ql" }, gq); ql.textContent = "ABOVE THE MIDDLE ON BOTH";
      el("line", { x1: px(mx), x2: px(mx), y1: y0, y2: y1, stroke: C.soft, "stroke-width": 2, "stroke-dasharray": "7 6" }, gAxes);
      el("line", { x1: x0, x2: x1, y1: py(my), y2: py(my), stroke: C.soft, "stroke-width": 2, "stroke-dasharray": "7 6" }, gAxes);
      el("line", { x1: x0, x2: x1, y1: y1, y2: y1, stroke: C.ink, "stroke-width": 3 }, gAxes);
      el("line", { x1: x0, x2: x0, y1: y0, y2: y1, stroke: C.ink, "stroke-width": 3 }, gAxes);
      var step = X.max > 4 ? 1 : 0.5;
      for (var v = 0; v <= X.max + 1e-9; v += step) { var t = el("text", { x: px(v), y: y1 + 26, "text-anchor": "middle", class: "tick" }, gAxes); t.textContent = +v.toFixed(1); }
      step = Y.max > 4 ? 1 : 0.5;
      for (v = 0; v <= Y.max + 1e-9; v += step) { t = el("text", { x: x0 - 12, y: py(v) + 5, "text-anchor": "end", class: "tick" }, gAxes); t.textContent = +v.toFixed(1); }
      var xl = el("text", { x: (x0 + x1) / 2, y: y1 + 58, "text-anchor": "middle", class: "axl" }, gAxes); xl.textContent = X.label + " →";
      var yl = el("text", { transform: "translate(24 " + (y0 + y1) / 2 + ") rotate(-90)", "text-anchor": "middle", class: "axl" }, gAxes); yl.textContent = Y.label + " →";
      var shown = 0, beat = 0, pz = AMS[0];
      dots.forEach(function (d) {
        var on = mins(d.a) >= minM || d.a[0] === "Nico Paz";
        if (on) { shown++; if (d.a[0] !== "Nico Paz" && d.a[X.i] >= pz[X.i] && d.a[Y.i] >= pz[Y.i]) beat++; }
        d.g.style.transform = "translate(" + px(d.a[X.i]) + "px," + py(d.a[Y.i]) + "px)";
        d.g.classList.toggle("off", !on);
        d.g.classList.toggle("cmp", d.a[0] === compare);
      });
      cnt.textContent = "Showing " + shown + " of 22. " + (beat === 0 ? "Nobody shown matches Paz on both." : beat + " shown match" + (beat === 1 ? "es" : "") + " or beat Paz on both.");
    }
    [xs, ys, slider].forEach(function (c) { c.addEventListener("input", draw); });
    listeners.push(draw);
    draw();
  }

  /* ---------- 2. shot filters ---------- */
  var shotLab = document.getElementById("shotLab");
  if (shotLab) {
    var season = "2526", filt = "all";
    var maps = shotLab.querySelectorAll(".maps [data-season]"), sc = shotLab.querySelector(".count");
    var tests = { all: function () { return true; }, goal: function (g) { return g.dataset.goal === "1"; },
      "in": function (g) { return g.dataset.in === "1"; }, out: function (g) { return g.dataset.in === "0"; }, fk: function (g) { return g.dataset.fk === "1"; } };
    function apply() {
      maps.forEach(function (m) { m.hidden = m.dataset.season !== season; });
      var m = shotLab.querySelector(".maps [data-season='" + season + "']"), gs = m.querySelectorAll(".shot"), n = 0, goals = 0;
      gs.forEach(function (g) { var ok = tests[filt](g); g.classList.toggle("off", !ok); if (ok) { n++; if (g.dataset.goal === "1") goals++; } });
      var lab = { all: "shots", "in": "shots inside the box", out: "shots from outside the box", fk: "direct free kicks" };
      sc.textContent = filt === "goal" ? goals + " goals from " + gs.length + " shots on the map." :
        filt === "all" ? gs.length + " shots on the map, " + goals + " scored." :
        n + " of " + gs.length + " " + lab[filt] + ", " + goals + " scored.";
      shotLab.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.season === season || b.dataset.f === filt)); });
    }
    shotLab.querySelectorAll("button").forEach(function (b) {
      b.addEventListener("click", function () { if (b.dataset.season) season = b.dataset.season; if (b.dataset.f) filt = b.dataset.f; apply(); });
    });
    apply();
  }

  /* ---------- 3. the move, animated ---------- */
  var board = document.querySelector("svg[aria-label*='signature']");
  function playMove() {
    if (!board) return;
    var parts = ["mv-carry", "mv-shot", "mv-pass"].map(function (id) { return board.querySelector("#" + id); });
    var goals = board.querySelectorAll(".gm"), labels = board.querySelectorAll(".mvl");
    if (RM) { parts.concat([].slice.call(goals), [].slice.call(labels)).forEach(function (n) { n.style.opacity = 1; }); return; }
    var carry = parts[0].querySelector("path"), shot = parts[1].querySelector("path");
    parts.forEach(function (p) { p.style.opacity = 0; });
    goals.forEach(function (g) { g.style.opacity = 0; g.style.transform = "scale(.2)"; });
    labels.forEach(function (l) { l.style.opacity = 0; });
    var ball = board.querySelector("#mv-ball") || el("circle", { id: "mv-ball", r: 8, fill: "#fff", stroke: C.ink, "stroke-width": 3 }, board);
    function along(path, ms, done) {
      var L = path.getTotalLength(), t0 = null;
      function f(ts) { if (!t0) t0 = ts; var k = Math.min(1, (ts - t0) / ms), e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
        var p = path.getPointAtLength(L * e); ball.setAttribute("cx", p.x); ball.setAttribute("cy", p.y);
        if (k < 1) requestAnimationFrame(f); else done && done(); }
      requestAnimationFrame(f);
    }
    ball.style.opacity = 1;
    parts[0].style.transition = "opacity .4s"; parts[0].style.opacity = 1; labels[0] && (labels[0].style.opacity = 1); labels[1] && (labels[1].style.opacity = 1);
    along(carry, 700, function () {
      parts[1].style.transition = "opacity .3s"; parts[1].style.opacity = 1; labels[2] && (labels[2].style.opacity = 1);
      along(shot, 900, function () {
        ball.style.opacity = 0;
        parts[2].style.transition = "opacity .5s"; parts[2].style.opacity = 1; labels[3] && (labels[3].style.opacity = 1);
        goals.forEach(function (g, i) { setTimeout(function () { g.style.transition = "opacity .3s, transform .35s cubic-bezier(.2,1.6,.4,1)"; g.style.opacity = 1; g.style.transform = "scale(1)"; }, 250 + i * 220); });
      });
    });
  }
  var replay = document.getElementById("replay");
  if (replay) replay.addEventListener("click", playMove);
  if (board) board.querySelectorAll(".gm").forEach(function (g) { g.style.transformBox = "fill-box"; g.style.transformOrigin = "center"; });

  /* ---------- 4. scroll reveals ---------- */
  function countUp(node) {
    var to = +node.dataset.count, t0 = null;
    if (RM) { node.textContent = to; return; }
    function f(ts) { if (!t0) t0 = ts; var k = Math.min(1, (ts - t0) / 900); node.textContent = Math.round(to * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(f); }
    requestAnimationFrame(f);
  }
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      var t = e.target; io.unobserve(t);
      t.classList.add("in");
      if (t.matches(".score")) t.querySelectorAll("[data-count]").forEach(countUp);
      if (t === board) playMove();
    });
  }, { threshold: 0.35 });
  document.querySelectorAll(".score, .touch, .strips").forEach(function (n) { io.observe(n); });
  if (board) io.observe(board);

  /* ---------- 5. compare picker ---------- */
  var pickers = document.querySelectorAll("select.compare");
  pickers.forEach(function (s) {
    AMS.slice(1).map(function (a) { return a[0]; }).sort().forEach(function (n) { var o = document.createElement("option"); o.value = n; o.textContent = n; s.appendChild(o); });
    s.addEventListener("change", function () { pickers.forEach(function (o) { o.value = s.value; }); setCompare(s.value); });
  });
  listeners.push(function () {
    document.querySelectorAll(".strips svg").forEach(function (sv) {
      sv.querySelectorAll(".cmplab").forEach(function (n) { n.remove(); });
      sv.querySelectorAll(".sd").forEach(function (c) {
        var on = c.dataset.name === compare; c.classList.toggle("cmp", on);
        if (on) { var t = el("text", { x: c.getAttribute("cx"), y: +c.getAttribute("cy") - 16, "text-anchor": "middle", class: "cmplab" }, sv); t.textContent = compare.split(" ").slice(-1)[0]; }
      });
    });
  });
})();
