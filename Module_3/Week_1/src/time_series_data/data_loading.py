# src/time_series_data/data_loading.py

import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load time series data from a CSV file.

    Parameters:
    filepath : str
        The path to the CSV file.

    Returns:
    pd.DataFrame
        The loaded time series DataFrame.
    """
    return pd.read_csv(filepath, parse_dates=True, index_col=0)
