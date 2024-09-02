# src/time_series_data/data_analysis.py

import pandas as pd


def resample_data(df: pd.DataFrame, frequency: str) -> pd.DataFrame:
    """
    Resample the DataFrame to a specified frequency and aggregate values.

    Parameters:
    df : pd.DataFrame
        The DataFrame to resample.
    frequency : str
        The frequency to resample to (e.g., 'A' for annual).

    Returns:
    pd.DataFrame
        The resampled DataFrame.
    """
    return df.resample(frequency).sum()


def rolling_mean(df: pd.DataFrame, window: int) -> pd.DataFrame:
    """
    Calculate the rolling mean over a specified window.

    Parameters:
    df : pd.DataFrame
        The DataFrame to calculate rolling mean on.
    window : int
        The window size for rolling mean.

    Returns:
    pd.DataFrame
        DataFrame with rolling mean calculated only on numeric columns.
    """
    # Chỉ chọn các cột số
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    return numeric_df.rolling(window=window, center=True).mean()


def describe_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate descriptive statistics for the DataFrame.

    Parameters:
    df : pd.DataFrame
        The DataFrame to describe.

    Returns:
    pd.DataFrame
        The descriptive statistics.
    """
    return df.describe()
