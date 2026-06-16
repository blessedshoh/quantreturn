"""Core return calculations. More metrics (vol, drawdown, Sharpe) land this week."""
from __future__ import annotations

import numpy as np
import pandas as pd


def simple_returns(prices: pd.Series) -> pd.Series:
    """Simple (arithmetic) returns: r_t = P_t / P_{t-1} - 1.

    The first value is NaN because there's no prior price.
    """
    return prices.pct_change()


def log_returns(prices: pd.Series) -> pd.Series:
    """Log returns: r_t = ln(P_t / P_{t-1}).

    Log returns are additive across time, which is why quants often prefer them.
    """
    return np.log(prices / prices.shift(1))
