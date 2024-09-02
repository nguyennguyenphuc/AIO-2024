def display_missing_values(df):
    """
    Display missing values in the dataframe.

    Parameters:
    - df: pd.DataFrame, the dataframe to check

    Returns:
    - None
    """
    missing_values = df.isnull().sum()
    print("Missing values per column:")
    print(missing_values)


def rating_group(rating):
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'
