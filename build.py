#!/usr/bin/env python3
"""Build The Fix analysis site into site/. Standard library only.

Each report is a Python module in reports/ that returns its body HTML. Charts are drawn as inline SVG
from the data in that module, in The Fix brand (paper, ink, one signal colour, club colour for the focus team).
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"

PAPER, SHADE, INK, SOFT, SIGNAL, FIX = "#E8E4DA", "#DCD7CB", "#121212", "#6E6A62", "#FF5A1F", "#1F8A5B"

CSS = """
@font-face{font-family:"Archivo";src:url(ASSETS/fonts/Archivo-VF.woff2) format("woff2");font-weight:100 900;font-stretch:62% 125%;font-display:swap}
@font-face{font-family:"Instrument Serif";src:url(ASSETS/fonts/InstrumentSerif-Italic.woff2) format("woff2");font-style:italic;font-display:swap}
@font-face{font-family:"JetBrains Mono";src:url(ASSETS/fonts/JetBrainsMono-VF.woff2) format("woff2");font-weight:100 800;font-display:swap}
:root{--paper:#E8E4DA;--shade:#DCD7CB;--ink:#121212;--soft:#6E6A62;--signal:#FF5A1F;--fix:#1F8A5B;--club:#C8102E;
--head:"Archivo","Arial Black",system-ui,sans-serif;--serif:"Instrument Serif",Georgia,serif;--mono:"JetBrains Mono",ui-monospace,Menlo,monospace;
--g:clamp(18px,4vw,48px)}
*{box-sizing:border-box}
html{background:var(--ink)}
body{margin:0;background:var(--paper);color:var(--ink);font:400 17px/1.62 var(--head);font-variation-settings:"wdth" 100;-webkit-font-smoothing:antialiased;position:relative}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:50;opacity:.45;mix-blend-mode:multiply;
background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .35 0 0 0 0 .32 0 0 0 0 .27 0 0 0 .5 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
a{color:inherit;text-decoration:underline;text-decoration-color:var(--signal);text-decoration-thickness:2px;text-underline-offset:3px}
a:hover{color:var(--signal)}
:focus-visible{outline:3px solid var(--signal);outline-offset:3px}
.wrap{max-width:1160px;margin:0 auto;padding-inline:var(--g)}
.col{max-width:760px}
.mono{font-family:var(--mono)}
.label{font:600 12px/1.2 var(--mono);letter-spacing:.14em;text-transform:uppercase}
.head{font-family:var(--head);font-weight:900;font-variation-settings:"wdth" 125;text-transform:uppercase;letter-spacing:-.02em;line-height:.88;margin:0}
.serif{font-family:var(--serif);font-style:italic;font-weight:400}

/* masthead: the programme's top strip */
.mast{border-bottom:3px solid var(--ink)}
.mast .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;padding-block:16px}
.mast img{height:40px;width:auto;display:block}
.mast nav{display:flex;gap:20px}.mast nav a{text-decoration:none}
.strip{background:var(--ink);color:var(--paper)}
.strip .wrap{display:flex;flex-wrap:wrap;gap:8px 26px;padding-block:9px}
.strip b{color:var(--signal);font-weight:600}

/* hero */
.hero{padding-block:clamp(40px,7vw,88px) clamp(32px,5vw,64px);border-bottom:3px solid var(--ink)}
.hero .kick{display:flex;align-items:center;gap:12px;margin:0 0 22px}
.hero .kick i{font-style:normal;background:var(--ink);color:var(--paper);padding:5px 9px}
.hero h1{font-size:clamp(44px,7.6vw,100px);max-width:14ch;text-wrap:balance}
.hero .human{font-size:clamp(22px,2.6vw,32px);line-height:1.22;max-width:30ch;margin:26px 0 0}
.score{display:grid;grid-template-columns:repeat(3,1fr);border-top:3px solid var(--ink);margin-top:clamp(32px,5vw,56px)}
.score>div{padding:18px 18px 4px 0}.score>div+div{padding-left:18px;border-left:1px solid var(--ink)}
.big{display:block;font:900 clamp(54px,8vw,104px)/.85 var(--head);font-variation-settings:"wdth" 125;letter-spacing:-.03em}
.big em{font-style:normal;color:var(--club)}.big small{font-size:.42em;color:var(--soft)}
.score p{margin:10px 0 0;font:500 14px/1.4 var(--mono);color:var(--soft)}
@keyframes stretch{0%{font-variation-settings:"wdth" 62;opacity:0}60%{opacity:1}100%{font-variation-settings:"wdth" 125}}
.big{animation:stretch .9s cubic-bezier(.2,1.5,.4,1) both}
.score>div:nth-child(2) .big{animation-delay:.12s}.score>div:nth-child(3) .big{animation-delay:.24s}
@media (prefers-reduced-motion:reduce){.big{animation:none}}
@media (max-width:760px){.score{grid-template-columns:1fr}.score>div+div{padding-left:0;border-left:none;border-top:1px solid var(--ink)}}

