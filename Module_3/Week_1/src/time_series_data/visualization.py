# src/time_series_data/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns


def plot_time_series(df, column, title, ylabel):
    """
    Plot a time series data.

    Parameters:
    df : pd.DataFrame
        The DataFrame containing the time series data.
    column : str
        The column to plot.
    title : str
        The title of the plot.
    ylabel : str
        The label for the y-axis.

    Returns:
    None
    """
    sns.set(rc={'figure.figsize': (11, 4)})
    df[column].plot(linewidth=0.5)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.show()


def plot_seasonality(df):
    """
    Plot seasonality boxplots for Consumption, Solar, and Wind.

    Parameters:
    df : pd.DataFrame
        The DataFrame containing the time series data.

    Returns:
    None
    """
    _, axes = plt.subplots(3, 1, figsize=(11, 10), sharex=True)
    for name, ax in zip(['Consumption', 'Solar', 'Wind'], axes):
        sns.boxplot(data=df, x='Month', y=name, ax=ax)
        ax.set_ylabel('GWh')
        ax.set_title(name)
    plt.show()


def plot_trends(df, original_col, rolling_col_7d, rolling_col_365d):
    """
    Plot original and rolling mean trends in a time series.

    Parameters:
    df : pd.DataFrame
        The DataFrame containing the time series data.
    original_col : str
        The column for original data.
    rolling_col_7d : str
        The column for 7-day rolling mean data.
    rolling_col_365d : str
        The column for 365-day rolling mean data.

    Returns:
    None
    """
    import matplotlib.dates as mdates

    _, ax = plt.subplots()
    ax.plot(df[original_col], marker='.', markersize=2,
            color='0.6', linestyle='None', label='Daily')
    ax.plot(df[rolling_col_7d], linewidth=2, label='7-d Rolling Mean')
    ax.plot(df[rolling_col_365d], color='0.2', linewidth=3,
            label='Trend (365-d Rolling Mean)')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.legend()
    ax.set_xlabel('Year')
    ax.set_ylabel('Consumption (GWh)')
    ax.set_title('Trends in Electricity Consumption')
    plt.show()
