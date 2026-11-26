"""How Man United won the ball back at Sporting (25 Nov 2026)."""

PAPER, SHADE, INK, SOFT, SIGNAL, FIX = "#E8E4DA", "#DCD7CB", "#121212", "#6E6A62", "#FF5A1F", "#1F8A5B"
CLUB = "#C8102E"

META = {
    "slug": "sporting-press",
    "date": "2026-11-25",
    "date_label": "25 Nov 2026",
    "fixture": "Sporting 2-2 Man United",
    "club": CLUB,
    "title": "How Man United won the ball back at Sporting",
    "summary": "United won the ball higher up the pitch than in any game this season, in Pochettino's second match. Then the press stopped at 67 minutes.",
}

# Every United regain (ball recovery, interception, tackle won). x = 0 own goal line to 100 Sporting's; y = 0 to 100 across.
REGAINS = [
    ("First half", "1", "recovery", 43, 91), ("First half", "3", "recovery", 36, 22), ("First half", "4", "recovery", 20, 42),
    ("First half", "8", "recovery", 43, 36), ("First half", "10", "recovery", 33, 65), ("First half", "13", "tackle won", 32, 83),
    ("First half", "13", "recovery", 25, 87), ("First half", "15", "recovery", 56, 94), ("First half", "17", "tackle won", 52, 50),
    ("First half", "17", "tackle won", 62, 38), ("First half", "17", "recovery", 53, 45), ("First half", "19", "tackle won", 66, 38),
    ("First half", "19", "recovery", 66, 38), ("First half", "19", "tackle won", 77, 26), ("First half", "19", "recovery", 78, 26),
    ("First half", "21", "recovery", 47, 40), ("First half", "21", "interception", 54, 93), ("First half", "21", "recovery", 58, 81),
    ("First half", "24", "recovery", 32, 13), ("First half", "26", "tackle won", 22, 15), ("First half", "34", "recovery", 65, 9),
    ("First half", "34", "recovery", 48, 44), ("First half", "35", "recovery", 11, 28), ("First half", "35", "tackle won", 42, 7),
    ("First half", "36", "recovery", 11, 76), ("First half", "38", "recovery", 38, 73), ("First half", "39", "interception", 59, 66),
    ("First half", "42", "recovery", 61, 80), ("First half", "44", "interception", 37, 15), ("First half", "44", "recovery", 30, 30),
    ("First half", "45+1", "tackle won", 70, 78), ("First half", "45+1", "recovery", 76, 73), ("First half", "45+2", "interception", 61, 87),
    ("First half", "45+2", "recovery", 77, 92), ("First half", "45+2", "interception", 68, 61), ("First half", "45+2", "tackle won", 67, 51),
    ("First half", "45+2", "recovery", 65, 46),
    ("45 to 67 min", "45", "interception", 32, 42), ("45 to 67 min", "45", "recovery", 30, 31), ("45 to 67 min", "45", "recovery", 81, 89),
    ("45 to 67 min", "48", "recovery", 81, 13), ("45 to 67 min", "49", "recovery", 74, 61), ("45 to 67 min", "51", "tackle won", 79, 97),
    ("45 to 67 min", "51", "recovery", 47, 30), ("45 to 67 min", "51", "tackle won", 56, 94), ("45 to 67 min", "52", "recovery", 58, 83),
    ("45 to 67 min", "53", "recovery", 69, 15), ("45 to 67 min", "55", "interception", 75, 31), ("45 to 67 min", "56", "recovery", 53, 56),
    ("45 to 67 min", "62", "recovery", 40, 9), ("45 to 67 min", "63", "tackle won", 74, 12), ("45 to 67 min", "64", "tackle won", 72, 5),
    ("45 to 67 min", "64", "recovery", 55, 21), ("45 to 67 min", "65", "interception", 53, 3), ("45 to 67 min", "67", "interception", 67, 85),
    ("45 to 67 min", "67", "recovery", 72, 82),
    ("After 67 min", "73", "interception", 36, 3), ("After 67 min", "84", "interception", 35, 87), ("After 67 min", "89", "tackle won", 33, 38),
    ("After 67 min", "89", "recovery", 22, 51), ("After 67 min", "89", "recovery", 31, 26), ("After 67 min", "92", "recovery", 26, 3),
    ("After 67 min", "93", "recovery", 38, 77),
]

