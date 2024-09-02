import pandas as pd

def select_columns(df, columns):
    """
    Select specific columns from the dataframe.
    
    Parameters:
    - df: pd.DataFrame, the dataframe to select from
    - columns: list of str, columns to select
    
    Returns:
    - pd.DataFrame: Dataframe with selected columns
    """
    return df[columns]

def filter_data(df, condition):
    """
    Filter the dataframe based on a condition.
    
    Parameters:
    - df: pd.DataFrame, the dataframe to filter
    - condition: boolean condition for filtering
    
    Returns:
    - pd.DataFrame: Filtered dataframe
    """
    return df[condition]

def group_by_column(df, group_column, agg_column, agg_func='mean'):
    """
    Group the dataframe by a column and aggregate another column.
    
    Parameters:
    - df: pd.DataFrame, the dataframe to group
    - group_column: str, the column to group by
    - agg_column: str, the column to aggregate
    - agg_func: str, aggregation function ('mean', 'sum', etc.)
    
    Returns:
    - pd.DataFrame: Grouped and aggregated dataframe
    """
    return df.groupby(group_column)[agg_column].agg(agg_func).reset_index()

def sort_data(df, sort_column, ascending=True):
    """
    Sort the dataframe by a specific column.
    
    Parameters:
    - df: pd.DataFrame, the dataframe to sort
    - sort_column: str, the column to sort by
    - ascending: bool, sort in ascending order (default is True)
    
    Returns:
    - pd.DataFrame: Sorted dataframe
    """
    return df.sort_values(by=sort_column, ascending=ascending)

def apply_custom_function(df, func, new_column_name):
    """
    Apply a custom function to the dataframe and create a new column.
    
    Parameters:
    - df: pd.DataFrame, the dataframe to apply the function to
    - func: function, the function to apply to each row
    - new_column_name: str, the name of the new column
    
    Returns:
    - pd.DataFrame: Dataframe with the new column
    """
    df[new_column_name] = df.apply(func, axis=1)
    return df
