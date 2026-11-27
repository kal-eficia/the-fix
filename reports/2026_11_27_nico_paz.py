"""Why Nico Paz is him: a transfer-watch deep dive (27 Nov 2026).
Charts are pre-rendered SVGs in reports/nico_paz/ (built from FotMob data with a local script that is not in the repo)."""
from pathlib import Path

PAPER, SHADE, INK, SOFT, SIGNAL = "#E8E4DA", "#DCD7CB", "#121212", "#6E6A62", "#FF5A1F"
CLUB = "#C8102E"
SVG = Path(__file__).resolve().parent / "nico_paz"

META = {
    "slug": "nico-paz",
    "date": "2026-11-27",
    "date_label": "27 Nov 2026",
    "fixture": "Transfer watch · Nico Paz",
    "club": CLUB,
    "share_image": "share.jpg",
    "title": "Why Nico Paz is him",
    "summary": "United want an option if Bruno goes. Two seasons of data on Como's 22-year-old 10: he takes men on, puts a tackle in, and nobody in his position in Serie A tackles more.",
}


def svg(name):
    return (SVG / name).read_text(encoding="utf-8")


EXTRA_CSS = f"""<style>
.two{{display:grid;grid-template-columns:1fr 1fr;gap:clamp(16px,3vw,40px);margin:30px 0 10px}}
.two svg{{width:100%;height:auto;display:block}}
@media (max-width:700px){{.two{{grid-template-columns:1fr}}}}
.quote{{border-left:8px solid var(--signal);padding:4px 0 4px 24px;margin:34px 0}}
.quote q{{display:block;font:italic 400 clamp(40px,6vw,78px)/1.02 var(--serif);quotes:"\\201C" "\\201D"}}
.quote p{{margin:12px 0 0;color:var(--soft)}}
.quote .label{{display:block;margin-top:8px}}
.tiles{{display:grid;grid-template-columns:repeat(10,1fr);gap:6px;margin:30px 0 12px}}
.tiles div{{background:var(--ink);color:var(--paper);padding:10px 6px 8px;text-align:center}}
.tiles div:first-child{{background:var(--signal);color:var(--ink)}}
.tiles span{{display:block;font:600 11px/1.2 var(--mono);letter-spacing:.08em}}
.tiles b{{display:block;font:900 clamp(22px,3.6vw,44px)/1 var(--head);font-variation-settings:"wdth" 100;margin-top:22px}}
@media (max-width:600px){{.tiles{{grid-template-columns:repeat(5,1fr)}}}}
.verdict{{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:3px solid var(--ink);margin:26px 0}}
.verdict div{{padding:16px 16px 6px 0}}.verdict div+div{{padding-left:16px;border-left:1px solid var(--ink)}}
.verdict b{{display:block;font:900 22px/1.05 var(--head);font-variation-settings:"wdth" 112;text-transform:uppercase}}
@media (max-width:700px){{.verdict{{grid-template-columns:1fr}}.verdict div+div{{padding-left:0;border-left:none;border-top:1px solid var(--ink)}}}}
.lab .ctrl,.ctrl{{display:flex;flex-wrap:wrap;gap:12px 22px;align-items:center;margin:18px 0 8px;font:600 12px/1.2 var(--mono);letter-spacing:.1em;text-transform:uppercase}}
.ctrl select{{font:600 13px var(--mono);background:var(--paper);color:var(--ink);border:2px solid var(--ink);padding:6px 8px;margin-left:6px}}
.ctrl .rng{{display:flex;align-items:center;gap:8px}}.ctrl input[type=range]{{accent-color:var(--signal);width:170px}}
.ctrl output{{min-width:120px;color:var(--signal)}}
.lab .count{{color:var(--soft);margin:6px 0 0}}
.lab .chart svg,.maps svg{{width:100%;height:auto;display:block}}
.maps{{max-width:640px;margin:10px auto 0}}
.btns .grp{{display:inline-flex;border:2px solid var(--ink)}}.btns button{{font:600 12px var(--mono);letter-spacing:.08em;text-transform:uppercase;background:var(--paper);color:var(--ink);border:0;padding:9px 12px;cursor:pointer}}
.btns button+button{{border-left:2px solid var(--ink)}}.btns button[aria-pressed=true]{{background:var(--ink);color:var(--paper)}}
.btn{{font:600 12px var(--mono);letter-spacing:.1em;text-transform:uppercase;background:var(--ink);color:var(--paper);border:0;padding:10px 14px;margin:12px 0 0;cursor:pointer}}
.pt{{transition:transform .7s cubic-bezier(.2,.8,.2,1),opacity .4s}}.pt.off{{opacity:.06;pointer-events:none}}
.pt .nmlab{{font:500 13px var(--mono);fill:var(--soft);opacity:0;transition:opacity .3s}}.pt.cmp .nmlab{{opacity:1;fill:var(--ink);font-weight:800}}
.pt.cmp circle{{fill:var(--ink);fill-opacity:1}}
.pazlab{{font:900 34px var(--head);font-variation-settings:"wdth" 110;fill:var(--ink)}}
.tick{{font:13px var(--mono);fill:var(--soft)}}.axl{{font:700 14px var(--mono);letter-spacing:.14em;fill:var(--ink)}}.ql{{font:700 13px var(--mono);letter-spacing:.12em;fill:var(--signal)}}
.shot{{transition:opacity .3s}}.shot.off{{opacity:.07}}
.strips .sd.cmp{{fill:var(--ink);r:10px}}.cmplab{{font:800 13px var(--mono);fill:var(--ink)}}
.js .touch .td{{transform-box:fill-box;transform-origin:center;transform:scale(0);transition:transform .6s cubic-bezier(.2,.8,.2,1);transition-delay:calc((1 - var(--z)) * 1100ms)}}
.js .touch.in .td{{transform:scale(1)}}
.js .strips .sd{{opacity:0;transform:translateY(-24px);transition:opacity .4s,transform .5s cubic-bezier(.2,1.4,.4,1);transition-delay:calc(var(--i) * 28ms)}}
.js .strips.in .sd{{opacity:1;transform:none}}
.js .strips .sp{{transform-box:fill-box;transform-origin:center;transform:scale(0);transition:transform .5s cubic-bezier(.2,1.6,.4,1) .9s}}.js .strips.in .sp{{transform:scale(1)}}
@media (prefers-reduced-motion:reduce){{.touch .td,.strips .sd,.strips .sp{{transform:none;opacity:1;transition:none}}.pt{{transition:none}}}}
.hero-grid{{display:grid;grid-template-columns:1.15fr .85fr;gap:clamp(16px,3vw,40px);align-items:center}}
.hero-img{{width:100%;height:auto;display:block;mix-blend-mode:multiply}}
@media (max-width:760px){{.hero-grid{{grid-template-columns:1fr}}.hero-img{{max-width:420px;margin:0 auto;order:-1}}}}
.tape{{margin-top:clamp(28px,4vw,48px)}}
.js .tape .draw{{stroke-dasharray:1 1;stroke-dashoffset:1;transition:stroke-dashoffset 1.6s cubic-bezier(.4,0,.2,1)}}
.js .tape .d2{{transition-delay:1.3s;transition-duration:.6s}}
.js .tape .head,.js .tape .endball{{opacity:0;transition:opacity .3s 1.5s}}
.js .tape .step{{opacity:0;transform:translateY(10px);transition:opacity .5s,transform .5s;transition-delay:calc(var(--i)*.45s)}}
.js .tape.on .draw{{stroke-dashoffset:0}}.js .tape.on .head,.js .tape.on .endball,.js .tape.on .step{{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){{.js .tape .draw{{stroke-dashoffset:0;transition:none}}.js .tape .head,.js .tape .endball,.js .tape .step{{opacity:1;transform:none;transition:none}}}}
#tip{{position:fixed;z-index:60;pointer-events:none;background:var(--ink);color:var(--paper);font:600 13px/1.35 var(--mono);padding:8px 10px;max-width:260px;opacity:0;transition:opacity .12s}}
#tip.on{{opacity:1}}
svg .tip,svg circle:has(title),svg g:has(title){{cursor:pointer}}
</style>"""


