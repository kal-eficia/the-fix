# The Fix

Football analysis by Kalid Nur: what's wrong, why, and the fix, told with the numbers.

**Read it:** [kal-eficia.github.io/the-fix](https://kal-eficia.github.io/the-fix/)

## Reports

| Date | Match | Report |
|---|---|---|
| 25 Nov 2026 | Sporting 2-2 Man United | [How Man United won the ball back at Sporting](https://kal-eficia.github.io/the-fix/sporting-press/) |

## How it's built

Each report is one Python file in `reports/`, holding its data and its text. `build.py` draws every chart as SVG from that data, in The Fix brand, and writes the site into `site/`. GitHub Actions builds and publishes it on every push. Standard library only.

```
python build.py
```

Brand: matchday programme. Paper `#E8E4DA`, ink `#121212`, one signal colour `#FF5A1F` that never changes, and the club colour for the focus team only. Archivo wide black for headlines, Instrument Serif Italic for the one human line, JetBrains Mono for numbers, labels and sources.

## Data

Event data is Opta's, read from public match centres (WhoScored, FotMob). Every figure on a page links to the source it came from. Only derived counts and positions are published, not raw feeds.

Code is MIT licensed. The Fix name and logo belong to Kalid Nur. Fonts are under the SIL Open Font License (see `site/assets/fonts/LICENCE.md`).
