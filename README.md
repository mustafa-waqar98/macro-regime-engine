# Macro Regime Classification Engine

A systematic macro research tool that takes real economic data as inputs, classifies the current market environment into one of four macro regimes, and generates asset class positioning signals - displaying everything on a live interactive dashboard.

## What It Does

- Pulls real-time economic data from FRED (CPI, PMI, yield spreads, Fed Funds Rate) and market data from Yahoo Finance (SPY, TLT, GLD, GSG, TIP, UUP)
  - **SPY:** S&P 500 Equities
  - **TLT:** Long-term US Treasuries
  - **GLD:** Gold
  - **GSG:** Commodities basket
  - **TIP:** Treasury Inflation- Protected Securities
  - **UUP:** USD Index bullish exposure
- Classifies the current macro environment into one of these four regimes:
  - **Goldilocks** (PMI > 50, CPI < 2.5%) - Equities, Credit
  - **Inflationary Boom** (PMI < 50, CPI > 2.5%) - Commodities, TIPS
  - **Stagflation** (PMI < 50, CPI > 2.5%) - Gold, Commodities
  - **Risk-Off / Deflation** (PMI < 50, CPI < 2.5%) - Long Bonds, Gold, USD
  - Shows how each asset class has historically performed in each regime
  - Outputs a current positioning signal: what to overweight, what to underweight, and why
  - Two classification methods: rule-based (first principles) and K-means clustering (ML layer)
  - Vol regimes overlay connecting macro regimes to options positioning signals

## Why I'm Building This

I spent 3 years on an FX Sales desk watching macro events move markets in real time. This project is my attempt at systematizing that intuition - building a tool that translates economic data into actionable positioning signals using both fundamental logic and machine learning

## Tech

- Python - 3.13+
- pandas, numpy, fredapi, yfinance
- scikit-learn (ML layer)
- Streamlit (live dashboard)
- Plotly / Matplotlib (visualization)
- Data: FRED API + Yahoo Finance

## Project Status

| Phase | Description | Status |
|-------|-------------|--------|
| 1 | Python foundations + rule-based classifier (no libraries) | In Progress |
| 2 | Data pipeline (FRED + yfinance) | Upcoming |
| 3 | Regime classifier + heatmap + positioning signal | Upcoming |
| 4 | Streamlit dashboard (live URL) | Upcoming |
| 5 | ML layer (K-means + PCA) | Upcoming |
| 6 | Vol regime overlay (Natenberg-inspired) | Upcoming |

## Live Dashboard

*Streamlit Cloud URL*