SPELLS = [("0-15", 0, 7), ("15-30", 10, 3), ("30-45+", 10, 7), ("45-60", 9, 3), ("60-75", 6, 2), ("75-90+", 0, 6)]  # (spell, Sporting half, own half)

SEASON = [  # date, opponent, coach, average regain height (0-100 of pitch length)
    ("22 Aug", "Hull", "Carrick", 39.3), ("30 Aug", "Ipswich", "Carrick", 38.9), ("6 Sep", "Everton", "Carrick", 28.1),
    ("10 Sep", "Sabah", "Carrick", 41.2), ("13 Sep", "Man City", "Carrick", 38.7), ("16 Sep", "Brighton", "Carrick", 35.6),
    ("20 Sep", "Fulham", "Carrick", 35.0), ("10 Oct", "Tottenham", "Carrick", 35.1), ("13 Oct", "Atletico", "Carrick", 42.7),
    ("18 Oct", "Leeds", "Carrick", 38.1), ("25 Oct", "Bournemouth", "Carrick", 36.1), ("31 Oct", "Chelsea", "Carrick", 32.9),
    ("3 Nov", "Roma", "Carrick", 39.4), ("8 Nov", "Aston Villa", "Carrick", 39.5), ("22 Nov", "Liverpool", "Pochettino", 28.5),
    ("25 Nov", "Sporting", "Pochettino", 51.2),
]

T = 'font-family="JetBrains Mono, monospace"'


def pitch_map():
    W, H, x0, y0 = 1000, 680, 20, 60
    L, Wd = 960, 960 * 68 / 105
    px = lambda v: x0 + v / 100 * L
    py = lambda v: y0 + Wd - v / 100 * Wd
    ln = f'stroke="{INK}" stroke-width="2" fill="none"'
    s = [f'<svg viewBox="0 0 {W} {y0 + Wd + 50:.0f}" role="img" aria-label="Map of all 63 United regains at Sporting">']
    s.append(f'<rect x="{px(60):.1f}" y="{y0}" width="{px(100) - px(60):.1f}" height="{Wd:.1f}" fill="{SHADE}"/>')
    # hatch the final 40%
    s.append(f'<defs><pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="10" stroke="{INK}" stroke-opacity=".12" stroke-width="3"/></pattern></defs>')
    s.append(f'<rect x="{px(60):.1f}" y="{y0}" width="{px(100) - px(60):.1f}" height="{Wd:.1f}" fill="url(#hatch)"/>')
    s.append(f'<rect x="{x0}" y="{y0}" width="{L}" height="{Wd:.1f}" {ln}/>')
    s.append(f'<line x1="{px(50):.1f}" x2="{px(50):.1f}" y1="{y0}" y2="{y0 + Wd:.1f}" {ln}/>')
    s.append(f'<circle cx="{px(50):.1f}" cy="{y0 + Wd / 2:.1f}" r="{9.15 / 105 * L:.1f}" {ln}/>')
    for a, b in [(0, 15.7), (84.3, 100)]:
        s.append(f'<rect x="{px(a):.1f}" y="{py(79.65):.1f}" width="{px(b) - px(a):.1f}" height="{py(20.35) - py(79.65):.1f}" {ln}/>')
    for a, b in [(0, 5.24), (94.76, 100)]:
        s.append(f'<rect x="{px(a):.1f}" y="{py(63.5):.1f}" width="{px(b) - px(a):.1f}" height="{py(36.5) - py(63.5):.1f}" {ln}/>')
    s.append(f'<text x="{px(80):.1f}" y="{y0 + Wd + 34:.1f}" text-anchor="middle" {T} font-size="15" font-weight="600" letter-spacing="2" fill="{INK}">FINAL 40% (HATCHED)</text>')
    s.append(f'<text x="{x0}" y="{y0 - 18}" {T} font-size="15" font-weight="600" letter-spacing="2" fill="{SOFT}">UNITED\'S GOAL</text>')
    s.append(f'<text x="{x0 + L}" y="{y0 - 18}" text-anchor="end" {T} font-size="15" font-weight="600" letter-spacing="2" fill="{INK}">UNITED ATTACK THIS WAY &#8594;</text>')
    for ph, mn, kind, x, y in REGAINS:
        if ph == "First half":
            mark = f'fill="{CLUB}" stroke="{INK}" stroke-width="1.5"'
        elif ph == "45 to 67 min":
            mark = f'fill="{PAPER}" stroke="{CLUB}" stroke-width="4"'
        else:
            mark = f'fill="{SOFT}" fill-opacity=".55" stroke="{INK}" stroke-width="1"'
        s.append(f'<circle cx="{px(x):.1f}" cy="{py(y):.1f}" r="10" {mark}><title>{mn} min: {kind} ({ph})</title></circle>')
    s.append("</svg>")
    return "".join(s)


