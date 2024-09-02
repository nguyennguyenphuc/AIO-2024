import pandas as pd

def load_data(file_path):
    """
    Load the IMDB movie dataset from a CSV file.
    
    Parameters:
    - file_path: str, path to the CSV file
    
    Returns:
    - pd.DataFrame: Loaded dataframe
    """
    df = pd.read_csv(file_path)
    return df

def view_data(df, num_rows=5):
    """
    Display the first few rows of the dataframe.
    
    Parameters:
    - df: pd.DataFrame, the dataframe to display
    - num_rows: int, number of rows to display (default is 5)
    
    Returns:
    - None
    """
    print(df.head(num_rows))
