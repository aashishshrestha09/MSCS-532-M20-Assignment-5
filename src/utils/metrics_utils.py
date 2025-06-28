"""
metrics_utils.py
"""

import pandas as pd
from typing import Tuple


def generate_summaries(
    df: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Compute mean and standard deviation runtimes grouped by Algorithm, InputType, InputSize.

    Args:
        df: DataFrame with raw benchmark data.

    Returns:
        Tuple of (mean_df, std_df).
    """
    mean_df = (
        df.groupby(["Algorithm", "InputType", "InputSize"])["RuntimeSeconds"]
        .mean()
        .reset_index()
    )
    std_df = (
        df.groupby(["Algorithm", "InputType", "InputSize"])["RuntimeSeconds"]
        .std()
        .reset_index()
    )
    return mean_df, std_df


def calculate_speedup(
    mean_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Calculate speedup of randomized over deterministic Quicksort per InputType and InputSize.

    Args:
        mean_df: DataFrame with mean runtimes.

    Returns:
        DataFrame with columns: ['InputType', 'InputSize', 'Speedup']
    """
    det = mean_df[mean_df["Algorithm"] == "deterministic"].set_index(
        ["InputType", "InputSize"]
    )
    rand = mean_df[mean_df["Algorithm"] == "randomized"].set_index(
        ["InputType", "InputSize"]
    )

    speedup = det["RuntimeSeconds"] / rand["RuntimeSeconds"]
    speedup_df = speedup.reset_index().rename(columns={0: "Speedup"})
    speedup_df.columns = ["InputType", "InputSize", "Speedup"]
    return speedup_df