def spells_chart():
    W, x0, y0, Hc = 1000, 60, 50, 300
    band = (W - x0 - 20) / len(SPELLS)
    peak = max(a + b for _, a, b in SPELLS)
    s = [f'<svg viewBox="0 0 {W} {y0 + Hc + 70}" role="img" aria-label="United regains per 15-minute spell, split by half of the pitch">']
    s.append(f'<line x1="{x0}" x2="{W - 20}" y1="{y0 + Hc}" y2="{y0 + Hc}" stroke="{INK}" stroke-width="3"/>')
    hx = x0 + band * 3
    s.append(f'<line x1="{hx:.1f}" x2="{hx:.1f}" y1="{y0 - 30}" y2="{y0 + Hc + 44}" stroke="{SIGNAL}" stroke-width="3" stroke-dasharray="8 6"/>')
    s.append(f'<text x="{hx + 10:.1f}" y="{y0 - 14}" {T} font-size="15" font-weight="600" letter-spacing="2" fill="{SIGNAL}">HALF-TIME</text>')
    bw = band * 0.58
    for i, (sp, opp, own) in enumerate(SPELLS):
        bx = x0 + i * band + (band - bw) / 2
        tot = opp + own
        h_own, h_opp = own / peak * Hc, opp / peak * Hc
        s.append(f'<rect x="{bx:.1f}" y="{y0 + Hc - h_own:.1f}" width="{bw:.1f}" height="{h_own:.1f}" fill="{SOFT}" fill-opacity=".45"><title>{sp} min, own half: {own}</title></rect>')
        if opp:
            s.append(f'<rect x="{bx:.1f}" y="{y0 + Hc - h_own - h_opp:.1f}" width="{bw:.1f}" height="{h_opp:.1f}" fill="{CLUB}"><title>{sp} min, Sporting\'s half: {opp}</title></rect>')
        s.append(f'<text x="{bx + bw / 2:.1f}" y="{y0 + Hc - h_own - h_opp - 12:.1f}" text-anchor="middle" {T} font-size="20" font-weight="700" fill="{CLUB if opp else SOFT}">{opp} of {tot}</text>')
        s.append(f'<text x="{bx + bw / 2:.1f}" y="{y0 + Hc + 30}" text-anchor="middle" {T} font-size="17" fill="{INK}">{sp}</text>')
    s.append(f'<text x="{W - 20}" y="{y0 + Hc + 58}" text-anchor="end" {T} font-size="13" letter-spacing="2" fill="{SOFT}">MINUTES</text>')
    s.append("</svg>")
    return "".join(s)


