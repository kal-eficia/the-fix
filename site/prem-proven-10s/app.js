/* The Fix: Prem Proven 10s. Every chart is drawn here from the JSON in #p10data.
   No libraries. Hover or tap any mark for detail. Respects prefers-reduced-motion. */
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var RM = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var NS = "http://www.w3.org/2000/svg";
  var C = { paper: "#E8E4DA", shade: "#DCD7CB", ink: "#121212", soft: "#6E6A62", sig: "#FF5A1F", grey: "#9a958b" };
  var D = JSON.parse(document.getElementById("p10data").textContent);
  // ams rows: name, season, team, min, npxg90, xa90, chances90, bcc90, tackles90, recov90, poss3_90
  var AMS = D.ams, PL = D.pl;
  var SEAS = { "2324": "2023/24", "2425": "2024/25", "2526": "2025/26", "2627": "2026/27 so far" };
  var KEY = { "Cole Palmer": "pal", "Morgan Gibbs-White": "mgw", "Bruno Fernandes": "bru" };
  var SHORT = { "Cole Palmer": "PALMER", "Morgan Gibbs-White": "GIBBS-WHITE", "Bruno Fernandes": "BRUNO" };

  function el(tag, attrs, parent, text) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    if (parent) parent.appendChild(e);
    return e;
  }
  function svgRoot(host, w, h, label) {
    host.innerHTML = "";
    return el("svg", { viewBox: "0 0 " + w + " " + h, role: "img", "aria-label": label }, host);
  }
  function median(a) { var s = a.slice().sort(function (x, y) { return x - y; }), m = s.length / 2; return s.length % 2 ? s[Math.floor(m)] : (s[m - 1] + s[m]) / 2; }
  function ord(n) { var s = ["th", "st", "nd", "rd"], v = n % 100; return n + (s[(v - 20) % 10] || s[v] || s[0]); }
  function f2(v) { return (+v).toFixed(2); }
  function comma(n) { return n.toLocaleString("en-GB"); }

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

  function group(host, sel, attr, cb) {
    var bs = host.querySelectorAll(sel + " button");
    bs.forEach(function (b) {
      b.addEventListener("click", function () {
        bs.forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
        cb(b.getAttribute(attr));
      });
    });
  }

  /* ================= 02. the bar is Bruno: strip ================= */
  (function () {
    var host = document.getElementById("barLab"); if (!host) return;
    var stat = 6, season = "2526";
    var LBL = { 4: "non-penalty xG per 90", 5: "xA per 90", 6: "chances created per 90", 7: "big chances created per 90" };
    function draw() {
      var rows = AMS.filter(function (r) { return r[1] === season && r[stat] != null; })
        .sort(function (a, b) { return b[stat] - a[stat]; });
      var W = 1000, H = 300, x0 = 40, x1 = 960, ly = 190;
      var vmax = Math.max.apply(null, rows.map(function (r) { return r[stat]; })) * 1.08;
      var step = vmax > 2 ? 0.5 : 0.1;
      var X = function (v) { return x0 + (x1 - x0) * v / vmax; };
      var s = svgRoot(host.querySelector(".chart"), W, H, "Strip chart of " + LBL[stat]);
      el("line", { x1: x0, x2: x1, y1: ly, y2: ly, stroke: C.ink, "stroke-width": 2 }, s);
      for (var v = 0; v <= vmax + 1e-9; v += step) {
        el("line", { x1: X(v), x2: X(v), y1: ly - 5, y2: ly + 5, stroke: C.ink, "stroke-width": 1.5 }, s);
        el("text", { x: X(v), y: ly + 26, class: "tick", "text-anchor": "middle" }, s, step < 0.5 ? v.toFixed(1) : String(+v.toFixed(1)));
      }
      el("text", { x: x0, y: 24, class: "axl" }, s, LBL[stat].toUpperCase() + " →");
      var stack = {};
      rows.forEach(function (r, i) {
        if (KEY[r[0]]) return;
        var b = Math.round(r[stat] * 50) / 50; stack[b] = (stack[b] || 0) + 1;
        var c = el("circle", { cx: X(r[stat]), cy: ly - 14 - (stack[b] - 1) * 15, r: 7, fill: C.grey, class: "pt" }, s);
        bindTip(c, r[0] + " (" + r[2] + ")\n" + f2(r[stat]) + " · " + ord(i + 1) + " of " + rows.length + "\n" + comma(r[3]) + " minutes");
      });
      var placed = [];
      rows.forEach(function (r, i) {
        var k = KEY[r[0]]; if (!k) return;
        var cx = X(r[stat]), up = k !== "pal";
        var g = el("g", {}, s);
        el("circle", { cx: cx, cy: ly - 14, r: 13, fill: k === "pal" ? C.sig : k === "mgw" ? C.ink : C.paper, stroke: C.ink, "stroke-width": 3.5 }, g);
        var lvl = 0; placed.forEach(function (p) { if (p.up === up && Math.abs(p.x - cx) < 190) lvl++; });
        placed.push({ x: cx, up: up });
        var ty = up ? ly - 46 - lvl * 22 : ly + 84 + lvl * 22;
        if (up) el("line", { x1: cx, x2: cx, y1: ly - 28, y2: ty + 6, stroke: C.ink, "stroke-width": 1 }, g);
        el("text", { x: cx, y: ty, class: "lab" + (k === "pal" ? " s" : ""), "text-anchor": cx > 820 ? "end" : cx < 120 ? "start" : "middle" }, g,
          SHORT[r[0]] + " " + f2(r[stat]) + " · " + ord(i + 1));
        bindTip(g, r[0] + " (" + r[2] + ")\n" + f2(r[stat]) + " · " + ord(i + 1) + " of " + rows.length + "\n" + comma(r[3]) + " minutes");
      });
      var have = rows.filter(function (r) { return KEY[r[0]]; }).map(function (r) { return SHORT[r[0]].toLowerCase(); });
      host.querySelector(".count").textContent = SEAS[season] + ": " + rows.length + " attacking midfielders" +
        (have.length < 3 ? ". Not in the group this season: " + ["bruno", "palmer", "gibbs-white"].filter(function (n) { return have.indexOf(n) < 0; }).join(", ") + " (under the minutes)" : "") + ".";
    }
    host.querySelector(".stat").addEventListener("change", function (e) { stat = +e.target.value; draw(); });
    group(host, ".seasons", "data-s", function (v) { season = v; draw(); });
    draw();
  })();

  /* ================= 03. both jobs: scatter ================= */
  (function () {
    var host = document.getElementById("bothLab"); if (!host) return;
    var FULL = AMS.filter(function (r) { return r[1] !== "2627"; });
    var W = 1000, H = 720, x0 = 80, x1 = 970, y0 = 30, y1 = 640, xmax = 0.45, ymax = 0.48;
    var X = function (v) { return x0 + (x1 - x0) * v / xmax; }, Y = function (v) { return y1 - (y1 - y0) * v / ymax; };
    var s = svgRoot(host.querySelector(".chart"), W, H, "Scatter of non-penalty xG per 90 against xA per 90 for 48 attacking-midfielder seasons");
    var mx = median(FULL.map(function (r) { return r[4]; })), my = median(FULL.map(function (r) { return r[5]; }));
    el("rect", { x: X(mx), y: Y(ymax), width: X(xmax) - X(mx), height: Y(my) - Y(ymax), fill: C.sig, "fill-opacity": .1 }, s);
    el("text", { x: X(xmax) - 8, y: Y(ymax) + 18, class: "ql", "text-anchor": "end" }, s, "ABOVE THE MIDDLE ON BOTH");
    for (var v = 0; v <= xmax + 1e-9; v += 0.1) { el("text", { x: X(v), y: y1 + 24, class: "tick", "text-anchor": "middle" }, s, v.toFixed(1)); }
    for (v = 0; v <= ymax + 1e-9; v += 0.1) { el("text", { x: x0 - 12, y: Y(v) + 4, class: "tick", "text-anchor": "end" }, s, v.toFixed(1)); }
    el("line", { x1: x0, x2: x1, y1: y1, y2: y1, stroke: C.ink, "stroke-width": 2 }, s);
    el("line", { x1: x0, x2: x0, y1: y0, y2: y1, stroke: C.ink, "stroke-width": 2 }, s);
    el("line", { x1: X(mx), x2: X(mx), y1: y0, y2: y1, stroke: C.soft, "stroke-dasharray": "6 6" }, s);
    el("line", { x1: x0, x2: x1, y1: Y(my), y2: Y(my), stroke: C.soft, "stroke-dasharray": "6 6" }, s);
    el("text", { x: (x0 + x1) / 2, y: y1 + 58, class: "axl", "text-anchor": "middle" }, s, "NON-PENALTY xG PER 90 (CHANCES HE GETS) →");
    el("text", { x: 18, y: (y0 + y1) / 2, class: "axl", "text-anchor": "middle", transform: "rotate(-90 18 " + (y0 + y1) / 2 + ")" }, s, "xA PER 90 (CHANCES HE MAKES) →");
    var sum = FULL.map(function (r) { return r[4] + r[5]; }).sort(function (a, b) { return b - a; });
    var gOthers = el("g", {}, s), gKey = el("g", {}, s);
    var pts = FULL.map(function (r) {
      var k = KEY[r[0]], g = el("g", { class: "pt" }, k ? gKey : gOthers);
      var c = el("circle", { cx: X(r[4]), cy: Y(r[5]), r: k ? 11 : 7, fill: k === "pal" ? C.sig : k === "mgw" ? C.ink : k === "bru" ? C.paper : C.grey,
        stroke: k ? C.ink : C.paper, "stroke-width": k ? 3 : 1.5 }, g);
      var lab = el("text", { x: X(r[4]) + 16, y: Y(r[5]) + 4, class: "lab" + (k === "pal" ? " s" : "") }, g,
        k ? SHORT[r[0]] + " " + r[1].slice(0, 2) + "/" + r[1].slice(2) : "");
      if (k === "bru" && r[1] === "2324") { lab.setAttribute("x", X(r[4]) - 16); lab.setAttribute("text-anchor", "end"); }
      if (k === "mgw" && r[1] !== "2526") { lab.setAttribute("x", X(r[4]) - 16); lab.setAttribute("text-anchor", "end"); }
      var rank = sum.indexOf(r[4] + r[5]) + 1;
      bindTip(g, r[0] + ", " + SEAS[r[1]] + " (" + r[2] + ")\nnpxG " + f2(r[4]) + " · xA " + f2(r[5]) + " per 90\n" + ord(rank) + " of 48 for the two added · " + comma(r[3]) + " min");
      return { r: r, g: g, lab: lab };
    });
    var pick = host.querySelector(".pick");
    Array.from(new Set(FULL.map(function (r) { return r[0]; }))).filter(function (n) { return !KEY[n]; }).sort().forEach(function (n) {
      var o = document.createElement("option"); o.value = n; o.textContent = n; pick.appendChild(o);
    });
    var season = "all", minM = 1350, who = "";
    function update() {
      var n = 0;
      pts.forEach(function (p) {
        var on = (season === "all" || p.r[1] === season) && p.r[3] >= minM;
        p.g.classList.toggle("off", !on); if (on) n++;
        if (!KEY[p.r[0]]) {
          var hit = who && p.r[0] === who;
          p.g.firstChild.setAttribute("fill", hit ? C.ink : C.grey); p.g.firstChild.setAttribute("r", hit ? 10 : 7);
          p.lab.textContent = hit ? p.r[0].split(" ").slice(-1)[0].toUpperCase() + " " + p.r[1].slice(0, 2) + "/" + p.r[1].slice(2) : "";
          if (hit) gKey.appendChild(p.g);
        }
      });
      var top = pts.filter(function (p) { return !p.g.classList.contains("off"); })
        .sort(function (a, b) { return (b.r[4] + b.r[5]) - (a.r[4] + a.r[5]); })[0];
      host.querySelector(".count").textContent = "Showing " + n + " of 48 seasons." + (top ? " Top for the two added: " + top.r[0] + ", " + SEAS[top.r[1]] + "." : "");
      host.querySelector("output").textContent = comma(minM);
    }
    group(host, ".seasons", "data-s", function (v) { season = v; update(); });
    host.querySelector(".mins").addEventListener("input", function (e) { minM = +e.target.value; update(); });
    pick.addEventListener("change", function () { who = pick.value; update(); });
    update();
  })();

  /* ---------- grouped bars helper ---------- */
  function bars(host, seasons, series, vmax, step, fmt, sub, label) {
    var W = 1000, H = 470, x0 = 60, x1 = 990, y0 = 50, y1 = 380;
    var Y = function (v) { return y1 - (y1 - y0) * v / vmax; };
    var s = svgRoot(host, W, H, label);
    for (var v = 0; v <= vmax + 1e-9; v += step) {
      el("line", { x1: x0, x2: x1, y1: Y(v), y2: Y(v), stroke: C.ink, "stroke-opacity": .12 }, s);
      el("text", { x: x0 - 10, y: Y(v) + 4, class: "tick", "text-anchor": "end" }, s, step < 1 ? v.toFixed(1) : String(v));
    }
    var gw = (x1 - x0) / seasons.length, bw = Math.min(70, gw / 3.2);
    seasons.forEach(function (se, i) {
      var cx = x0 + gw * (i + 0.5);
      series.forEach(function (sr, j) {
        var val = sr.get(se), bx = cx + (j - series.length / 2) * (bw + 8) + 4;
        var r = el("rect", { x: bx, y: Y(val), width: bw, height: y1 - Y(val), fill: sr.fill, stroke: sr.stroke || "none", "stroke-width": 2.5, class: "bar" }, s);
        r.style.transitionDelay = (i * 120 + j * 60) + "ms";
        el("text", { x: bx + bw / 2, y: Y(val) - 8, class: "lab", "text-anchor": "middle", style: "fill:" + (sr.text || C.ink) }, s, fmt(val));
        bindTip(r, SEAS[se] + "\n" + sr.name + ": " + fmt(val) + (sr.extra ? "\n" + sr.extra(se) : ""));
      });
      el("text", { x: cx, y: y1 + 26, class: "axl", "text-anchor": "middle" }, s, SEAS[se].replace("20", "").replace("/20", "/").toUpperCase());
      el("text", { x: cx, y: y1 + 48, class: "tick", "text-anchor": "middle" }, s, sub(se));
    });
    el("line", { x1: x0, x2: x1, y1: y1, y2: y1, stroke: C.ink, "stroke-width": 2 }, s);
    var lx = x0;
    series.forEach(function (sr) {
      el("rect", { x: lx, y: 8, width: 18, height: 18, fill: sr.fill, stroke: sr.stroke || "none", "stroke-width": 2 }, s);
      var t = el("text", { x: lx + 26, y: 22, class: "axl" }, s, sr.name.toUpperCase()); lx += 50 + sr.name.length * 10;
    });
  }
  var ALLS = ["2324", "2425", "2526", "2627"];
  var pb = document.getElementById("palBars");
  if (pb) bars(pb, ALLS, [
    { name: "Non-penalty xG", fill: "#bdb8ad", stroke: C.ink, get: function (s) { return PL["pal" + s].npxg; }, extra: function (s) { return PL["pal" + s].npshots + " non-penalty shots"; } },
    { name: "Non-penalty goals", fill: C.sig, text: C.sig, get: function (s) { return PL["pal" + s].npg; }, extra: function (s) { var p = PL["pal" + s]; return "plus " + p.pengoals + " of " + p.pen + " pens"; } }
  ], 15, 5, function (v) { return v % 1 ? v.toFixed(1) : String(v); }, function (s) { return comma(PL["pal" + s].min) + " MIN" + (s === "2324" ? " · POCH" : ""); },
  "Palmer's non-penalty xG and non-penalty goals by season");
  var mb = document.getElementById("mgwBars");
  if (mb) bars(mb, ALLS, [
    { name: "Non-penalty xG per 90", fill: C.ink, get: function (s) { var p = PL["mgw" + s]; return p.npxg / p.min * 90; }, extra: function (s) { return PL["mgw" + s].npg + " non-penalty goals from " + PL["mgw" + s].npxg + " npxG"; } },
    { name: "xA per 90", fill: C.sig, text: C.sig, get: function (s) { var p = PL["mgw" + s]; return p.xa / p.min * 90; }, extra: function (s) { return PL["mgw" + s].assists + " assists from " + PL["mgw" + s].xa + " xA"; } }
  ], 0.35, 0.1, f2, function (s) { var p = PL["mgw" + s]; return p.npg + " NP GOALS · " + p.assists + " AST"; },
  "Gibbs-White's non-penalty xG and xA per 90 by season");

  /* ================= minutes ================= */
  (function () {
    var host = document.getElementById("minsBars"); if (!host) return;
    var W = 1000, H = 560, x0 = 210, x1 = 960, vmax = 3420;
    var X = function (v) { return x0 + (x1 - x0) * v / vmax; };
    var s = svgRoot(host, W, H, "League minutes per season for Palmer and Gibbs-White");
    [["pal", "PALMER", C.sig, C.ink], ["mgw", "GIBBS-WHITE", C.ink, C.paper]].forEach(function (p, j) {
      var top = 30 + j * 270;
      el("text", { x: 0, y: top, class: "axl" }, s, p[1]);
      ALLS.forEach(function (se, i) {
        var d = PL[p[0] + se], y = top + 18 + i * 56;
        el("text", { x: x0 - 14, y: y + 30, class: "tick", "text-anchor": "end" }, s, SEAS[se].replace("20", "").replace("/20", "/"));
        var r = el("rect", { x: x0, y: y, width: X(d.min) - x0, height: 44, fill: p[2], class: "hbar" }, s);
        r.style.transitionDelay = (j * 300 + i * 90) + "ms";
        el("text", { x: X(d.min) - 12, y: y + 29, class: "lab", "text-anchor": "end", style: "fill:" + p[3] }, s, comma(d.min));
        bindTip(r, p[1] + ", " + SEAS[se] + "\n" + comma(d.min) + " league minutes\n" + d.goals + " goals, " + d.assists + " assists");
      });
      el("line", { x1: X(3420), x2: X(3420), y1: top + 10, y2: top + 250, stroke: C.soft, "stroke-dasharray": "4 5" }, s);
    });
    el("text", { x: X(3420), y: H - 6, class: "tick", "text-anchor": "end" }, s, "38 × 90 = 3,420");
  })();

  /* ================= 07. shot lab ================= */
  (function () {
    var host = document.getElementById("shotLab"); if (!host) return;
    var who = "pal", season = "2324", filt = "all";
    var W = 680, L = 40, k = W / 68, H = L * k + 40;
    function P(x, y) { return [(68 - y) * k, (105 - x) * k + 10]; }   // FotMob shot maps: x along (goal at 105), y across with y < 34 = attacker's RIGHT (Opta convention), so mirror
    function draw() {
      var d = PL[who + season], s = svgRoot(host.querySelector(".chart"), W, H, "Shot map");
      el("rect", { x: 0, y: 0, width: W, height: H, fill: C.shade }, s);
      var ln = { stroke: C.ink, "stroke-opacity": .5, "stroke-width": 2, fill: "none" };
      function rect(a, b, c, e) { var p = P(a, c), q = P(b, e); el("rect", Object.assign({ x: Math.min(p[0], q[0]), y: Math.min(p[1], q[1]), width: Math.abs(q[0] - p[0]), height: Math.abs(q[1] - p[1]) }, ln), s); }
      rect(105, 105 - L, 0, 68); rect(105, 88.5, 13.84, 54.16); rect(105, 99.5, 24.84, 43.16);
      var gp = P(105, 30.34), gq = P(105, 37.66); el("rect", Object.assign({ x: gp[0], y: gp[1] - 14, width: gq[0] - gp[0], height: 14 }, ln), s);
      var c = P(94, 34), r = 9.15 * k, by = P(88.5, 0)[1], dx = Math.sqrt(r * r - (by - c[1]) * (by - c[1]));
      el("path", Object.assign({ d: "M" + (c[0] - dx) + "," + by + " A" + r + "," + r + " 0 0 0 " + (c[0] + dx) + "," + by }, ln), s);
      var shots = d.shots.slice().sort(function (a, b) { return b[2] - a[2]; }), shown = 0, goals = 0, far = 0;
      shots.forEach(function (q) {
        if (q[0] < 105 - L + 1) { far++; return; }
        var outside = q[0] < 88.5 || q[1] < 13.84 || q[1] > 54.16;
        var on = filt === "all" || (filt === "goal" && q[3]) || (filt === "out" && outside);
        var p = P(q[0], q[1]), rr = 4 + 28 * Math.sqrt(q[2]);
        var e = el("circle", { cx: p[0], cy: p[1], r: rr, fill: q[3] ? C.sig : "none", stroke: q[3] ? C.ink : C.ink, "stroke-opacity": q[3] ? 1 : .55, "stroke-width": q[3] ? 2.5 : 2, class: "shot" + (on ? "" : " off") }, s);
        if (on) { shown++; if (q[3]) goals++; }
        var dist = Math.round(Math.hypot(105 - q[0], 34 - q[1]));
        bindTip(e, (q[3] ? "GOAL" : "No goal") + " · " + q[2].toFixed(2) + " xG\n" + dist + " m from goal" + (q[4] === "FreeKick" ? " · direct free kick" : q[4] === "SetPiece" || q[4] === "FromCorner" ? " · set piece" : ""));
      });
      var nm = who === "pal" ? "Palmer" : "Gibbs-White", tot = d.shots.length;
      var out = d.shots.filter(function (q) { return q[0] < 88.5 || q[1] < 13.84 || q[1] > 54.16; }).length;
      host.querySelector(".count").textContent = nm + ", " + SEAS[season] + ": " + tot + " non-penalty shots, " + d.npg + " goals from " + d.npxg + " xG. " +
        Math.round(100 * out / tot) + "% from outside the box." + (filt !== "all" ? " Showing " + shown + (filt === "goal" ? " goals." : " from outside the box, " + goals + " scored.") : "");
    }
    group(host, ".who", "data-p", function (v) { who = v; draw(); });
    group(host, ".seasons", "data-s", function (v) { season = v; draw(); });
    group(host, ".filt", "data-f", function (v) { filt = v; draw(); });
    draw();
  })();

  /* ---------- scroll reveals + count-up ---------- */
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
  }, { threshold: 0.3 });
  document.querySelectorAll(".score, .grow, .split").forEach(function (n) { io.observe(n); });
})();
