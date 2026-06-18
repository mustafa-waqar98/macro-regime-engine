# Macro Regime Classification Engine

A systematic macro tool that pulls real economic data, classifies the
current US environment into one of four macro regimes, and outputs an
asset-allocation signal (what to overweight / underweight).

## Why I'm Building This

I spent 3 years on an FX Sales desk watching macro events move markets
in real time. This project systematizes that intuition — translating
economic data into positioning signals, starting from first-principles
rule-based logic and building toward a historical backtest.

## What Works Today

- **Rule-based regime classifier.** Takes a PMI reading and a YoY CPI
  inflation rate, classifies into four regimes on a 2×2 of growth
  direction × inflation direction, and returns target over/underweights
  from a lookup table. Fully tested (hand-typed expected values).
- **Live FRED data pipeline.** Pulls CPI (`CPIAUCSL`) and converts it to
  a YoY inflation rate; pulls the PMI proxy. Network/secret-handling code
  is walled off from the pure classifier, which has no external deps.

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

## Planned

- **Backtester** — run the classifier across decades of history and score
  how the allocation rules would have performed. (The headline goal.)
- Momentum axis (direction of travel, not just level) — the Greetham Investment Clock conversion.
- Point-in-time data handling so backtests don't use revised figures the past couldn't have seen.

- **ML classification layer** — K-means clustering + PCA as a second,
data-driven classifier to sit alongside the rule-based one, so the two
approaches can be compared (does unsupervised clustering rediscover the
hand-built regimes, or carve the space differently?).
- **Volatility regime overlay** — connect macro regimes to options
positioning signals (Natenberg-inspired), mapping each regime to a
vol stance.
- **Live dashboard** — Streamlit front end with the current regime, the historical heatmap, and the positioning signal.

## Tech

Python 3.13 · pandas · fredapi · git

Planned: numpy, scikit-learn (ML layer), Streamlit (dashboard),
Plotly/Matplotlib (viz), yfinance (asset return data for the backtester).

## Status

Phase 1 (foundations + rule-based classifier): **done.**
Phase 2 (live FRED data → backtester): **in progress.**