/* sections */
section.part{padding-block:clamp(44px,6vw,80px);border-bottom:1px solid var(--ink)}
.part-head{display:grid;grid-template-columns:88px 1fr;gap:6px 20px;align-items:start;margin-bottom:26px}
.part-head .no{font:900 56px/.8 var(--head);font-variation-settings:"wdth" 125;color:var(--signal)}
.part-head h2{font-size:clamp(32px,4.6vw,58px)}
.part-head .label{grid-column:2;color:var(--soft)}
@media (max-width:600px){.part-head{grid-template-columns:1fr}.part-head .label{grid-column:1}}
.part p{margin:0 0 16px;max-width:66ch}
.part ul{margin:20px 0;padding:0;list-style:none;max-width:70ch}
.part li{position:relative;padding:14px 0 14px 30px;border-top:1px solid rgba(18,18,18,.25)}
.part li::before{content:"";position:absolute;left:0;top:23px;width:12px;height:12px;background:var(--ink)}
.part li b{font-weight:800}
.human{font-family:var(--serif);font-style:italic;font-size:clamp(22px,2.4vw,28px);line-height:1.25;max-width:36ch}
table{border-collapse:collapse;width:100%;margin:28px 0 10px;font-size:16px}
th{font:600 11.5px/1.3 var(--mono);letter-spacing:.12em;text-transform:uppercase;text-align:left;padding:0 14px 10px 0;border-bottom:3px solid var(--ink);vertical-align:bottom}
td{padding:13px 14px 13px 0;border-bottom:1px solid rgba(18,18,18,.3);vertical-align:top}
td.n{font:600 18px/1.3 var(--mono);white-space:nowrap}td.n.us{color:var(--club)}
.scroll{overflow-x:auto}
figure{margin:34px 0 26px}
figure>svg{width:100%;height:auto;display:block}
.fig-sub svg{width:14px;height:14px;display:inline-block;vertical-align:-2px;margin-right:4px}
figcaption{font:400 12.5px/1.5 var(--mono);color:var(--soft);margin-top:10px;max-width:90ch}
.fig-title{font:900 clamp(20px,2.4vw,28px)/1 var(--head);font-variation-settings:"wdth" 112;text-transform:uppercase;letter-spacing:-.01em;margin:0 0 6px}
.fig-sub{font:500 13px/1.45 var(--mono);color:var(--soft);margin:0 0 14px}
.note{font:400 14px/1.55 var(--mono);color:var(--soft);max-width:80ch}

/* the fix panel */
.fixpanel{background:var(--ink);color:var(--paper)}
.fixpanel .part-head .no{color:var(--signal)}.fixpanel .part-head .label{color:#B8B2A6}
.fixpanel li{border-top-color:rgba(232,228,218,.3)}.fixpanel li::before{background:var(--signal)}
.fixpanel a{color:var(--paper)}
.caveat{border-left:6px solid var(--signal);padding:6px 0 6px 18px;margin:28px 0 0}

/* index cards */
.cards{display:grid;gap:0;border-top:3px solid var(--ink);margin-top:36px}
.card{display:grid;grid-template-columns:150px 1fr;gap:20px;padding:26px 0;border-bottom:1px solid var(--ink);text-decoration:none}
.card:hover h3{color:var(--signal)}
.card h3{font-size:clamp(26px,3.4vw,40px)}
.card p{margin:10px 0 0;color:var(--soft)}
@media (max-width:600px){.card{grid-template-columns:1fr}}

footer{background:var(--ink);color:#B8B2A6;padding-block:44px;font:400 14px/1.6 var(--mono)}
footer .wrap{display:flex;flex-wrap:wrap;gap:28px;justify-content:space-between;align-items:flex-start}
footer img{height:44px}footer a{color:var(--paper)}footer p{margin:0;max-width:60ch}
"""


def page(title, desc, body, depth, club):
    assets = "../" * depth + "assets"
    home = "../" * depth or "./"
    css = CSS.replace("ASSETS", assets).replace("--club:#C8102E", f"--club:{club}")
    html = f"""<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{assets}/logo/avatar-signal.png"><meta name="theme-color" content="#121212">
<link rel="icon" href="{assets}/logo/mark.svg" type="image/svg+xml">
<link rel="preload" href="{assets}/fonts/Archivo-VF.woff2" as="font" type="font/woff2" crossorigin>
<style>{css}</style></head><body>
<header class="mast"><div class="wrap"><a href="{home}" aria-label="The Fix home"><img src="{assets}/logo/lockup-ink.png" alt="The Fix" width="154" height="40"></a>
<nav class="label"><a href="{home}">Reports</a></nav></div></header>
<main>{body}</main>
<footer><div class="wrap"><img src="{assets}/logo/lockup-paper.png" alt="The Fix" width="169" height="44">
<p>The Fix is football analysis by Kalid Nur: what's wrong, why, and the fix, told with the numbers. Event data is Opta's, read from public match centres; every source is linked on the page it supports.</p></div></footer>
</body></html>
"""
    assert "—" not in html, "no em dashes"
    return html


def load_reports():
    out = []
    for p in sorted((ROOT / "reports").glob("*.py")):
        spec = importlib.util.spec_from_file_location(p.stem, p)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out.append(mod)
    return sorted(out, key=lambda m: m.META["date"], reverse=True)


def build():
    reports = load_reports()
    for r in reports:
        m = r.META
        d = SITE / m["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(m["title"] + " | The Fix", m["summary"], r.body(), 1, m["club"]), encoding="utf-8")
    cards = "".join(
        f'<a class="card" href="{r.META["slug"]}/"><span class="label">{r.META["date_label"]}<br>{r.META["fixture"]}</span>'
        f'<div><h3 class="head">{r.META["title"]}</h3><p>{r.META["summary"]}</p></div></a>' for r in reports)
    body = f"""<section class="hero"><div class="wrap">
<p class="kick label"><i>The Fix</i> Analysis</p>
<h1 class="head">What's wrong, why, and the fix</h1>
<p class="human serif">Football analysis told with the numbers, one match at a time.</p>
<div class="cards">{cards}</div></div></section>"""
    (SITE / "index.html").write_text(page("The Fix | Football analysis", "What's wrong, why, and the fix: football analysis told with the numbers.", body, 0, "#C8102E"), encoding="utf-8")
    (SITE / ".nojekyll").write_text("")
    print("built", len(reports), "report(s) into", SITE)


if __name__ == "__main__":
    build()
