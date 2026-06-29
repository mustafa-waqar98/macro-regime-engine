# Macro Regime Classification Engine

A systematic macro tool that pulls real economic data, classifies the
current US environment into one of four macro regimes, outputs an
asset-allocation signal (what to overweight / underweight), and backtests
that signal against history using point-in-time data.

## Why I'm Building This

I spent 3 years on an FX Sales desk watching macro events move markets
in real time. This project systematizes that intuition — translating
economic data into positioning signals, starting from first-principles
rule-based logic and building toward a historical backtest that's honest
about what was actually knowable at each decision date.

## What Works Today

- **Rule-based regime classifier.** Takes a PMI reading and a YoY CPI
  inflation rate, classifies into four regimes on a 2×2 of growth
  direction × inflation direction, and returns target over/underweights
  from a lookup table. Fully tested (hand-typed expected values).
- **Live FRED data pipeline.** Pulls CPI (`CPIAUCSL`) and converts it to
  a YoY inflation rate; pulls the PMI proxy. Network/secret-handling code
  is walled off from the pure classifier, which has no external deps.
- **Point-in-time vintage backtester.** Runs the classifier across
  2014–present using the FRED ALFRED API to fetch each month's CPI and
  PMI **as they were actually printed on that decision date** — revisions
  and publication lag included. No lookahead. Compares the strategy to a
  passive 60/40 benchmark.

### The honest result

| | Multiple (2014-03 → 2026-05) |
|---|---|
| Strategy (point-in-time, no lookahead) | **2.33x** |
| 60/40 benchmark | 3.02x |
| Strategy (revised data, *with* lookahead) | 2.52x |

This is the **first end-to-end backtest** — a deliberately simple v1:
binary level thresholds, equal-weight allocation, hard regime flips. It
underperforms passive 60/40 over this window (it spends time out of
equities through an equity bull decade and pays transition costs on every
flip), which is exactly the honest baseline to build from. The roadmap
below — a momentum axis, gradual rebalancing, risk-weighting — is aimed
at closing that gap.

The point of getting here first was an honest **measurement
infrastructure**, not a winning number. With that in place, the
**0.19x gap between the lookahead (2.52x) and point-in-time (2.33x) runs
is the lookahead bias, quantified** — the performance that disappears
once the backtest can only see what was knowable in real time. Every
future improvement gets scored against this same honest baseline.

### The four regimes

| Regime | Growth | Inflation | Overweight |
|---|---|---|---|
| Goldilocks | Expansion | Low (< 2.5%) | Equities, Credit |
| Inflationary Boom | Expansion | High (≥ 2.5%) | Commodities, TIPS |
| Stagflation | Contraction | High (≥ 2.5%) | Gold, Commodities |
| Risk-Off | Contraction | Low (< 2.5%) | Long Bonds, Gold, USD |

### A note on the PMI series

The classic ISM Manufacturing PMI was removed from FRED in 2016 over a
licensing dispute, and S&P Global's US PMI isn't served through the FRED
API either. This project uses the **NY Fed Empire State manufacturing
diffusion index** (`GACDISA066MSFRBNY`) as the best fetchable proxy — a
manufacturing survey that prints monthly and slightly ahead of CPI. It's
a **diffusion index centered on 0**, so the expansion/contraction split
is at 0, not the 50 of a conventional PMI.

The backtest window starts in **March 2014** because that's where FRED's
real-time vintage archive for this proxy begins — the backtest starts
where point-in-time data actually starts, rather than fabricating history
the model couldn't have seen.

## Planned

- **Momentum axis** (direction of travel, not just level) — the Greetham
  Investment Clock conversion. Identical PMI/CPI levels mean opposite
  things depending on whether they're accelerating or rolling over; the
  current level-only threshold is blind to this exactly at inflection
  points. Next up.
- **Allocation refinements** — gradual rebalancing vs. hard flips,
  vol/risk-weighting vs. equal dollars.
- **ML classification layer** — K-means clustering + PCA as a second,
  data-driven classifier to sit alongside the rule-based one, so the two
  approaches can be compared (does unsupervised clustering rediscover the
  hand-built regimes, or carve the space differently?).
- **Volatility regime overlay** — connect macro regimes to options
  positioning signals (Natenberg-inspired), mapping each regime to a
  vol stance.
- **Live dashboard** — Streamlit front end with the current regime, the
  historical heatmap, and the positioning signal.

## Tech

Python 3.13 · pandas · fredapi · yfinance · matplotlib · pytest · git

Planned: numpy, scikit-learn (ML layer), Streamlit (dashboard), Plotly (viz).

## Status

- **Phase 1** (foundations + rule-based classifier): **done.**
- **Phase 2** (live FRED data → point-in-time backtester): **done.**
- **Phase 3** (momentum axis + allocation refinements): **in progress.**