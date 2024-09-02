import pandas as pd
import numpy as np


def check_missing_values(df):
    """
    Check for missing values in the dataframe.

    Parameters:
    - df: pd.DataFrame, the dataframe to check

    Returns:
    - pd.Series: Series with the count of missing values per column
    """
    return df.isnull().sum()


def drop_missing_values(df):
    """
    Drop rows with any missing values from the dataframe.

    Parameters:
    - df: pd.DataFrame, the dataframe to clean

    Returns:
    - pd.DataFrame: Cleaned dataframe with no missing values
    """
    return df.dropna()


def fill_missing_values(df):
    """
    Fill missing values in the dataframe.
    Numeric columns are filled with the mean, categorical columns are filled with 'Unknown'.

    Parameters:
    - df: pd.DataFrame, the dataframe to clean

    Returns:
    - pd.DataFrame: Cleaned dataframe with filled missing values
    """
    df_filled = df.copy()
    numeric_columns = df_filled.select_dtypes(include=[np.number]).columns
    df_filled[numeric_columns] = df_filled[numeric_columns].fillna(
        df[numeric_columns].mean())
    df_filled[df.select_dtypes(include=['object']).columns] = df_filled.select_dtypes(
        include=['object']).fillna('Unknown')
    return df_filled
