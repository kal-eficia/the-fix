"""Branthwaite or Bassey: a transfer-watch deep dive on United's left-sided centre-back search (27 Nov 2026).
Charts are drawn in the browser (site/branthwaite-bassey/app.js) from reports/cb_watch/data.json,
built from FotMob (Opta) Premier League data for 2025/26 and 2026/27, pulled on 27 Nov 2026."""
from pathlib import Path

CLUB = "#C8102E"
DATA = Path(__file__).resolve().parent / "cb_watch" / "data.json"
HERO = Path(__file__).resolve().parent.parent / "site" / "branthwaite-bassey" / "hero.jpg"

META = {
    "slug": "branthwaite-bassey",
    "date": "2026-11-27",
    "date_label": "27 Nov 2026",
    "fixture": "Transfer watch · Branthwaite and Bassey",
    "club": CLUB,
    "share_image": "share.jpg",
    "title": "Branthwaite or Bassey?",
    "summary": "United want a left-sided centre-back. One of these two gives you Maguire's presence in the air, the other gives you pace. Two seasons of data on both, against every centre-back in the league.",
}

CSS = """<style>
.hero-img{width:100%;height:auto;display:block;mix-blend-mode:multiply;margin:0 0 clamp(10px,2vw,24px)}
.verdict{display:grid;grid-template-columns:1fr 1fr;gap:0;border-top:3px solid var(--ink);margin:26px 0}
.verdict div{padding:16px 16px 6px 0}.verdict div+div{padding-left:16px;border-left:1px solid var(--ink)}
.verdict b{display:block;font:900 22px/1.05 var(--head);font-variation-settings:"wdth" 112;text-transform:uppercase}
.verdict b.a{color:var(--signal)}
@media (max-width:700px){.verdict{grid-template-columns:1fr}.verdict div+div{padding-left:0;border-left:none;border-top:1px solid var(--ink)}}
.ctrl{display:flex;flex-wrap:wrap;gap:12px 22px;align-items:center;margin:18px 0 8px;font:600 12px/1.2 var(--mono);letter-spacing:.1em;text-transform:uppercase}
.ctrl select{font:600 13px var(--mono);background:var(--paper);color:var(--ink);border:2px solid var(--ink);padding:6px 8px;margin-left:6px}
.ctrl label.chk{display:flex;align-items:center;gap:8px;cursor:pointer}.ctrl input[type=checkbox]{accent-color:var(--signal);width:18px;height:18px}
.grp{display:inline-flex;border:2px solid var(--ink)}.grp button{font:600 12px var(--mono);letter-spacing:.08em;text-transform:uppercase;background:var(--paper);color:var(--ink);border:0;padding:9px 12px;cursor:pointer}
.grp button+button{border-left:2px solid var(--ink)}.grp button[aria-pressed=true]{background:var(--ink);color:var(--paper)}
.count{color:var(--soft);margin:6px 0 0;font:600 12px/1.4 var(--mono);letter-spacing:.08em;text-transform:uppercase}
.chart svg{width:100%;height:auto;display:block;overflow:visible}
.tick{font:13px var(--mono);fill:var(--soft)}.axl{font:700 13px var(--mono);letter-spacing:.14em;fill:var(--ink)}.ql{font:700 12px var(--mono);letter-spacing:.12em;fill:var(--signal)}
.lab{font:800 13px var(--mono);fill:var(--ink)}.lab.s{fill:var(--signal)}.grp-t{font:900 15px var(--head);font-variation-settings:"wdth" 112;letter-spacing:.02em;fill:var(--ink)}
.pt{transition:transform .7s cubic-bezier(.2,.8,.2,1),opacity .35s}.pt.off{opacity:.07;pointer-events:none}
.dd{transition:transform .8s cubic-bezier(.2,.8,.2,1)}
.hbar{transform-box:fill-box;transform-origin:left;transition:transform .8s cubic-bezier(.2,.8,.2,1)}
.js .grow:not(.in) .hbar{transform:scaleX(0)}
.js .grow:not(.in) .dd{transform:translateX(-40px);opacity:0}
.tbl{width:100%;border-collapse:collapse;font:600 14px/1.3 var(--mono);margin:20px 0}
.tbl th,.tbl td{text-align:right;padding:9px 8px;border-bottom:1px solid rgba(18,18,18,.18)}.tbl th:first-child,.tbl td:first-child{text-align:left}
.tbl thead th{font-size:11px;letter-spacing:.12em;text-transform:uppercase;border-bottom:3px solid var(--ink)}
.tbl td.hi{color:var(--signal)}
@media (max-width:640px){.tbl{font-size:12px}.tbl th,.tbl td{padding:7px 4px}}
@media (prefers-reduced-motion:reduce){.pt,.dd,.hbar{transition:none}.js .grow:not(.in) .hbar,.js .grow:not(.in) .dd{transform:none;opacity:1}}
@media (max-width:640px){.hero h1.head{font-size:10vw;font-variation-settings:"wdth" 100}}
#tip{position:fixed;z-index:60;pointer-events:none;background:var(--ink);color:var(--paper);font:600 13px/1.35 var(--mono);padding:8px 10px;max-width:300px;opacity:0;transition:opacity .12s;white-space:pre-line}
#tip.on{opacity:1}
svg [tabindex]{cursor:pointer;outline:none}
</style>"""

