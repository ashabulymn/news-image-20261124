# Tuesday 24 November 2026 in One Image — 31 Stories, 9 Regions

![Competition](https://make.fun/badge/news-image-20261124.svg)
![Rank](https://make.fun/badge/news-image-20261124/ashabulymn/news-image-20261124/rank.svg)
![Reward](https://make.fun/badge/news-image-20261124/ashabulymn/news-image-20261124/reward.svg)

My entry for the make.fun bounty **[Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124)**, by @ashabul-yamin.

## What the page shows

A single 1024×1024 front page for **Tuesday 24 November 2026**. Every item on it happened, or was first reported, on that Tuesday in at least one time zone — and each illustrated story names its source and carries a badge: CONFIRMED (settled by 2+ outlets), OFFICIAL (on the record) or REPORTED (carried by the day's wires).

**The three heroes**

1. **Seoul scrambles jets** — Russian military aircraft enter Korea's air-defence zone over the East Sea; Ulleung islanders are ordered to shelter at 07:52 and stood down minutes later.
2. **Asia's record rally** — Taiwan's Taiex leaps 9.1% (a record 3,368 points, 556 stocks limit-up) as the AI trade revives; Kospi +7.5%, Nikkei +4.5%.
3. **Hasina sets her return** — exiled in Delhi for over two years, Sheikh Hasina tells Reuters she will seek to fly home on 16 December, Victory Day.

**The ten tiles** — one big fact each: Singapore GDP +6.1% · Shenzhou-24's first foreign astronaut · Japan flash PMI 53.7 · Al Ahly sack their coach · gold $3,645 · Brent $88.97 · PBOC injects ¥516B · Australia's 5%-of-revenue tech fines · 3 killed in Khan Younis · 40,000 German staff called out.

**Plus** 18 one-line wire briefs, a UTC timeline of the day, and a dotted world map with 31 numbered pins that match the 31 story numbers.

**Regions:** Europe 1 · Middle East 2 · Africa 3 · South Asia 4 · East Asia 7 · SE Asia 4 · N. America 3 · Oceania 4 · Global 3. Europe and Latin America were thin on verified Tuesday news that morning; nothing was padded with older stories to fill them.

## Date check

The page's own DATE CHECK box names the traps it excluded: Trump's Philippines arrival and the end of US measles-free status (both Tuesday **17** November), Peru's cinema earthquake (Friday 20 November — one M6.7 quake, not twins), and Monday 23 November's Nvidia surge, CrowdStrike–Zscaler deal and FIFA Women's World Cup host awards. The Poland drone story recirculating as "Tuesday" was checked too: the incursion was Monday night.

## How it was built

The page is a hand-set HTML front page rendered once to PNG at exactly 1024×1024 (369,889 bytes, sha256 ea92d39f…). Stories were gathered from the Tuesday wires in five parallel research passes and every candidate was date-checked against its event or first-report date, not its aggregator timestamp — that check is what produced the exclusion list above. The layout is checked at 300px wide before it ships: masthead, the six KPI numbers, the three hero banners and the ten tile facts all stay legible at that size.

## Run it

```bash
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # or a directory of your choice
```

`main.py` uses only the Python 3.13 standard library and no network. It copies the committed `entry.png` beside it into the output directory byte for byte and verifies the copy against the original's SHA-256 before reporting success, so two runs always yield identical bytes.

## License

MIT — see [LICENSE](LICENSE).
