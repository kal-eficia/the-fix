/* The Fix: Branthwaite or Bassey. Charts drawn from the JSON in #cbdata. No libraries.
   Hover or tap any mark for detail. Respects prefers-reduced-motion. */
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var RM = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var NS = "http://www.w3.org/2000/svg";
  var C = { paper: "#E8E4DA", shade: "#DCD7CB", ink: "#121212", soft: "#6E6A62", sig: "#FF5A1F", grey: "#9a958b" };
  var D = JSON.parse(document.getElementById("cbdata").textContent);
  var F = D.fields;
  var CB = D.cbs.map(function (r) { var o = {}; F.forEach(function (f, i) { o[f] = r[i]; }); return o; });
  var BRA = "Jarrad Branthwaite", BAS = "Calvin Bassey", MAG = "Harry Maguire", LIS = "Lisandro Martínez";
  var SHORT = {}; SHORT[BRA] = "BRANTHWAITE"; SHORT[BAS] = "BASSEY"; SHORT[MAG] = "MAGUIRE"; SHORT[LIS] = "LISANDRO";
  var STYLE = {}; STYLE[BRA] = { fill: C.sig, stroke: C.ink, r: 12 }; STYLE[BAS] = { fill: C.ink, stroke: C.paper, r: 12 };
  STYLE[MAG] = { fill: C.paper, stroke: C.ink, r: 10 }; STYLE[LIS] = { fill: C.paper, stroke: C.soft, r: 9 };
  var POS = { 34: "right centre-back", 35: "centre-back", 36: "left centre-back" };
  var M = {
    h: { l: "Height", u: "cm", d: 0 }, aer90: { l: "Aerial duels won per 90", u: "", d: 2 }, aerpct: { l: "Aerial duels won %", u: "%", d: 1 },
    ts: { l: "Top speed", u: " km/h", d: 1 }, spr90: { l: "Sprints per 90", u: "", d: 1 }, padj: { l: "Tackles + interceptions (possession-adjusted)", u: "", d: 2 },
    dp90: { l: "Times dribbled past per 90", u: "", d: 2, low: true }, rec90: { l: "Recoveries per 90", u: "", d: 2 }, clr90: { l: "Clearances per 90", u: "", d: 2 },
    pas90: { l: "Accurate passes per 90", u: "", d: 1 }, paspct: { l: "Pass accuracy", u: "%", d: 1 }, lb90: { l: "Accurate long balls per 90", u: "", d: 2 }
  };
  function fmt(k, v) { return (+v).toFixed(M[k].d) + M[k].u; }
  function rank(k, name) {
    var me = CB.filter(function (r) { return r.name === name; })[0]; if (!me) return null;
    var better = CB.filter(function (r) { return M[k].low ? r[k] < me[k] : r[k] > me[k]; }).length;
    return better + 1;
  }
  function ord(n) { var s = ["th", "st", "nd", "rd"], v = n % 100; return n + (s[(v - 20) % 10] || s[v] || s[0]); }
  function comma(n) { return n.toLocaleString("en-GB"); }
  function median(a) { var s = a.slice().sort(function (x, y) { return x - y; }), m = s.length / 2; return s.length % 2 ? s[Math.floor(m)] : (s[m - 1] + s[m]) / 2; }
  function el(tag, attrs, parent, text) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    if (parent) parent.appendChild(e);
    return e;
  }
  function svgRoot(host, w, h, label) { host.innerHTML = ""; return el("svg", { viewBox: "0 0 " + w + " " + h, role: "img", "aria-label": label }, host); }

  /* ---------- tooltip ---------- */
  var tip = document.getElementById("tip");
  function showTip(t, x, y) {
    tip.textContent = t; tip.classList.add("on");
    var w = tip.offsetWidth, h = tip.offsetHeight, L = Math.min(window.innerWidth - w - 8, x + 14), T = y - h - 14;
    if (T < 8) T = y + 18; tip.style.left = Math.max(8, L) + "px"; tip.style.top = T + "px";
  }
  function hideTip() { tip.classList.remove("on"); }
  function bindTip(node, txt) {
    node.setAttribute("tabindex", "0"); node.setAttribute("aria-label", txt.replace(/\n/g, ". "));
    node.addEventListener("pointerenter", function (e) { showTip(txt, e.clientX, e.clientY); });
    node.addEventListener("pointermove", function (e) { showTip(txt, e.clientX, e.clientY); });
    node.addEventListener("pointerleave", hideTip);
    node.addEventListener("click", function (e) { showTip(txt, e.clientX, e.clientY); e.stopPropagation(); });
    node.addEventListener("focus", function () { var r = node.getBoundingClientRect(); showTip(txt, r.right, r.top); });
    node.addEventListener("blur", hideTip);
  }
  document.addEventListener("click", hideTip);
  window.addEventListener("scroll", hideTip, { passive: true });

  /* ================= 03. physical map ================= */
  (function () {
    var host = document.getElementById("mapLab"); if (!host) return;
    var xs = "aerpct", ys = "ts", leftOnly = false, who = "";
    var pick = host.querySelector(".pick");
    CB.map(function (r) { return r.name; }).filter(function (n) { return !STYLE[n]; }).sort().forEach(function (n) {
      var o = document.createElement("option"); o.value = n; o.textContent = n; pick.appendChild(o);
    });
    function draw() {
      var W = 1000, H = 700, x0 = 80, x1 = 960, y0 = 30, y1 = 610;
      var xv = CB.map(function (r) { return r[xs]; }), yv = CB.map(function (r) { return r[ys]; });
      var xmin = Math.min.apply(null, xv), xmax = Math.max.apply(null, xv), ymin = Math.min.apply(null, yv), ymax = Math.max.apply(null, yv);
      var px = (xmax - xmin) * 0.06, py = (ymax - ymin) * 0.08; xmin -= px; xmax += px; ymin -= py; ymax += py;
      var X = function (v) { return x0 + (x1 - x0) * (v - xmin) / (xmax - xmin); }, Y = function (v) { return y1 - (y1 - y0) * (v - ymin) / (ymax - ymin); };
      var s = svgRoot(host.querySelector(".chart"), W, H, "Scatter of " + M[xs].l + " against " + M[ys].l + " for Premier League centre-backs");
      var mx = median(xv), my = median(yv);
      el("rect", { x: X(mx), y: y0, width: x1 - X(mx), height: Y(my) - y0, fill: C.sig, "fill-opacity": .1 }, s);
      el("text", { x: x1 - 8, y: y0 + 18, class: "ql", "text-anchor": "end" }, s, xs === "h" ? "TALL AND QUICK" : "STRONG IN THE AIR AND QUICK");
      function ticks(lo, hi, n) { var step = Math.pow(10, Math.floor(Math.log10((hi - lo) / n))), out = []; [1, 2, 5, 10].some(function (m) { if ((hi - lo) / (step * m) <= n) { step *= m; return true; } });
        for (var v = Math.ceil(lo / step) * step; v <= hi; v += step) out.push(+v.toFixed(4)); return out; }
      ticks(xmin, xmax, 8).forEach(function (v) { el("text", { x: X(v), y: y1 + 24, class: "tick", "text-anchor": "middle" }, s, String(v)); });
      ticks(ymin, ymax, 7).forEach(function (v) { el("text", { x: x0 - 12, y: Y(v) + 4, class: "tick", "text-anchor": "end" }, s, String(v)); });
      el("line", { x1: x0, x2: x1, y1: y1, y2: y1, stroke: C.ink, "stroke-width": 2 }, s);
      el("line", { x1: x0, x2: x0, y1: y0, y2: y1, stroke: C.ink, "stroke-width": 2 }, s);
      el("line", { x1: X(mx), x2: X(mx), y1: y0, y2: y1, stroke: C.soft, "stroke-dasharray": "6 6" }, s);
      el("line", { x1: x0, x2: x1, y1: Y(my), y2: Y(my), stroke: C.soft, "stroke-dasharray": "6 6" }, s);
      el("text", { x: (x0 + x1) / 2, y: y1 + 58, class: "axl", "text-anchor": "middle" }, s, M[xs].l.toUpperCase() + " →");
      el("text", { x: 18, y: (y0 + y1) / 2, class: "axl", "text-anchor": "middle", transform: "rotate(-90 18 " + (y0 + y1) / 2 + ")" }, s, M[ys].l.toUpperCase() + " →");
      var shown = 0, gO = el("g", {}, s), gK = el("g", {}, s);
      CB.slice().sort(function (a, b) { return (STYLE[a.name] ? 1 : 0) - (STYLE[b.name] ? 1 : 0); }).forEach(function (r) {
        var st = STYLE[r.name], hit = who && r.name === who;
        var on = !leftOnly || r.pos === 36 || st;
        var g = el("g", { class: "pt" + (on ? "" : " off") }, st || hit ? gK : gO);
        if (on) shown++;
        el("circle", { cx: X(r[xs]), cy: Y(r[ys]), r: st ? st.r : hit ? 10 : 7, fill: st ? st.fill : hit ? C.ink : C.grey,
          stroke: st ? st.stroke : C.paper, "stroke-width": st ? 3 : 1.5 }, g);
        if (st || hit) {
          var right = X(r[xs]) < 820, lab = st ? SHORT[r.name] : r.name.split(" ").slice(-1)[0].toUpperCase();
          el("text", { x: X(r[xs]) + (right ? 16 : -16), y: Y(r[ys]) + 4, class: "lab" + (r.name === BRA ? " s" : ""), "text-anchor": right ? "start" : "end" }, g, lab);
        }
        bindTip(g, r.name + " (" + r.team + ", " + POS[r.pos] + ")\n" + M[xs].l + ": " + fmt(xs, r[xs]) + " · " + ord(rank(xs, r.name)) + " of 51\n" +
          M[ys].l + ": " + fmt(ys, r[ys]) + " · " + ord(rank(ys, r.name)) + " of 51\n" + comma(r.min) + " minutes");
      });
      host.querySelector(".count").textContent = "Showing " + shown + " of 51 centre-backs" + (leftOnly ? " (left centre-backs, plus the four we're comparing)." : ".");
    }
    host.querySelector(".xs").addEventListener("change", function (e) { xs = e.target.value; draw(); });
    host.querySelector(".ys").addEventListener("change", function (e) { ys = e.target.value; draw(); });
    host.querySelector(".leftonly").addEventListener("change", function (e) { leftOnly = e.target.checked; draw(); });
    pick.addEventListener("change", function () { who = pick.value; draw(); });
    draw();
  })();

  /* ================= 04. head to head: rank dumbbells ================= */
  (function () {
    var host = document.getElementById("rankLab"); if (!host) return;
    var GROUPS = [["IN THE AIR", ["h", "aer90", "aerpct"]], ["PACE", ["ts", "spr90"]], ["DEFENDING", ["padj", "dp90", "rec90", "clr90"]], ["ON THE BALL", ["pas90", "paspct", "lb90"]]];
    var showMag = false, showLis = false;
    function draw() {
      var W = 1000, x0 = 360, x1 = 960, rowH = 46, y = 40;
      var rows = GROUPS.reduce(function (n, g) { return n + g[1].length; }, 0);
      var H = 40 + rows * rowH + GROUPS.length * 44 + 30;
      var X = function (rk) { return x0 + (x1 - x0) * (51 - rk) / 50; };
      var s = svgRoot(host.querySelector(".chart"), W, H, "Ranks among 51 Premier League centre-backs");
      el("text", { x: x0, y: 18, class: "tick" }, s, "51st");
      el("text", { x: x1, y: 18, class: "tick", "text-anchor": "end" }, s, "1st of 51 →");
      el("line", { x1: (x0 + x1) / 2, x2: (x0 + x1) / 2, y1: 26, y2: H - 20, stroke: C.soft, "stroke-dasharray": "4 6" }, s);
      el("text", { x: (x0 + x1) / 2, y: 18, class: "tick", "text-anchor": "middle" }, s, "middle");
      var who = [BRA, BAS].concat(showMag ? [MAG] : []).concat(showLis ? [LIS] : []);
      var i = 0;
      GROUPS.forEach(function (g) {
        y += 34; el("text", { x: 0, y: y, class: "grp-t" }, s, g[0]); y += 10;
        g[1].forEach(function (k) {
          var cy = y + rowH / 2;
          el("text", { x: 0, y: cy + 5, class: "tick", style: "fill:" + C.ink }, s, M[k].l);
          el("line", { x1: x0, x2: x1, y1: cy, y2: cy, stroke: C.ink, "stroke-opacity": .25, "stroke-width": 2 }, s);
          var rb = rank(k, BRA), rs = rank(k, BAS);
          el("line", { x1: X(rb), x2: X(rs), y1: cy, y2: cy, stroke: C.ink, "stroke-width": 4, class: "dd" }, s).style.transitionDelay = (i * 60) + "ms";
          who.slice().reverse().forEach(function (n) {
            var r = CB.filter(function (q) { return q.name === n; })[0], rk = rank(k, n), st = STYLE[n];
            var c = el("circle", { cx: X(rk), cy: cy, r: st.r, fill: st.fill, stroke: st.stroke, "stroke-width": 3, class: "dd" }, s);
            c.style.transitionDelay = (i * 60) + "ms";
            bindTip(c, SHORT[n] + ": " + M[k].l + "\n" + fmt(k, r[k]) + " · " + ord(rk) + " of 51" + (M[k].low ? " (fewer is better)" : ""));
          });
          [[BRA, rb, -16], [BAS, rs, 26]].forEach(function (q) {
            el("text", { x: X(q[1]), y: cy + q[2], class: "lab" + (q[0] === BRA ? " s" : ""), "text-anchor": "middle", style: "font-size:11px" }, s, ord(q[1]));
          });
          y += rowH; i++;
        });
      });
      var lx = 0, ly = H - 4;
      who.forEach(function (n) {
        var st = STYLE[n]; el("circle", { cx: lx + 8, cy: ly - 5, r: 7, fill: st.fill, stroke: st.stroke, "stroke-width": 2.5 }, s);
        el("text", { x: lx + 22, y: ly, class: "lab" }, s, SHORT[n]); lx += 40 + SHORT[n].length * 9.5;
      });
    }
    host.querySelector(".mag").addEventListener("change", function (e) { showMag = e.target.checked; draw(); });
    host.querySelector(".lis").addEventListener("change", function (e) { showLis = e.target.checked; draw(); });
    draw();
  })();

  /* ================= 07. minutes ================= */
  (function () {
    var host = document.getElementById("minsBars"); if (!host) return;
    var SE = ["23/24", "24/25", "25/26", "26/27 so far"];
    var W = 1000, H = 560, x0 = 210, x1 = 960, vmax = 3420;
    var X = function (v) { return x0 + (x1 - x0) * v / vmax; };
    var s = svgRoot(host, W, H, "League minutes per season for Branthwaite and Bassey");
    [["bra", "BRANTHWAITE", C.sig, C.ink], ["bas", "BASSEY", C.ink, C.paper]].forEach(function (p, j) {
      var top = 30 + j * 270;
      el("text", { x: 0, y: top, class: "axl" }, s, p[1]);
      D.mins[p[0]].forEach(function (m, i) {
        var y = top + 18 + i * 56;
        el("text", { x: x0 - 14, y: y + 30, class: "tick", "text-anchor": "end" }, s, SE[i]);
        var r = el("rect", { x: x0, y: y, width: X(m) - x0, height: 44, fill: p[2], class: "hbar" }, s);
        r.style.transitionDelay = (j * 300 + i * 90) + "ms";
        el("text", { x: X(m) - 12, y: y + 29, class: "lab", "text-anchor": "end", style: "fill:" + p[3] }, s, comma(m));
        bindTip(r, p[1] + ", " + SE[i] + "\n" + comma(m) + " league minutes");
      });
      el("line", { x1: X(3420), x2: X(3420), y1: top + 10, y2: top + 250, stroke: C.soft, "stroke-dasharray": "4 5" }, s);
    });
    el("text", { x: X(3420), y: H - 6, class: "tick", "text-anchor": "end" }, s, "38 × 90 = 3,420");
  })();

  /* ---------- reveals + count-up ---------- */
  function countUp(node) {
    var to = +node.dataset.count, t0 = null;
    if (RM) { node.textContent = comma(to); return; }
    function f(ts) { if (!t0) t0 = ts; var q = Math.min(1, (ts - t0) / 900); node.textContent = comma(Math.round(to * (1 - Math.pow(1 - q, 3)))); if (q < 1) requestAnimationFrame(f); }
    requestAnimationFrame(f);
  }
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      io.unobserve(e.target); e.target.classList.add("in");
      if (e.target.matches(".score")) e.target.querySelectorAll("[data-count]").forEach(countUp);
    });
  }, { threshold: 0.25 });
  document.querySelectorAll(".score, .grow").forEach(function (n) { io.observe(n); });
})();
