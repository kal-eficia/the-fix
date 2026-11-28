"""Prem Proven 10s: Cole Palmer and Morgan Gibbs-White, a transfer-watch deep dive (27 Nov 2026).
Charts are drawn in the browser (site/prem-proven-10s/app.js) from reports/prem_proven/data.json,
built from FotMob (Opta) Premier League data pulled on 28 Nov 2026."""
import json
from pathlib import Path

CLUB = "#C8102E"
DATA = Path(__file__).resolve().parent / "prem_proven" / "data.json"

META = {
    "slug": "prem-proven-10s",
    "date": "2026-11-27",
    "date_label": "27 Nov 2026",
    "fixture": "Transfer watch · Palmer and Gibbs-White",
    "club": CLUB,
    "share_image": "share.jpg",
    "title": "Prem Proven 10s",
    "summary": "If Bruno goes, Pochettino could go back for Cole Palmer or take Morgan Gibbs-White. Three seasons of Premier League data on both, penalties taken out.",
}

CSS = """<style>
.hero-img{width:100%;height:auto;display:block;mix-blend-mode:multiply;margin:0 0 clamp(10px,2vw,24px)}
.quote{border-left:8px solid var(--signal);padding:4px 0 4px 24px;margin:34px 0}
.quote q{display:block;font:italic 400 clamp(36px,5.4vw,70px)/1.04 var(--serif);quotes:"\\201C" "\\201D"}
.quote .label{display:block;margin-top:12px}
.verdict{display:grid;grid-template-columns:1fr 1fr;gap:0;border-top:3px solid var(--ink);margin:26px 0}
.verdict div{padding:16px 16px 6px 0}.verdict div+div{padding-left:16px;border-left:1px solid var(--ink)}
.verdict b{display:block;font:900 22px/1.05 var(--head);font-variation-settings:"wdth" 112;text-transform:uppercase}
.verdict b.pal{color:var(--signal)}
@media (max-width:700px){.verdict{grid-template-columns:1fr}.verdict div+div{padding-left:0;border-left:none;border-top:1px solid var(--ink)}}
.ctrl{display:flex;flex-wrap:wrap;gap:12px 22px;align-items:center;margin:18px 0 8px;font:600 12px/1.2 var(--mono);letter-spacing:.1em;text-transform:uppercase}
.ctrl select{font:600 13px var(--mono);background:var(--paper);color:var(--ink);border:2px solid var(--ink);padding:6px 8px;margin-left:6px}
.ctrl .rng{display:flex;align-items:center;gap:8px}.ctrl input[type=range]{accent-color:var(--signal);width:170px}
.ctrl output{min-width:110px;color:var(--signal)}
.grp{display:inline-flex;border:2px solid var(--ink)}.grp button{font:600 12px var(--mono);letter-spacing:.08em;text-transform:uppercase;background:var(--paper);color:var(--ink);border:0;padding:9px 12px;cursor:pointer}
.grp button+button{border-left:2px solid var(--ink)}.grp button[aria-pressed=true]{background:var(--ink);color:var(--paper)}
.count{color:var(--soft);margin:6px 0 0;font:600 12px/1.4 var(--mono);letter-spacing:.08em;text-transform:uppercase}
.chart svg{width:100%;height:auto;display:block;overflow:visible}
.chart.pitch{max-width:620px;margin:0 auto}
.tick{font:13px var(--mono);fill:var(--soft)}.axl{font:700 13px var(--mono);letter-spacing:.14em;fill:var(--ink)}.ql{font:700 12px var(--mono);letter-spacing:.12em;fill:var(--signal)}
.lab{font:800 13px var(--mono);fill:var(--ink)}.lab.s{fill:var(--signal)}
.big3{font:900 30px var(--head);font-variation-settings:"wdth" 110}
.pt{transition:transform .7s cubic-bezier(.2,.8,.2,1),opacity .35s}.pt.off{opacity:.06;pointer-events:none}
.bar{transform-box:fill-box;transform-origin:bottom;transition:transform .8s cubic-bezier(.2,.8,.2,1)}
.hbar{transform-box:fill-box;transform-origin:left;transition:transform .8s cubic-bezier(.2,.8,.2,1)}
.js .grow:not(.in) .bar{transform:scaleY(0)}.js .grow:not(.in) .hbar{transform:scaleX(0)}
.shot{transition:opacity .3s}.shot.off{opacity:.06}
.split{display:flex;height:64px;margin:18px 0 8px;font:800 14px var(--mono);letter-spacing:.08em}
.split span{display:flex;align-items:center;padding:0 16px}.split .a{background:var(--signal);color:var(--ink)}.split .b{background:#8a867d;color:var(--paper);justify-content:flex-end}
.js .split span{transform-origin:left;transition:transform .9s cubic-bezier(.2,.8,.2,1)}.js .split:not(.in) span{transform:scaleX(0)}
@media (prefers-reduced-motion:reduce){.pt,.bar,.hbar,.split span{transition:none}.js .grow:not(.in) .bar,.js .grow:not(.in) .hbar,.js .split:not(.in) span{transform:none}}
#tip{position:fixed;z-index:60;pointer-events:none;background:var(--ink);color:var(--paper);font:600 13px/1.35 var(--mono);padding:8px 10px;max-width:280px;opacity:0;transition:opacity .12s;white-space:pre-line}
#tip.on{opacity:1}
svg [tabindex]{cursor:pointer;outline:none}
</style>"""

