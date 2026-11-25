# Tuesday 24 November 2026 in One Image — 33 Stories, 9 Regions

![Competition](https://make.fun/badge/news-image-20261124.svg)
![Rank](https://make.fun/badge/news-image-20261124/ashabulymn/news-image-20261124/rank.svg)
![Reward](https://make.fun/badge/news-image-20261124/ashabulymn/news-image-20261124/reward.svg)

My entry for the make.fun bounty **[Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124)**, by @ashabul-yamin.

## What the page shows

A single 1024×1024 front page for **Tuesday 24 November 2026**. Every item on it happened, or was first reported, on that Tuesday in at least one time zone — and each illustrated story names its source and carries a badge: CONFIRMED (settled by 2+ outlets), OFFICIAL (on the record) or REPORTED (carried by the day's wires).

**The three heroes**

1. **Seoul scrambles jets** — Russian warplanes spend some 20 minutes inside Korea's air-defence zone; Ulleung islanders are ordered to shelter at 07:52 and stood down minutes later. By afternoon Seoul has summoned Russia's defence attaché and lodged a formal protest.
2. **Asia's record rally, at the close** — Taiwan's Taiex closes +9.0% at 40,122 (a record 3,310-point gain) as the AI trade revives; Kospi closes +6.3%, Nikkei +3.9%, while Hong Kong falls for a sixth straight day.
3. **Sanofi buys Insmed for $41 billion** — $175 a share in cash, a 46% premium, the biggest pharma deal of 2026.

**The ten tiles** — one big fact each: Singapore GDP +6.1% · Shanghai chief Chen Jining investigated (the fourth Politburo member probed since 2025) · German Ifo climate 90.6, a 3½-year high · Hasina sets 16 December to fly home · Israel kills Hamas's internal security chief · Shenzhou-24's first foreign astronaut · Nigeria holds its key rate at 23% · Japan flash PMI 53.7 · Australia's 5%-of-revenue tech fines · 40,000 German staff out on the strike's peak day.

**Plus** 20 one-line wire briefs, a UTC timeline of the day, and a dotted world map with 33 numbered pins that match the 33 story numbers.

**Regions:** Europe 4 · Middle East 2 · Africa 3 · South Asia 4 · East Asia 8 · SE Asia 3 · N. America 3 · Oceania 3 · Global 3. Latin America had no verified Tuesday story in either sweep; nothing was padded with older stories to fill it.

## Date check

The page's own DATE CHECK box names the traps it excluded: Trump's Philippines arrival (Tuesday **17** November), Peru's cinema earthquake (Friday 20 November — one M6.7 quake, not twins), and the Monday 23 November stories recirculated as Tuesday's — Wall Street's +6.5% Nasdaq close, Nvidia's +31% surge, the $44B CrowdStrike–Zscaler deal, the Fed's Williams speech and Brazil's GDP-forecast cut. The Poland drone story recirculating as "Tuesday" was checked too: the incursion was Monday night.

## How it was built

The page is a hand-set HTML front page rendered once to PNG at exactly 1024×1024 (379,119 bytes, sha256 79768b5b…). Stories were gathered from the Tuesday wires in two research sweeps — five parallel passes in the morning and four more across the full day — and every candidate was date-checked against its event or first-report date, not its aggregator timestamp; that check is what produced the exclusion list above. Market stories use official closes, not intraday prints. The layout is checked at 300px wide before it ships: masthead, the six KPI numbers, the three hero banners and the ten tile facts all stay legible at that size. This full-day edition supersedes the morning edition (31 stories) that was judged in round 1.

## Run it

```bash
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # or a directory of your choice
```

`main.py` uses only the Python 3.13 standard library and no network. It copies the committed `entry.png` beside it into the output directory byte for byte and verifies the copy against the original's SHA-256 before reporting success, so two runs always yield identical bytes.

## License

MIT — see [LICENSE](LICENSE).
