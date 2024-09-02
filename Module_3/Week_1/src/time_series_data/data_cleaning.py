# src/time_series_data/data_cleaning.py

import pandas as pd


def add_time_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add 'Year', 'Month', and 'Weekday' columns to the DataFrame based on the DateTime index.

    Parameters:
    df : pd.DataFrame
        The DataFrame to which time columns will be added.

    Returns:
    pd.DataFrame
        DataFrame with additional time-based columns.
    """
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df['Weekday'] = df.index.day_name()
    return df


def view_missing_values(df: pd.DataFrame) -> pd.Series:
    """
    Check and return the count of missing values for each column in the DataFrame.

    Parameters:
    df : pd.DataFrame
        The DataFrame to check for missing values.

    Returns:
    pd.Series
        A series containing the count of missing values for each column.
    """
    return df.isnull().sum()


def delete_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Delete rows with missing values from the DataFrame.

    Parameters:
    df : pd.DataFrame
        The DataFrame to clean.

    Returns:
    pd.DataFrame
        A cleaned DataFrame with rows containing missing values removed.
    """
    return df.dropna()


def fill_missing_values(df: pd.DataFrame, fill_value) -> pd.DataFrame:
    """
    Fill missing values in the DataFrame.

    Parameters:
    df : pd.DataFrame
        The DataFrame to fill.
    fill_value : scalar, dict, or Series
        Value to use to fill the missing values.

    Returns:
    pd.DataFrame
        DataFrame with missing values filled.
    """
    return df.fillna(fill_value)
