"""
model_forecast.py

Dengue forecasting model module.

This module exposes generate_forecast(), which the API server calls to
retrieve predictions from the pre-trained SARIMA / autoregressive model.

NOTE: The statistical model implementation below is a representative
placeholder.  Replace the body of generate_forecast() with your own
trained-model loading / inference code without changing the public
interface (function name or return structure).
"""

from __future__ import annotations

import datetime
from dataclasses import dataclass


@dataclass
class ForecastResult:
    """Structured container returned by generate_forecast()."""

    predicted_cases: float
    lower_bound: float
    upper_bound: float


def generate_forecast() -> ForecastResult:
    """Run the dengue forecasting model and return next-month predictions.

    Returns
    -------
    ForecastResult
        A dataclass with three fields:
        - predicted_cases : point-forecast for the next month
        - lower_bound     : lower edge of the 95 % confidence interval
        - upper_bound     : upper edge of the 95 % confidence interval

    Notes
    -----
    Swap the placeholder arithmetic below for your real model inference,
    for example::

        import pickle, pandas as pd
        with open("dengue_sarima.pkl", "rb") as fh:
            model = pickle.load(fh)
        forecast = model.get_forecast(steps=1)
        summary  = forecast.summary_frame(alpha=0.05)
        predicted = float(summary["mean"].iloc[0])
        lower     = float(summary["mean_ci_lower"].iloc[0])
        upper     = float(summary["mean_ci_upper"].iloc[0])
        return ForecastResult(predicted, lower, upper)
    """
    # --- placeholder: deterministic values derived from the current date ---
    # Replace this section with real model inference.
    base = 120.0 + (datetime.date.today().month * 5.0)
    predicted_cases = round(base, 2)
    lower_bound = round(base * 0.80, 2)
    upper_bound = round(base * 1.20, 2)
    # ----------------------------------------------------------------------

    return ForecastResult(
        predicted_cases=predicted_cases,
        lower_bound=lower_bound,
        upper_bound=upper_bound,
    )
