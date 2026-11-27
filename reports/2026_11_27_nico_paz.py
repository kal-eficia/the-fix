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
#tip{{position:fixed;z-index:60;pointer-events:none;background:var(--ink);color:var(--paper);font:600 13px/1.35 var(--mono);padding:8px 10px;max-width:260px;opacity:0;transition:opacity .12s}}
#tip.on{{opacity:1}}
svg .tip,svg circle:has(title),svg g:has(title){{cursor:pointer}}
</style>"""


def body():
    return EXTRA_CSS + f"""
<div class="strip"><div class="wrap label"><span>Transfer watch</span><span>Nico Paz · Como · 22</span><span>Serie A</span><span><b>On United's list if Bruno goes</b></span></div></div>
<section class="hero"><div class="wrap">
<p class="kick label"><i>The Fix</i> Deep dive</p>
<h1 class="head">Why Nico Paz is him</h1>
<p class="human">A lovely left foot, a 10 who'll put a tackle in, and on United's list if Bruno goes. Two seasons of his numbers, checked against every attacking midfielder in Serie A.</p>
<div class="score">
<div><span class="big"><em>1st</em><small>/22</small></span><p>Tackles per 90 among Serie A attacking midfielders, 2025/26</p></div>
<div><span class="big">3rd<small>/22</small></span><p>Dribbles per 90 among the same 22 players</p></div>
<div><span class="big">12<small>+</small>6</span><p>Serie A goals and assists in 2025/26, as Como finished fourth</p></div>
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
<div class="two">{svg("touch-2526.svg")}{svg("touch-2627.svg")}</div>
<p class="fig-sub">Dot size = how often he's on the ball there. Black = his busiest zones. Ringed: his pocket.</p>
<figcaption>Drawn from FotMob heatmap data (touch locations), Serie A 2025/26 (2,416 touches) and 2026/27 to 27 Nov (843 touches). Como attack upwards.</figcaption>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">03</span><h2 class="head">You know it's coming</h2></div>
<p>His move: pick it up in that pocket on the right, shift it inside onto the left foot, and either bend it towards the far post or slip it through for a runner. Everyone in the ground knows it's coming.</p></div>
<figure><p class="fig-title">3 of his 5 goals from outside the box last season came from right of centre</p>
<p class="fig-sub">Board: an illustration of the typical pattern. Black squares: his real 2025/26 Serie A goals from outside the box (hover or tap for detail).</p>
{svg("board.svg")}
<figcaption>Goal locations: FotMob shot data, Serie A 2025/26. The arrows are an illustration drawn from his touch and shot maps, not tracking data of a single goal.</figcaption></figure>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">04</span><h2 class="head">He does both jobs</h2></div>
<p>This is the one that makes him different. Most 10s either beat a man or win the ball. Paz does both, and he did it over a full season.</p></div>
<figure><p class="fig-title">Every Serie A attacking midfielder, 2025/26: tackles against dribbles</p>
<p class="fig-sub">Bigger dot = more minutes. Hover or tap any dot for the player and both numbers. Dashed lines: the middle of the 22.</p>
{svg("scatter.svg")}
<figcaption>FotMob league stats, Serie A 2025/26, filtered to attacking midfielders (22 players). Minutes are approximate: total tackles divided by tackles per 90.</figcaption></figure>
<div class="col"><ul>
<li><b>Only Messias sits near him</b>, and he did it in roughly 670 minutes against Paz's 2,882. Miretti matches his tackling in about 610 minutes but takes nobody on.</li>
<li><b>It has held up this season:</b> 2.73 tackles and 2.10 dribbles per 90 in 2026/27, against 2.84 and 2.15 last season. That's a trait, not a hot streak.</li>
<li><b>Possession makes the tackling stand out more.</b> Como have more of the ball than almost anyone in Serie A, so their players get fewer chances to defend. Adjusting for that would push his number up, not down.</li>
</ul></div>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">05</span><h2 class="head">Where he ranks</h2></div>
<p>Each line below is all 22 Serie A attacking midfielders last season. Elite at two things, middle of the pack at one, and we'll say so.</p></div>
<figure>{svg("strips.svg")}
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
<div class="col"><div class="part-head"><span class="no">06</span><h2 class="head">How he shoots</h2></div>
<p>He shoots on sight. A lot of it is from range, and that drags his chance quality down, but when he hits the target he hits it clean. His shots on target were worth more than the chances they came from in both seasons, and his free kicks are a weapon.</p></div>
<div class="two">{svg("shots-2526.svg")}{svg("shots-2627.svg")}</div>
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
<div class="part-head"><span class="no">07</span><h2 class="head">What his manager says</h2></div>
<p>Fàbregas built Como's attack around him, and you can hear it in how he talks about him.</p>
<div class="quote"><q>He's our brand.</q><p>On why Como wanted to keep him for many years.</p><span class="label">Fàbregas, press conference, January 2025, <a href="https://prod.beinsports.com/en-us/soccer/serie-a/articles-video/f%C3%A0bregas-secures-nico-paz-s-future-except-for-real-madrid-2025-01-18">via beIN Sports</a></span></div>
<div class="quote"><q>He trusts me and I trust him.</q><p>After the season that took Como into the Champions League.</p><span class="label">Fàbregas, May 2026, <a href="https://www.tuttomercatoweb.com/serie-a/fabregas-sul-suo-futuro-a-volte-si-parla-troppo-nico-paz-mi-fido-di-lui-e-lui-si-fida-di-me-2239893">via TuttoMercatoWeb</a></span></div>
<p>He has also said Como wouldn't sell him for 40 or 50 million, with only Real Madrid's buy-back able to take him, and he has <a href="https://www.90min.com/fr/real-madrid-cesc-fabregas-compare-lionel-messi-a-nico-paz-et-lui-donne-des-conseils-30-10-2025">compared him with Messi</a>.</p>
</div></div></section>