def season_chart():
    W, x0, y0, Hc, lo, hi = 1000, 70, 40, 340, 25, 60
    M = lambda v: v * 1.05  # share of pitch length to metres on a 105 m pitch
    n = len(SEASON)
    step = (W - x0 - 60) / (n - 1)
    x = lambda i: x0 + i * step
    y = lambda m: y0 + Hc - (m - lo) / (hi - lo) * Hc
    car = [h for *_, c, h in SEASON if c == "Carrick"]
    avg, best = M(sum(car) / len(car)), M(max(car))
    s = [f'<svg viewBox="0 0 {W} {y0 + Hc + 110}" role="img" aria-label="Average height of United regains in every match this season">']
    for v in (30, 40, 50, 60):
        s.append(f'<line x1="{x0}" x2="{W - 40}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="{INK}" stroke-opacity=".15"/>'
                 f'<text x="{x0 - 12}" y="{y(v) + 5:.1f}" text-anchor="end" {T} font-size="15" fill="{SOFT}">{v} m</text>')
    nc = len(car)
    s.append(f'<line x1="{x0}" x2="{x(nc - 1):.1f}" y1="{y(avg):.1f}" y2="{y(avg):.1f}" stroke="{INK}" stroke-width="2.5" stroke-dasharray="9 6"/>')
    ky = y(27.5)
    s.append(f'<line x1="{x(3):.1f}" x2="{x(3) + 36:.1f}" y1="{ky - 5:.1f}" y2="{ky - 5:.1f}" stroke="{INK}" stroke-width="2.5" stroke-dasharray="9 6"/>'
             f'<text x="{x(3) + 46:.1f}" y="{ky:.1f}" {T} font-size="15" font-weight="600" fill="{INK}">CARRICK AVERAGE {avg:.0f} M (BEST {best:.0f} M)</text>')
    dx = (x(nc - 1) + x(nc)) / 2
    s.append(f'<line x1="{dx:.1f}" x2="{dx:.1f}" y1="{y0 - 10}" y2="{y0 + Hc}" stroke="{INK}" stroke-width="2"/>'
             f'<text x="{dx - 10:.1f}" y="{y0 + 6}" text-anchor="end" {T} font-size="14" font-weight="600" letter-spacing="2" fill="{INK}">POCHETTINO &#8594;</text>')
    pts = " ".join(f"{x(i):.1f},{y(M(h)):.1f}" for i, (*_, h) in enumerate(SEASON))
    s.append(f'<polyline points="{pts}" fill="none" stroke="{SOFT}" stroke-width="2.5"/>')
    for i, (d, opp, coach, h) in enumerate(SEASON):
        hot = opp == "Sporting"
        s.append(f'<circle cx="{x(i):.1f}" cy="{y(M(h)):.1f}" r="{13 if hot else 8}" fill="{SIGNAL if hot else PAPER}" stroke="{INK}" stroke-width="{3 if hot else 2.5}"><title>{d} v {opp} ({coach}): {M(h):.0f} m</title></circle>')
        s.append(f'<text x="{x(i):.1f}" y="{y0 + Hc + 22}" text-anchor="end" transform="rotate(-45 {x(i):.1f} {y0 + Hc + 22})" {T} font-size="14" font-weight="{700 if hot else 400}" fill="{INK if hot else SOFT}">{opp}</text>')
    last, prev = SEASON[-1], SEASON[-2]
    s.append(f'<text x="{x(n - 1) - 22:.1f}" y="{y(M(last[3])) + 8:.1f}" text-anchor="end" font-family="Archivo, sans-serif" font-weight="900" font-size="34" style="font-variation-settings:\'wdth\' 125" fill="{INK}">{M(last[3]):.0f} M</text>')
    s.append(f'<text x="{x(n - 2) - 6:.1f}" y="{y(M(prev[3])) + 32:.1f}" {T} font-size="14" fill="{SOFT}">Anfield {M(prev[3]):.0f} m</text>')
    s.append("</svg>")
    return "".join(s)


