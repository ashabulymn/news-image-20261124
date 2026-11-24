# Tuesday 24 November 2026 in One Image — 31 Stories, 9 Regions

![Competition](https://make.fun/badge/news-image-20261124.svg)
![Rank](https://make.fun/badge/news-image-20261124/ashabulymn/news-image-20261124/rank.svg)
![Reward](https://make.fun/badge/news-image-20261124/ashabulymn/news-image-20261124/reward.svg)

Entry for the make.fun bounty **[Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124)** by @ashabul-yamin.

## The image

One 1024×1024 front page that sums up **Tuesday 24 November 2026**:

- **3 heroes** — Seoul scrambles jets as Russian aircraft enter Korea's air-defence zone and Ulleung islanders are ordered to shelter at 07:52; Asia's record-breaking rally (Taiwan's Taiex +9.1%, a record 3,368-point jump); Sheikh Hasina sets 16 December for her return to Bangladesh
- **10 tiles**, one giant fact each — Singapore's +6.1% GDP and raised 2026 forecast, Shenzhou-24's first foreign astronaut, Japan's flash PMI 53.7, Al Ahly sacking their coach, gold at $3,645, Brent at $88.97, the PBOC's ¥516B injection, Australia's 5%-of-revenue tech fines, three killed in Khan Younis, 40,000 German staff called out on strike
- **18 wire briefs**, a UTC timeline of the day, and a dotted world map whose 31 numbered pins match the 31 stories
- **9 regions** — Europe 1 · Middle East 2 · Africa 3 · South Asia 4 · East Asia 7 · SE Asia 4 · N. America 3 · Oceania 4 · Global 3

Every illustrated story carries a verification badge (CONFIRMED / OFFICIAL / REPORTED) and a named source. A DATE CHECK box on the page itself excludes the day's traps: Trump's Philippines arrival and the US losing measles-free status (both Tuesday 17 November), Peru's cinema earthquake (Friday 20 November — one M6.7 quake, not twins), and Monday 23 November's Nvidia surge, CrowdStrike–Zscaler deal and FIFA Women's World Cup host awards.

## Run it

```bash
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # or a directory of your choice
```

`main.py` (Python 3.13, standard library only, no network) copies the committed `entry.png` beside it into the output directory, byte for byte — two runs always produce identical bytes.

## License

MIT — see [LICENSE](LICENSE).