<section class="part fixpanel"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">08</span><h2 class="head">What's still raw</h2><span class="label">The honest bit</span></div>
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
<div class="part-head"><span class="no">09</span><h2 class="head">A 10 for a decade</h2></div>
<p>He's 22, already a starter in a Champions League side (33 league starts last season), and the bits he's elite at have held for two seasons. Get him in now and that's your 10 for the best part of ten years.</p>
<div class="tiles">{"".join(f"<div><span>{27 + k}/{28 + k}</span><b>{22 + k}</b></div>" for k in range(10))}</div>
<p class="note">His age at the start of each season.</p>
<p class="human">Is he the one to follow Bruno? Or is he one season too early?</p>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">10</span><h2 class="head">Method and sources</h2></div>
<ul>
<li><b>Player data:</b> <a href="https://www.fotmob.com/players/1347574/nico-paz">FotMob</a> season pages for Serie A 2025/26 and 2026/27 (to 27 Nov): touches, shots, xG, xGOT, tackles, dribbles, recoveries. Touch and shot maps are drawn from FotMob's location data.</li>
<li><b>Positional comparison:</b> FotMob league stats for Serie A 2025/26 filtered to attacking midfielders (22 qualifying players): <a href="https://www.fotmob.com/leagues/55/stats/season/27044/players/total_tackle/serie?position=attackingMidfielder">tackles</a>, <a href="https://www.fotmob.com/leagues/55/stats/season/27044/players/won_contest/serie?position=attackingMidfielder">dribbles</a>, <a href="https://www.fotmob.com/leagues/55/stats/season/27044/players/poss_won_att_3rd/serie?position=attackingMidfielder">ball won in the final third</a>.</li>
<li><b>The two-season rule:</b> something only counts as a trait if it shows up at the same level in both seasons. Ten-game swings (his box touches doubled this season) are treated as noise.</li>
<li><b>Same league, same position:</b> percentiles and rankings only compare Paz with Serie A attacking midfielders. We don't line up Serie A numbers against Premier League ones.</li>
<li><b>What the stats count:</b> "duels won" is left out because it double-counts tackles and dribbles. Tackle counts depend on how often a team is without the ball, so possession is discussed alongside them.</li>
<li><b>Role and style:</b> <a href="https://www.hudl.com/blog/nico-paz-como-statsbomb">Hudl StatsBomb on his inverted role</a>; <a href="https://tacticalfootballanalysis.com/como-2026-2027-cesc-fabregas-tactical-data-analysis-tactics/">Como's 2026/27 shape</a>.</li>
<li><b>News:</b> Bruno's contract option and United's interest in Paz as reported by The Athletic, 27 Nov 2026. Real Madrid's buy-back: club statement, June 2026; price as reported.</li>
<li><b>What we didn't have:</b> video, tracking data and possession-value models (OBV, xT). The tactics board is an illustration of a pattern seen in his maps, not a reconstruction of one goal.</li>
</ul>
</div></div></section>
<div id="tip" role="status" aria-live="polite"></div>
<script>
(function(){{
  var tip=document.getElementById('tip');
  var els=document.querySelectorAll('svg title');
  function show(t,x,y){{tip.textContent=t;tip.classList.add('on');
    var w=tip.offsetWidth,h=tip.offsetHeight;var L=Math.min(window.innerWidth-w-8,x+14),T=y-h-14;if(T<8)T=y+18;
    tip.style.left=L+'px';tip.style.top=T+'px';}}
  function hide(){{tip.classList.remove('on');}}
  els.forEach(function(ti){{
    var el=ti.parentNode,txt=ti.textContent;el.setAttribute('data-tip',txt);el.setAttribute('tabindex','0');el.setAttribute('aria-label',txt);ti.remove();
    el.addEventListener('pointerenter',function(e){{show(txt,e.clientX,e.clientY);}});
    el.addEventListener('pointermove',function(e){{show(txt,e.clientX,e.clientY);}});
    el.addEventListener('pointerleave',hide);
    el.addEventListener('click',function(e){{show(txt,e.clientX,e.clientY);e.stopPropagation();}});
    el.addEventListener('focus',function(){{var r=el.getBoundingClientRect();show(txt,r.right,r.top);}});
    el.addEventListener('blur',hide);
  }});
  document.addEventListener('click',hide);window.addEventListener('scroll',hide,{{passive:true}});
}})();
</script>
"""