def body():
    n_high = sum(1 for r in REGAINS if r[3] >= 60)
    assert len(REGAINS) == 63 and n_high == 24, (len(REGAINS), n_high)
    assert sum(a + b for _, a, b in SPELLS) == 63
    return f"""
<div class="strip"><div class="wrap label"><span>Champions League</span><span>Sporting CP 2-2 Man United</span><span>25 Nov 2026</span><span><b>Pochettino's 2nd game</b></span></div></div>
<section class="hero"><div class="wrap">
<p class="kick label"><i>The Fix</i> Match report</p>
<h1 class="head">How Man United won the ball back at Sporting</h1>
<p class="human">They won it in better places than all season. Then they stopped.</p>
<div class="score">
<div><span class="big"><em>24</em><small> v </small>5</span><p>Regains in the final 40% of the pitch, United v Sporting</p></div>
<div><span class="big">54<small> m</small></span><p>Average spot United won the ball, their highest of the season</p></div>
<div><span class="big">2<small>/24</small></span><p>High regains that led to a shot within 15 seconds</p></div>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">01</span><h2 class="head">The short version</h2></div>
<p>United won the ball back about as often as Sporting (63 times to 66), but far higher up the pitch: 24 of their regains came in the final 40% of the pitch, against Sporting's 5. They pressed hardest before half-time, won the ball highest in the 15 minutes after the break, and never won it in Sporting's half again after the 67th minute. The gap was the end product: those 24 high regains led to two shots.</p>
<div class="scroll"><table>
<thead><tr><th>Measure</th><th>United</th><th>Sporting</th></tr></thead><tbody>
<tr><td>Times they won the ball back</td><td class="n us">63</td><td class="n">66</td></tr>
<tr><td>Won in the final third</td><td class="n us">17</td><td class="n">3</td></tr>
<tr><td>Won in the final 40% of the pitch</td><td class="n us">24</td><td class="n">5</td></tr>
<tr><td>Average spot they won it (0 = own goal line, 100 = opponent's)</td><td class="n us">51</td><td class="n">32</td></tr>
<tr><td>Opponent passes allowed per challenge in their build-up (lower = harder press)</td><td class="n us">12.6</td><td class="n">14.4</td></tr>
</tbody></table></div>
<p class="note">"Won the ball back" here means a ball recovery, an interception or a tackle won, from Opta's event data (via WhoScored).</p>
</div></div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">02</span><h2 class="head">Where United won it</h2></div>
<p>United won the ball most often around halfway and in Sporting's half, and spread it evenly across the width: 23 on the right, 19 in the middle, 21 on the left. Sporting were the opposite: 37 of their 66 regains came in their own third, and only 3 in United's.</p></div>
<figure><p class="fig-title">United won it high until the 67th minute, then only in their own half</p>
<p class="fig-sub"><svg width="14" height="14" aria-hidden="true"><circle cx="7" cy="7" r="6" fill="{CLUB}"/></svg> First half (37) &nbsp; <svg width="14" height="14" aria-hidden="true"><circle cx="7" cy="7" r="5" fill="{PAPER}" stroke="{CLUB}" stroke-width="3"/></svg> 45 to 67 min (19) &nbsp; <svg width="14" height="14" aria-hidden="true"><circle cx="7" cy="7" r="6" fill="{SOFT}" fill-opacity=".55"/></svg> After 67 min (7)</p>
{pitch_map()}
<figcaption>Opta event data via WhoScored · every United ball recovery, interception and tackle won, 25 Nov 2026 · {n_high} of 63 in the final 40% (hatched)</figcaption></figure>
<div class="col"><ul>
<li><b>The front of the press won it highest.</b> Amad won it in the final 40% six times, more than anyone. Mainoo and Tielemans did it four times each, Fernandes twice.</li>
<li><b>The back line stepped in too.</b> Maguire won it high three times by stepping out on the left: twice in first-half stoppage time and once at 67 minutes.</li>
<li><b>The deep regains clustered on the flanks.</b> 20 of United's 28 own-half regains came out wide, the channels Sporting's wing-backs worked in.</li>
</ul></div>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">03</span><h2 class="head">When United won it</h2></div>
<p>The press ran from the 15th minute to roughly the 67th, in two waves either side of half-time, and then stopped.</p></div>
<figure><p class="fig-title">In Sporting's half from 15 to 75 minutes, then not at all</p>
<p class="fig-sub"><svg width="14" height="14" aria-hidden="true"><rect width="14" height="14" fill="{CLUB}"/></svg> Won in Sporting's half &nbsp; <svg width="14" height="14" aria-hidden="true"><rect width="14" height="14" fill="{SOFT}" fill-opacity=".45"/></svg> Won in own half</p>
{spells_chart()}
<figcaption>Opta event data via WhoScored · United regains by 15-minute spell, split at halfway · first-half stoppage time counted in 30-45+</figcaption></figure>
<div class="col"><ul>
<li><b>First half: the hardest press.</b> Sporting managed about 10 passes in their own build-up for every United challenge, against about 16 after the break. United also had far more of the ball up the pitch: 141 passes in Sporting's half before the break, 71 after it (<a href="https://www.fotmob.com/matches/sporting-cp-vs-manchester-united/3bf4ni">FotMob</a>).</li>
<li><b>45 to 67 minutes: the highest regains.</b> Sporting had more of the ball now, so United pressed in bursts rather than all the time, and those bursts won it close to goal. Mainoo won it three times between the 51st and 55th minutes, and the two goals came in this spell (48th and 50th minutes).</li>
<li><b>After 67 minutes: nothing high.</b> Mazraoui and Zirkzee had gone off at 64 to 65 minutes. United's last seven regains all came in their own half, Sporting's passes in United's half rose from 58 before the break to 109 after it, and the equaliser came at 80 minutes.</li>
</ul></div>
</div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">04</span><h2 class="head">How United won it</h2></div>
<p>United went after Sporting's back three and wing-backs. Both central midfielders pushed into Sporting's half, and the back line held high behind them. Of the 24 times United won the ball in the final 40% of the pitch, 18 came straight off a Sporting centre-back or wing-back.</p>
<ul>
<li><b>The wide players pressed the wing-backs.</b> Amad made 14 defensive actions before the 64th minute, more than anyone, at an average spot inside Sporting's half on the right. Mbeumo did the same job on the left. Between them, Sporting's two wing-backs lost the ball to a high United regain 11 times.</li>
<li><b>The midfield pair pushed up.</b> Mainoo and Tielemans made their defensive actions, on average, further forward than Fernandes. That shows they stepped onto Sporting's midfielders rather than sitting in front of the back four.</li>
<li><b>They won it by tackling, not by waiting.</b> A third of the high regains (8 of 24) were tackles won, against a fifth of all regains. When United got close, they took the ball off a player rather than collecting a loose pass.</li>
<li><b>It came from organised pressing more than scrambling.</b> Only 23 of the 63 regains (37%) came within five seconds of United losing the ball. That matches Chelsea away as the lowest share of the season, so most regains came from a set press on Sporting's build-up rather than a reaction to losing possession.</li>
<li><b>The back line squeezed up.</b> Maguire and Mazraoui made their defensive actions, on average, about 45 metres from their own goal. That kept the team short, but it is also why Sporting kept trying balls in behind.</li>
</ul>
<p class="note">WhoScored lists United as a 4-2-3-1 throughout. Sporting started in a 3-1-4-2 and switched to a 3-4-2-1 at 71 minutes. The average positions above cover the first 64 minutes, before the substitutions changed the shape; the counts cover the whole match.</p>
</div></div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">05</span><h2 class="head">Why it bodes well</h2></div>
<p>Sporting was the furthest up the pitch United have won the ball all season, by a long way, and it came in Pochettino's second game. I ran every United match this season through the same measures, and the gap is too big to call an ordinary night.</p></div>
<figure><p class="fig-title">United won the ball higher at Sporting than in any game this season</p>
<p class="fig-sub">Average spot of each regain, metres from United's own goal line</p>
{season_chart()}
<figcaption>Opta event data via WhoScored · 15 United matches this season (Como away not available) plus Sporting · regains = recoveries, interceptions, tackles won</figcaption></figure>
<div class="col">
<div class="scroll"><table>
<thead><tr><th>Measure</th><th>Sporting</th><th>Carrick average (14 games)</th><th>Carrick's best</th></tr></thead><tbody>
<tr><td>Regains in the opponent's half</td><td class="n us">35</td><td class="n">19</td><td>26 (Roma, Sabah, Tottenham)</td></tr>
<tr><td>Share of regains in the opponent's half</td><td class="n us">56%</td><td class="n">27%</td><td>41% (Sabah)</td></tr>
<tr><td>Regains in the final 40%</td><td class="n us">24</td><td class="n">11</td><td>17 (Sabah)</td></tr>
<tr><td>Regains in the final third</td><td class="n us">17</td><td class="n">6</td><td>10 (Aston Villa)</td></tr>
</tbody></table></div>
<ul>
<li><b>The change was where they pressed, not how hard.</b> Sporting got about 13 passes in their build-up per United challenge. That is harder than the Carrick average of 16, but City at home (9) and Spurs at home (10) were tougher. United didn't run more; they pressed from a higher starting point. Positioning is coachable and repeatable in a way that one-off effort isn't.</li>
<li><b>It was organised.</b> Most regains came from a set press on Sporting's build-up, not from scrambling after losing the ball (see How United won it). Set pressing patterns travel from game to game.</li>
<li><b>It came fast.</b> Pochettino took over during the international break and had not finished a full week at the club when United played Sporting. A shape this clear after so few sessions suggests it was coached, not improvised.</li>
<li><b>The players for it are already there.</b> Amad, Mainoo and Tielemans won the ball high most often, and all three are first-choice players.</li>
</ul>
<p class="caveat">The honest caveat is that this is one game. Anfield, his debut, was one of United's deepest games of the season (30 metres), and Sporting's back-three build-up invites a press more than most teams do. Brentford at home (28 November) and Newcastle away (2 December) will show whether the height holds.</p>
</div></div></section>

<section class="part fixpanel"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">06</span><h2 class="head">What still needs fixing</h2><span class="label">The fix</span></div>
<p class="human">Winning the ball high only pays if something happens next, and at Sporting very little did.</p>
<ul>
<li><b>Too few shots from good regains.</b> The 24 high regains led to a shot within 15 seconds twice (8%). Under Carrick, 30 of 155 high regains did (19%), so United won the ball in better places and did less with it.</li>
<li><b>The ball went straight back.</b> After a high regain, United strung two or more passes together 10 times out of 24 and lost it again without completing a pass 11 times.</li>
<li><b>It stopped at 67 minutes.</b> No high regains after that point, while Sporting moved to a 3-4-2-1 at 71 minutes and pushed United back. The equaliser came at 80. Whether that was legs or the changes at 64 to 65 minutes, a press that lasts two-thirds of a match won't hold leads.</li>
<li><b>A slow start.</b> None of United's first seven regains came in Sporting's half; the press only switched on after 15 minutes.</li>
</ul>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">07</span><h2 class="head">Method and sources</h2></div>
<ul>
<li><b>Event data:</b> Opta's event feed for each match, read from the WhoScored match centre. A regain is a ball recovery, an interception or a tackle won. "High" means the final 40% of the pitch; positions are converted to metres on a 105 m pitch.</li>
<li><b>Passes per challenge:</b> the opponent's passes in their own 60% of the pitch divided by United's tackles, interceptions, challenges and fouls in that zone. Lower means a harder press.</li>
<li><b>Shot after a high regain:</b> a United shot within 15 seconds of the regain.</li>
<li><b>Season comparison:</b> 16 United matches in all competitions from 22 August to 25 November. Como away is missing because its page wouldn't load.</li>
<li><b>Context:</b> half-by-half passes and the line-ups from FotMob.</li>
</ul>
<p class="note">Sources: <a href="https://www.whoscored.com/matches/2029151/live/europe-champions-league-2026-2027-sporting-cp-manchester-united">WhoScored match centre, Sporting CP 2-2 Man United</a> · <a href="https://www.fotmob.com/matches/sporting-cp-vs-manchester-united/3bf4ni">FotMob match page</a> · <a href="https://www.manutd.com/en/news/mauricio-pochettinos-most-important-focus-against-sporting">manutd.com: Pochettino's "most important" focus against Sporting</a></p>
</div></div></section>
"""
