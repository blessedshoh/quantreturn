"""Tests for returns_toolkit.metrics."""
import numpy as np
import pandas as pd

from returns_toolkit.metrics import simple_returns, log_returns


def test_simple_returns_basic():
    prices = pd.Series([100.0, 110.0, 99.0])
    out = simple_returns(prices)
    # first is NaN, then +10%, then -10%
    assert np.isnan(out.iloc[0])
    assert np.isclose(out.iloc[1], 0.10)
    assert np.isclose(out.iloc[2], -0.10)


def test_log_returns_additive():
    # log returns sum to total log return over the period
    prices = pd.Series([100.0, 110.0, 121.0])
    out = log_returns(prices)
    total = np.log(prices.iloc[-1] / prices.iloc[0])
    assert np.isclose(out.iloc[1:].sum(), total)


def test_log_vs_simple_small_moves():
    # for tiny moves, log and simple returns nearly coincide
    prices = pd.Series([100.0, 100.5])
    assert np.isclose(simple_returns(prices).iloc[1],
                      log_returns(prices).iloc[1], atol=1e-4)
