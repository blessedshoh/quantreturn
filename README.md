# quant-returns-toolkit

A small, tested Python library for the core return & risk analytics every quant uses:
log/simple returns, rolling volatility, drawdown, and risk-adjusted ratios (Sharpe, Sortino, Calmar).

> Project 1 of an 8-project quant research portfolio. Built to be reusable, tested, and reproducible — not a notebook dump.

## Status
🚧 Week 1 — scaffold + first tested function. Returns/vol/Sharpe/drawdown landing this week.

## Install
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Quick start
```python
import pandas as pd
from returns_toolkit.metrics import simple_returns, log_returns

prices = pd.Series([100, 101, 99, 103])
print(simple_returns(prices))
print(log_returns(prices))
```

## Run tests
```bash
pytest
```

## Layout
```
src/returns_toolkit/   library code
notebooks/             exploratory analysis
tests/                 pytest tests
```

## Limitations / honest notes
To be filled in as the toolkit grows — e.g., assumptions about trading-day count for annualization, handling of missing data, and why naive Sharpe can mislead.