def body():
    return EXTRA_CSS + f"""
<div class="strip"><div class="wrap label"><span>Transfer watch</span><span>Nico Paz · Como · 22</span><span>Serie A</span><span><b>On United's list if Bruno goes</b></span></div></div>
<section class="hero"><div class="wrap">
<div class="hero-grid"><div>
<p class="kick label"><i>The Fix</i> Deep dive</p>
<h1 class="head">Why Nico Paz is him</h1>
<p class="human">A lovely left foot, a 10 who'll put a tackle in, and on United's list if Bruno goes. Two seasons of his numbers, checked against every attacking midfielder in Serie A.</p>
</div><img class="hero-img" src="paz.jpg" width="900" height="1004" alt="Nico Paz, printed in halftone"></div>
<div class="score">
<div><span class="big"><em>1st</em><small>/22</small></span><p>Tackles per 90 among Serie A attacking midfielders, 2025/26</p></div>
<div><span class="big">3rd<small>/22</small></span><p>Dribbles per 90 among the same 22 players</p></div>
<div><span class="big"><span data-count="12">12</span><small>+</small><span data-count="6">6</span></span><p>Serie A goals and assists in 2025/26, as Como finished fourth</p></div>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">01</span><h2 class="head">The short version</h2></div>
<p>United have taken up the extra year on Bruno Fernandes's contract, so if he goes next summer there's a fee, and The Athletic reports Paz is on the list of options. This piece isn't Bruno against Paz. It's about whether Paz is the real thing on his own terms, and two seasons of data say he is.</p>
<div class="verdict">
<div><b>He lives in the pocket</b><p>Right of centre, just inside their half, where he can open up on his left foot. Same spot both seasons.</p></div>
<div><b>He does both jobs</b><p>Takes men on like a winger, tackles like a holding midfielder. Nobody in his position in Serie A combines the two over a full season.</p></div>
<div><b>The edges are raw</b><p>Too many shots from range and he doesn't win it high. Both are the stuff a 22-year-old works on.</p></div>
</div>
<p class="note">Every claim below is either a two-season trait (2025/26: 2,882 league minutes; 2026/27: 857 so far) or is labelled as a single-season number.</p>
</div></div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">02</span><h2 class="head">Where he lives</h2></div>
<p>Fàbregas calls him "an 8 or a 10", and in practice he roams. But the touch maps show a clear home: he drifts into the pocket right of centre, just inside the opposition half. Left-footed and on his inverted side, once he turns he's facing the whole pitch with every option open. He also drops into his own half to collect when Como are building.</p></div>
<div class="two touch">{svg("touch-2526.svg")}{svg("touch-2627.svg")}</div>
<p class="fig-sub">Dot size = how often he's on the ball there. Black = his busiest zones. Ringed: his pocket.</p>
<figcaption>Drawn from FotMob heatmap data (touch locations), Serie A 2025/26 (2,416 touches) and 2026/27 to 27 Nov (843 touches). Como attack upwards.</figcaption>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">03</span><h2 class="head">You know it's coming</h2></div>
<p>His move: pick it up in that pocket on the right, shift it inside onto the left foot, and either bend it towards the far post or slip it through for a runner. Everyone in the ground knows it's coming.</p></div>
<figure><p class="fig-title">All 5 of his goals from outside the box last season came from within 10 metres of the middle, where the cut inside takes him</p>
<p class="fig-sub">Board: an illustration of the typical pattern. Black squares: his real 2025/26 Serie A goals from outside the box (hover or tap for detail).</p>
{svg("board.svg")}
<button id="replay" class="btn" type="button">Replay the move</button>
<figcaption>Goal locations: FotMob shot data, Serie A 2025/26. The arrows are an illustration drawn from his touch and shot maps, not tracking data of a single goal.</figcaption></figure>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">04</span><h2 class="head">What the tape shows</h2></div>
<p>Numbers tell you how often. Tape tells you how. We went through his first half against United (Champions League, 21 Oct 2026) frame by frame, and two moments say a lot about him.</p></div>
<figure class="tape"><p class="fig-title">19': United lose it at his end. Eleven seconds later he's past halfway</p>
<p class="fig-sub">United's attack breaks down on the edge of Como's box. Paz picks up the loose ball on the right and just goes, pushing it with his left, with a United player chasing all the way and never getting in front. About 40 metres, and Como go from defending to attacking.</p>
{svg("tape-carry.svg")}
<p class="note">He doesn't beat a man here, so it won't show up as a dribble. No public stat counts a carry like this, which is exactly why you watch the tape.</p></figure>
<figure class="tape"><p class="fig-title">39': Cunha gets tight. Cunha ends up on the floor</p>
<p class="fig-sub">On the corner of United's box with Cunha on his back. Low, arm out, body between man and ball, and he rolls him. Cunha goes down, Paz plays on, and Bruno has to come across.</p>
{svg("tape-duel.svg")}
<p class="note">This is the strength the duel numbers hint at but can't prove, because "duels won" counts tackles and dribbles too.</p>
<figcaption>Both boards are drawn from the broadcast of Como v United, Champions League, 21 Oct 2026, first half. Times are the match clock. Positions are approximate: a board of what the camera shows, not tracking data. Two moments from one half aren't a pattern on their own; they're here because they match what two seasons of numbers say he does.</figcaption></figure>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">05</span><h2 class="head">He does both jobs</h2></div>
<p>This is the one that makes him different. Most 10s either beat a man or win the ball. Paz does both, and he did it over a full season.</p></div>
<figure><p class="fig-title">Every Serie A attacking midfielder, 2025/26</p>
<p class="fig-sub">Play with it. Drag the minutes slider to 1,000 and watch who's left in the corner. Swap what's on each axis, or pick a player to compare. Bigger dot = more minutes.</p>
<div id="scatterLab" class="lab">
<div class="ctrl">
<label>Across <select name="x"><option value="t" selected>Tackles</option><option value="d">Dribbles</option><option value="f">Won in final third</option></select></label>
<label>Up <select name="y"><option value="t">Tackles</option><option value="d" selected>Dribbles</option><option value="f">Won in final third</option></select></label>
<label class="rng">Minutes played <input type="range" name="min" min="0" max="2800" step="100" value="0"><output class="mins">everyone</output></label>
<label>Compare with <select class="compare"><option value="">nobody</option></select></label>
</div>
<p class="count label"></p>
<div class="chart"></div>
<noscript>{svg("scatter.svg")}</noscript>
</div>
<figcaption>FotMob league stats, Serie A 2025/26, filtered to attacking midfielders (22 players). Minutes are approximate: total tackles divided by tackles per 90. Shaded area: above the middle of the 22 on both measures.</figcaption></figure>
<div class="col"><ul>
<li><b>Only Messias sits near him</b>, and he did it in roughly 670 minutes against Paz's 2,882. Miretti matches his tackling in about 610 minutes but takes nobody on.</li>
<li><b>It has held up this season:</b> 2.73 tackles and 2.10 dribbles per 90 in 2026/27, against 2.84 and 2.15 last season. That's a trait, not a hot streak.</li>
<li><b>Possession makes the tackling stand out more.</b> Como have more of the ball than almost anyone in Serie A, so their players get fewer chances to defend. Adjusting for that would push his number up, not down.</li>
</ul></div>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">06</span><h2 class="head">Where he ranks</h2></div>
<p>Each line below is all 22 Serie A attacking midfielders last season. Elite at two things, middle of the pack at one, and we'll say so.</p></div>
<div class="ctrl"><label>Compare with <select class="compare"><option value="">nobody</option></select></label></div>
<figure class="strips">{svg("strips.svg")}
<figcaption>FotMob league stats, Serie A 2025/26, attacking midfielders. Grey dots: the other 21 (hover or tap for names). Stacked dots share a value.</figcaption></figure>
<div class="col"><div class="scroll"><table>
<thead><tr><th>Tackles per 90, attacking midfielders</th><th>Per 90</th><th>Total</th></tr></thead><tbody>
<tr><td><b>Nico Paz</b></td><td class="n us">2.8</td><td class="n us">91</td></tr>
<tr><td>Fabio Miretti</td><td class="n">2.8</td><td class="n">19</td></tr>
<tr><td>Junior Messias</td><td class="n">2.7</td><td class="n">20</td></tr>
<tr><td>Mattéo Tramoni</td><td class="n">1.8</td><td class="n">32</td></tr>
<tr><td>Lassana Coulibaly</td><td class="n">1.6</td><td class="n">48</td></tr>
<tr><td>Middle of the 22</td><td class="n">1.1</td><td class="n">-</td></tr>
</tbody></table></div>
<p class="note">Across every position in Serie A last season he was 13th of 324 for tackles per 90, ahead of most midfielders and full-backs.</p></div>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">07</span><h2 class="head">How he shoots</h2></div>
<p>He shoots on sight. A lot of it is from range, and that drags his chance quality down, but when he hits the target he hits it clean. His shots on target were worth more than the chances they came from in both seasons, and his free kicks are a weapon.</p></div>
<div id="shotLab" class="lab">
<div class="ctrl btns">
<span class="grp"><button type="button" data-season="2526">2025/26</button><button type="button" data-season="2627">2026/27</button></span>
<span class="grp"><button type="button" data-f="all">All</button><button type="button" data-f="goal">Goals</button><button type="button" data-f="in">Inside the box</button><button type="button" data-f="out">Outside the box</button><button type="button" data-f="fk">Free kicks</button></span>
</div>
<p class="count label"></p>
<div class="maps"><div data-season="2526">{svg("shots-2526.svg")}</div><div data-season="2627" hidden>{svg("shots-2627.svg")}</div></div>
</div>
<p class="fig-sub">Circle size = chance quality (xG). Orange = goal. Penalties left off. Hover or tap any shot.</p>
<div class="col"><div class="scroll"><table>
<thead><tr><th>Serie A</th><th>2025/26</th><th>2026/27</th></tr></thead><tbody>
<tr><td>Shots</td><td class="n">121</td><td class="n">48</td></tr>
<tr><td>From outside the box</td><td class="n">72 (60%)</td><td class="n">23 (48%)</td></tr>
<tr><td>Non-penalty xG per shot</td><td class="n">0.06</td><td class="n">0.07</td></tr>
<tr><td>xG (chance quality)</td><td class="n">8.48</td><td class="n">3.12</td></tr>
<tr><td>xGOT (strike quality, shots on target)</td><td class="n us">11.51</td><td class="n us">4.11</td></tr>
<tr><td>Goals</td><td class="n">12</td><td class="n">3</td></tr>
<tr><td>Shots from direct free kicks</td><td class="n">12</td><td class="n">3</td></tr>
</tbody></table></div>
<ul>
<li><b>Shot choice is moving the right way:</b> from 60% outside the box last season to under half this season.</li>
<li><b>Don't read too much into 12 goals from 6.9 non-penalty xG.</b> Finishing above xG rarely repeats year to year. The repeatable part is the striking: xGOT above xG in both seasons.</li>
<li><b>Free kicks are worked on.</b> Fàbregas has talked about him practising them rep after rep after training.</li>
</ul></div>
<figcaption>FotMob shot data, Serie A. xG includes two penalties in 2025/26. xGOT only counts shots on target.</figcaption>
</div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">08</span><h2 class="head">What his manager says</h2></div>
<p>Fàbregas built Como's attack around him, and you can hear it in how he talks about him.</p>
<div class="quote"><q>He's our brand.</q><p>On why Como wanted to keep him for many years.</p><span class="label">Fàbregas, press conference, January 2025, <a href="https://prod.beinsports.com/en-us/soccer/serie-a/articles-video/f%C3%A0bregas-secures-nico-paz-s-future-except-for-real-madrid-2025-01-18">via beIN Sports</a></span></div>
<div class="quote"><q>He trusts me and I trust him.</q><p>After the season that took Como into the Champions League.</p><span class="label">Fàbregas, May 2026, <a href="https://www.tuttomercatoweb.com/serie-a/fabregas-sul-suo-futuro-a-volte-si-parla-troppo-nico-paz-mi-fido-di-lui-e-lui-si-fida-di-me-2239893">via TuttoMercatoWeb</a></span></div>
<p>He has also said Como wouldn't sell him for 40 or 50 million, with only Real Madrid's buy-back able to take him, and he has <a href="https://www.90min.com/fr/real-madrid-cesc-fabregas-compare-lionel-messi-a-nico-paz-et-lui-donne-des-conseils-30-10-2025">compared him with Messi</a>.</p>
</div></div></section>

<section class="part fixpanel"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">09</span><h2 class="head">What's still raw</h2><span class="label">The honest bit</span></div>
<p class="human">Nobody's the finished article at 22. These are the parts to watch.</p>
<ul>
<li><b>Shot choice.</b> 60% of last season's shots came from outside the box at about 0.06 xG each. It's improving, but it's the clearest thing to coach.</li>
<li><b>He doesn't win it high.</b> He was 10th of 22 attacking midfielders for winning the ball in the final third (0.8 per 90, both seasons). He tracks back and nicks it deeper rather than pressing from the front.</li>
<li><b>The final ball is good, not elite.</b> 13 big chances created last season is a strong number, but FotMob's traits put him in the bottom half (36th percentile) for chances created among Serie A attacking midfielders and wingers this season.</li>
<li><b>Serie A is not the Premier League.</b> Numbers usually come down a little after a move to a tougher, faster league, and this season's sample is only about ten games.</li>
<li><b>The price and the paperwork.</b> Real Madrid hold a buy-back option for 2027/28 (reported at around 80 million euros), so any deal goes through them as well as Como.</li>
</ul>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">10</span><h2 class="head">A 10 for a decade</h2></div>
<p>He's 22, already a starter in a Champions League side (33 league starts last season), and the bits he's elite at have held for two seasons. Get him in now and that's your 10 for the best part of ten years.</p>
<div class="tiles">{"".join(f"<div><span>{27 + k}/{28 + k}</span><b>{22 + k}</b></div>" for k in range(10))}</div>
<p class="note">His age at the start of each season.</p>
<p class="human">Is he the one to follow Bruno? Or is he one season too early?</p>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">11</span><h2 class="head">Method and sources</h2></div>
<ul>
<li><b>Player data:</b> <a href="https://www.fotmob.com/players/1347574/nico-paz">FotMob</a> season pages for Serie A 2025/26 and 2026/27 (to 27 Nov): touches, shots, xG, xGOT, tackles, dribbles, recoveries. Touch and shot maps are drawn from FotMob's location data.</li>
<li><b>Positional comparison:</b> FotMob league stats for Serie A 2025/26 filtered to attacking midfielders (22 qualifying players): <a href="https://www.fotmob.com/leagues/55/stats/season/27044/players/total_tackle/serie?position=attackingMidfielder">tackles</a>, <a href="https://www.fotmob.com/leagues/55/stats/season/27044/players/won_contest/serie?position=attackingMidfielder">dribbles</a>, <a href="https://www.fotmob.com/leagues/55/stats/season/27044/players/poss_won_att_3rd/serie?position=attackingMidfielder">ball won in the final third</a>.</li>
<li><b>The two-season rule:</b> something only counts as a trait if it shows up at the same level in both seasons. Ten-game swings (his box touches doubled this season) are treated as noise.</li>
<li><b>Same league, same position:</b> percentiles and rankings only compare Paz with Serie A attacking midfielders. We don't line up Serie A numbers against Premier League ones.</li>
<li><b>What the stats count:</b> "duels won" is left out because it double-counts tackles and dribbles. Tackle counts depend on how often a team is without the ball, so possession is discussed alongside them.</li>
<li><b>Role and style:</b> <a href="https://www.hudl.com/blog/nico-paz-como-statsbomb">Hudl StatsBomb on his inverted role</a>; <a href="https://tacticalfootballanalysis.com/como-2026-2027-cesc-fabregas-tactical-data-analysis-tactics/">Como's 2026/27 shape</a>.</li>
<li><b>News:</b> Bruno's contract option and United's interest in Paz as reported by The Athletic, 27 Nov 2026. Real Madrid's buy-back: club statement, June 2026; price as reported.</li>
<li><b>Video:</b> the broadcast first half of Como v United (21 Oct 2026), cut to his involvements, checked frame by frame against the match clock. Paz identified by his number and, where shown, the name on his shirt.</li>
<li><b>What we didn't have:</b> full-match video, tracking data and possession-value models (OBV, xT). The "You know it's coming" board is an illustration of a pattern seen in his maps, not a reconstruction of one goal.</li>
</ul>
</div></div></section>
<div id="tip" role="status" aria-live="polite"></div>
<script src="app.js" defer></script>
"""