FM = '<a href="https://www.fotmob.com/players/1030829/jarrad-branthwaite">FotMob (Opta)</a>'


def body():
    data = DATA.read_text(encoding="utf-8")
    hero = '<img class="hero-img" src="hero.jpg" width="1400" height="933" alt="Jarrad Branthwaite and Calvin Bassey, printed in halftone">' if HERO.exists() else ""
    return CSS + f"""
<div class="strip"><div class="wrap label"><span>Transfer watch</span><span>Jarrad Branthwaite · Everton · 24</span><span>Calvin Bassey · Fulham · 26</span><span><b>United's left-sided centre-back search</b></span></div></div>
<section class="hero"><div class="wrap">
{hero}
<p class="kick label"><i>The Fix</i> Deep dive</p>
<h1 class="head">Branthwaite or Bassey?</h1>
<p class="human">United want a left-sided centre-back, and these are the two names on the list. One gives you Maguire's presence in the air. The other gives you pace and a defender who's hard to get past. Two seasons of numbers, against every centre-back in the league.</p>
<div class="score">
<div><span class="big"><em>3rd</em><small>/51</small></span><p>Branthwaite for height at 195cm, among 51 Premier League centre-backs. Maguire is 194cm</p></div>
<div><span class="big"><span data-count="73">73</span><small>%</small></span><p>Aerial duels Branthwaite wins, 3rd of 51. Bassey wins 56%, 34th</p></div>
<div><span class="big">5th<small>/51</small></span><p>Bassey for sprints per 90, and 11th for top speed. Branthwaite is 34th and 14th</p></div>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">01</span><h2 class="head">The short version</h2></div>
<p>Pochettino wants a left-sided centre-back, and both of these play there: FotMob logs both as left centre-backs. They're very different defenders, though, and the choice depends on what United are replacing.</p>
<div class="verdict">
<div><b class="a">Branthwaite</b><p>Dominant in the air, 6ft 5in and quick for his size. He'd replace what United lose if Maguire goes. The worry is fitness: 681 league minutes last season.</p></div>
<div><b>Bassey</b><p>Rapid, aggressive and hard to dribble past, and he has been available every season. But he's 9cm shorter and loses a lot more in the air.</p></div>
</div>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">02</span><h2 class="head">The job</h2></div>
<p>Reports say Branthwaite and Bassey are high on United's list for the left side of the back line, with Lisandro Martínez's future uncertain (<a href="https://www.livescore.com/en/news/football/premier-league/manchester-united-show-serious-interest-in-former-ajax-and-psv-players-goal/">GOAL</a>). Sky reported on 18 November that the club wants a centre-back in January, with Pochettino having a say in who (<a href="https://azat.tv/en/manchester-united-january-transfer-targets-pochettino/">via Sky Sports News</a>).</p>
<p>Then there's Maguire. He's signed until June 2027 with an option for a further year (<a href="https://www.manutd.com/en/news/detail/Harry-Maguire-signs-new-contract-with-Man-Utd-until-at-least-2027">Manchester United</a>), so he isn't leaving yet. But he's 33, and when he does go, United lose one of the best headers of a ball in the league: he wins 74% of his aerial duels, 2nd of 51 centre-backs. Lisandro, United's other senior left-sided centre-back, is the shortest centre-back in the group at 178cm.</p>
</div></div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">03</span><h2 class="head">The physical map</h2></div>
<p>Every Premier League centre-back with 1,350+ league minutes across last season and this one. Across is how often he wins his headers, up is top speed. Top right is the rare one: big, dominant in the air and quick.</p></div>
<figure id="mapLab"><div class="ctrl">
<label>Across<select class="xs"><option value="aerpct">Aerial duels won %</option><option value="aer90">Aerial duels won per 90</option><option value="h">Height</option></select></label>
<label>Up<select class="ys"><option value="ts">Top speed</option><option value="spr90">Sprints per 90</option></select></label>
<label class="chk"><input type="checkbox" class="leftonly"> Left centre-backs only</label>
<label>Highlight<select class="pick"><option value="">Nobody else</option></select></label></div>
<div class="chart"></div><p class="count"></p>
<figcaption>{FM}, Premier League 2025/26 and 2026/27 to 27 Nov, combined. Main position centre-back, min 1,350 minutes. Top speed is the fastest recorded across both seasons. Dashed lines: the median. Hover or tap any dot.</figcaption></figure>
<div class="col"><p>Branthwaite sits where Maguire does in the air, and he's nearly 2km/h quicker at top speed. Bassey is one of the fastest centre-backs in the league, but in the air he's in the bottom third.</p></div>
</div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">04</span><h2 class="head">Head to head</h2></div>
<p>Where each one ranks among the 51 centre-backs on every measure. Further right is better. Switch Maguire and Lisandro on to see who United would be replacing.</p></div>
<figure id="rankLab"><div class="ctrl"><label class="chk"><input type="checkbox" class="mag"> Show Maguire</label><label class="chk"><input type="checkbox" class="lis"> Show Lisandro</label></div>
<div class="chart grow"></div>
<figcaption>{FM}, Premier League, 2025/26 and 2026/27 combined, 51 centre-backs with 1,350+ minutes. Tackles plus interceptions are adjusted for team possession. For "dribbled past", fewer is better, so it's ranked that way round.</figcaption></figure>
</div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">05</span><h2 class="head">Defending</h2></div>
<p>Raw tackle counts flatter defenders in teams that don't have the ball, and Everton have had 44% to 45% of it against Fulham's 52% to 56%. So we adjust tackles and interceptions for possession. Once you do, Bassey comes out ahead: 9th of 51, against Branthwaite's 20th.</p>
<p>Bassey is also one of the hardest centre-backs in the league to dribble past (0.23 times per 90, 9th fewest). Branthwaite gets beaten more often (0.40, 32nd). Branthwaite makes more clearances, partly because Everton spend more time without the ball.</p>
<table class="tbl"><thead><tr><th>Per 90, both seasons</th><th>Branthwaite</th><th>Bassey</th><th>Maguire</th></tr></thead><tbody>
<tr><td>Aerial duels won</td><td class="hi">3.89</td><td>1.43</td><td>3.18</td></tr>
<tr><td>Aerial win %</td><td class="hi">73.1%</td><td>56.0%</td><td>74.0%</td></tr>
<tr><td>Tackles + interceptions (possession-adjusted)</td><td>2.58</td><td class="hi">2.98</td><td>2.31</td></tr>
<tr><td>Times dribbled past</td><td>0.40</td><td class="hi">0.23</td><td>0.31</td></tr>
<tr><td>Recoveries</td><td>3.49</td><td class="hi">3.94</td><td>3.74</td></tr>
<tr><td>Clearances</td><td class="hi">6.07</td><td>3.73</td><td>5.31</td></tr>
</tbody></table>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">06</span><h2 class="head">On the ball</h2></div>
<p>Neither is a standout passer. Bassey sees more of the ball (56 accurate passes per 90 against Branthwaite's 40) and is more secure with it (88% against 85%). Branthwaite's 85% is 38th of 51, and some of that is team context: Everton have much less of the ball. Their long passing is close: about 2.5 accurate long balls per 90 each.</p>
<p>For a Pochettino side that wants to build from the back, Bassey is the more comfortable on the ball of the two. Lisandro, the man he might be replacing, is better than both: 7th of 51 for accurate long balls.</p>
</div></div></section>

<section class="part"><div class="wrap">
<div class="col"><div class="part-head"><span class="no">07</span><h2 class="head">Who's always available</h2></div>
<p>League minutes, last four seasons. This is the biggest difference between them.</p></div>
<figure><div class="chart grow" id="minsBars"></div>
<figcaption>{FM}, Premier League. A full 38-game season is 3,420 minutes. 2026/27 to 27 Nov.</figcaption></figure>
<div class="col"><p>Branthwaite was an ever-present in 2023/24 (3,117 minutes), then lost most of last season to injury: 681 minutes, and only seven starts. He's started all ten league games he's played this season, but it's the reason a reported €90m price looks steep (<a href="https://www.footballtransfers.com/us/transfer-news/uk-premier-league/2026/09/manchester-utds-branthwaite-dilemma-after-everton-price-emerges-31329">FootballTransfers</a>). Bassey has played 2,300 to 3,074 minutes in each of the last three full seasons.</p>
<p>The contracts point the same way. Bassey's runs to June 2027, so Fulham are selling from a weaker position. Branthwaite is tied down until 2030 (both from FotMob).</p></div>
</div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">08</span><h2 class="head">So who do you take?</h2></div>
<div class="verdict">
<div><b class="a">Branthwaite</b><p>If the brief is "replace Maguire", he's the only one of the two who does it. He's as tall, wins as many headers and covers the ground behind better. You're paying a big fee for a player who missed most of last season.</p></div>
<div><b>Bassey</b><p>If the brief is "a quick, aggressive left-sided centre-back for a high line", he's the fitter option, and FotMob values him at about half Branthwaite's price (€27m against €50m). You'd need height somewhere else in the back four.</p></div>
</div>
<p class="human">Who are you taking?</p>
</div></div></section>

<section class="part"><div class="wrap"><div class="col">
<div class="part-head"><span class="no">09</span><h2 class="head">Method and sources</h2></div>
<ul>
<li><b>Data:</b> FotMob (Opta) season stats for <a href="https://www.fotmob.com/players/1030829/jarrad-branthwaite">Branthwaite</a>, <a href="https://www.fotmob.com/players/877401/calvin-bassey">Bassey</a> and every Premier League centre-back, pulled 27 Nov 2026. Heights, positions and contracts are from FotMob too.</li>
<li><b>Comparison set:</b> players whose main FotMob position is centre-back (left, right or central), 2025/26 and 2026/27 combined, min 1,350 minutes: 51 players. Combining the two seasons gives Branthwaite a fair sample (1,572 minutes) after his injury.</li>
<li><b>Possession adjustment:</b> tackles plus interceptions × 50 ÷ the opponent's share of the ball, season by season, using FotMob team possession.</li>
<li><b>Physical data:</b> top speed is the fastest recorded in either season; sprints are counted per 90. These come from FotMob's tracking-based physical stats.</li>
<li><b>Reports, not data:</b> United's interest, Lisandro's future and Branthwaite's price are as reported by the outlets linked above. We haven't treated any of them as fact.</li>
<li><b>What we didn't have:</b> tracking of where each one defends, or possession-value models. Aerial volume depends on how direct a team is, so we lean on win rate.</li>
</ul>
</div></div></section>
<script id="cbdata" type="application/json">{data}</script>
<div id="tip" role="status" aria-live="polite"></div>
<script src="app.js" defer></script>
"""