SRC = '<a href="https://www.fotmob.com/players/1096353/cole-palmer">FotMob (Opta)</a>'


def body():
    data = DATA.read_text(encoding="utf-8")
    return CSS + f"""
<div class="strip"><div class="wrap label"><span>Transfer watch</span><span>Cole Palmer · Chelsea · 24</span><span>Morgan Gibbs-White · Forest · 26</span><span><b>Options if Bruno goes</b></span></div></div>
<section class="hero"><div class="wrap">
<img class="hero-img" src="hero.jpg" width="1400" height="933" alt="Cole Palmer and Morgan Gibbs-White, printed in halftone">
<p class="kick label"><i>The Fix</i> Deep dive</p>
<h1 class="head">Prem Proven 10s</h1>
<p class="human">If Bruno goes, Pochettino could go back for the 10 he already got the best out of, or take the one who's always out there. Three seasons of Premier League numbers on Cole Palmer and Morgan Gibbs-White, penalties taken out.</p>
<div class="score">
<div><span class="big"><em>1st</em><small>/48</small></span><p>Palmer's Poch season, for chances got plus chances made, among every Premier League attacking-midfielder season since 2023/24</p></div>
<div><span class="big"><span data-count="9">9</span><small>/22</small></span><p>Palmer's 2023/24 league goals that were penalties</p></div>
<div><span class="big"><span data-count="3160">3,160</span></span><p>Gibbs-White's league minutes in 2023/24. He's played 2,800+ every full season</p></div>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">01</span><h2 class="head">The short version</h2></div>
<p class="count">Updated 28 Nov: includes Gibbs-White's two goals in Forest's 3-2 win over Chelsea.</p>
<p>Pochettino is now United's manager, Bruno's future is up in the air, and both of these have been linked with Old Trafford. They're very different bets. We compared each with every Premier League attacking midfielder over three seasons, with penalties stripped out.</p>
<div class="verdict">
<div><b class="pal">Palmer</b><p>The best numbers of any 10 in the league over three seasons, even without the penalties. It wasn't a one-season wonder, and Pochettino has already got the best out of him once. The worry is the last 18 months.</p></div>
<div><b>Gibbs-White</b><p>Always available, Forest's captain, and he does it with much less of the ball. But he's been a creator, then a scorer, then a creator again, and never top-quarter at both in the same season.</p></div>
</div>
<p>Neither of them makes chances like Bruno. That part doesn't get replaced like for like.</p>
</div></div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">02</span><h2 class="head">The bar is Bruno</h2></div>
<p>Start with the job. Bruno's been 1st or 2nd among Premier League attacking midfielders for chances created in every season we looked at. Switch the stat and the season and see where the two options land.</p></div>
<figure id="barLab"><div class="ctrl"><label>Stat<select class="stat"><option value="6">Chances created per 90</option><option value="7">Big chances created per 90</option><option value="5">xA per 90</option><option value="4">Non-penalty xG per 90</option></select></label>
<span class="grp seasons"><button type="button" data-s="2324">23/24</button><button type="button" data-s="2425">24/25</button><button type="button" data-s="2526" aria-pressed="true">25/26</button><button type="button" data-s="2627">26/27 so far</button></span></div>
<div class="chart"></div><p class="count"></p>
<figcaption>{SRC}, Premier League. Players whose main position is attacking midfielder, min 1,350 minutes (500 for 2026/27 so far). Chances created include set pieces, and Bruno takes plenty of them. Hover or tap any dot.</figcaption></figure>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">03</span><h2 class="head">Only one has done both</h2></div>
<p>A 10 has two jobs: get on the end of chances and make them for others. Across is non-penalty xG per 90 (chances he gets), up is xA per 90 (chances he makes). Every dot is one player's season.</p></div>
<figure id="bothLab"><div class="ctrl">
<span class="grp seasons"><button type="button" data-s="all" aria-pressed="true">All three</button><button type="button" data-s="2324">23/24</button><button type="button" data-s="2425">24/25</button><button type="button" data-s="2526">25/26</button></span>
<span class="rng">Min minutes <input type="range" class="mins" min="1350" max="3200" step="50" value="1350"><output>1,350</output></span>
<label>Highlight<select class="pick"><option value="">Nobody else</option></select></label></div>
<div class="chart"></div><p class="count"></p>
<figcaption>{SRC}, Premier League, 2023/24 to 2025/26. 48 attacking-midfielder seasons at 1,350+ minutes. Dashed lines: the median of the 48. Penalties are excluded from xG.</figcaption></figure>
<div class="col"><p>Palmer's two big seasons are 1st and 3rd of the 48 for the two added together. Bruno's seasons are 6th, 10th and 12th, and almost all of that is the making. Gibbs-White's best is 18th.</p></div>
</div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">04</span><h2 class="head">The Poch season</h2></div>
<p>2023/24 at Chelsea: 22 league goals and 11 assists, more goal involvements than anyone in the league, in his first season as a regular. The obvious question is how much of that was penalties.</p>
<div class="split" aria-label="13 non-penalty goals and 9 penalties"><span class="a" style="flex:13">13 OPEN PLAY & SET PIECES</span><span class="b" style="flex:9">9 PENS</span></div>
<p>Nine of the 22, and he scored every one. Take them all out and it's still the best attacking-midfielder season in the league in three years: 1st of 48 for non-penalty xG and xA added together.</p>
<div class="quote"><q>One of his best skills is his mentality and his capacity to deal with the pressure.</q><span class="label">Pochettino, April 2024, <a href="https://premierleague.com/news/3954071">via premierleague.com</a></span></div>
</div></div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">05</span><h2 class="head">Not a one-off</h2></div>
<p>The season after Pochettino left, Palmer actually got better chances: 13.4 non-penalty xG against 11.1. He scored fewer because he took fewer penalties and finished a bit colder. Goals minus xG swings from year to year; the chances are the steadier signal. Two elite seasons in a row passes our two-season test.</p></div>
<figure><div class="chart grow" id="palBars"></div>
<figcaption>{SRC}, Premier League season totals, from FotMob's shot maps. 2026/27 to 27 Nov.</figcaption></figure>
<div class="col"><p>The worry is what came after: a groin problem that kept him out for much of autumn 2025, 1,965 league minutes last season, and middling numbers in 1,060 minutes this season. That's a small sample, so we wouldn't read much into it either way.</p></div>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">06</span><h2 class="head">Three different Gibbs-Whites</h2></div>
<p>Gibbs-White's profile keeps changing. In 2023/24 he was a creator (10 assists). In 2025/26 he became a goalscorer. This season he's back to making chances, and he's 1st of 14 for big chances created.</p></div>
<figure><div class="chart grow" id="mgwBars"></div>
<figcaption>{SRC}, Premier League, per 90 minutes, penalties excluded. 2026/27: 990 minutes so far.</figcaption></figure>
<div class="col"><p>Last season's 14 open-play goals came from 10.3 xG. Beating your xG by nearly four is a hot streak, and those rarely repeat: this season it's one from 2.2. That one came on Friday night, when he scored twice (the other a penalty) in Forest's 3-2 win over Palmer's Chelsea, with the top FotMob rating on the pitch (8.9). He's never been top-quarter for scoring and creating in the same season.</p>
<p>There is real context, though. Forest had 40.3%, 40.8% and 46.8% of the ball across these three seasons. Chelsea had 59.0%, 57.2% and 57.7%. Gibbs-White's numbers come with a lot less possession.</p></div>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">07</span><h2 class="head">Where they shoot from</h2></div>
<p>Every non-penalty shot, bigger circle for a better chance. Pick a player and a season.</p></div>
<figure id="shotLab"><div class="ctrl">
<span class="grp who"><button type="button" data-p="pal" aria-pressed="true">Palmer</button><button type="button" data-p="mgw">Gibbs-White</button></span>
<span class="grp seasons"><button type="button" data-s="2324" aria-pressed="true">23/24</button><button type="button" data-s="2425">24/25</button><button type="button" data-s="2526">25/26</button><button type="button" data-s="2627">26/27</button></span>
<span class="grp filt"><button type="button" data-f="all" aria-pressed="true">All</button><button type="button" data-f="goal">Goals</button><button type="button" data-f="out">Outside box</button></span></div>
<div class="chart pitch"></div><p class="count"></p>
<figcaption>{SRC} shot maps, Premier League. Penalties left out. Attacking upwards.</figcaption></figure>
<div class="col"><p>Palmer shoots a lot from distance: more than half his non-penalty shots in both big seasons came from outside the box, almost all with his left foot. Gibbs-White's scoring season came when he moved his shooting closer: 34% from outside the box, down from 51% two seasons before.</p></div>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">08</span><h2 class="head">The catch for each</h2></div>
<p>League minutes every season. One is always out there.</p></div>
<figure><div class="chart grow" id="minsBars"></div>
<figcaption>{SRC}, Premier League. A full 38-game season is 3,420 minutes. 2026/27 to 27 Nov.</figcaption></figure>
<div class="col">
<p><b>Palmer:</b> the injury is the obvious one. The other is the work without the ball. In his Poch season he was last of 14 attacking midfielders for tackles and for recoveries per 90. Chelsea had the ball 59% of the time, which keeps those numbers down, but he's never going to be a 10 who presses for fun.</p>
<p><b>Gibbs-White:</b> you're buying reliability and graft, not Palmer's ceiling. He was 18th of 19 for tackles last season too, so neither is a Bruno-style runner.</p>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">09</span><h2 class="head">So who do you take?</h2></div>
<div class="verdict">
<div><b class="pal">Palmer</b><p>The swing for the fences. Highest ceiling of any 10 in the league, a manager who's already unlocked him, and Chelsea have him tied down to 2034, so he won't come cheap.</p></div>
<div><b>Gibbs-White</b><p>The safer bet. Plays every week, captains his club, contract to 2028. Gives you a good 10, not a great one.</p></div>
</div>
<p class="human">Who are you taking?</p>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">10</span><h2 class="head">Method and sources</h2></div>
<ul>
<li><b>Data:</b> FotMob (Opta) season stats and shot maps for <a href="https://www.fotmob.com/players/1096353/cole-palmer">Palmer</a> and <a href="https://www.fotmob.com/players/789502/morgan-gibbs-white">Gibbs-White</a>, and FotMob's Premier League stats for every attacking midfielder, pulled 28 Nov 2026, so Forest's 3-2 win over Chelsea on 27 Nov is included.</li>
<li><b>Comparison set:</b> players whose main FotMob position is attacking midfielder, min 1,350 minutes a season (Opta's radar threshold): 14 in 2023/24, 15 in 2024/25, 19 in 2025/26. That's 48 player-seasons. For 2026/27 so far, min 500 minutes (14 players).</li>
<li><b>Penalties out:</b> non-penalty xG and goals are counted from the shot maps. Chances created and xA include set pieces.</li>
<li><b>Two-season rule:</b> something only counts as a trait if it shows up in two seasons. Goals minus xG is treated as mostly noise.</li>
<li><b>Context:</b> team possession from FotMob's Premier League team stats. Tackles and recoveries depend on how much a team is without the ball.</li>
<li><b>News:</b> Pochettino's appointment (<a href="https://theanalyst.com/?p=269147">The Analyst</a>); United linked with Gibbs-White as a Bruno replacement (<a href="https://www.goal.com/en/lists/man-utd-morgan-gibbs-white-potential-bruno-fernandes-replacement-wage-bill/bltb2dcad9de73777d9">GOAL</a>); Palmer's 2025 groin injury (<a href="https://www.si.com/soccer/cole-palmer-injury-progress-potential-return-date-chelsea-star">SI</a>). Contracts from FotMob.</li>
<li><b>What we didn't have:</b> tracking data and possession-value models (OBV, xT). The halftone photos are printed from press images.</li>
</ul>
</div></div></section>
<script id="p10data" type="application/json">{data}</script>
<div id="tip" role="status" aria-live="polite"></div>
<script src="app.js" defer></script>
"""
