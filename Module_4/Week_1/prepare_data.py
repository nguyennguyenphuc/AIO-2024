import numpy as np

def get_column(data, index):
    """Retrieve a specific column from the data by index."""
    result = [row[index] for row in data]
    return result

def prepare_data(file_name_dataset):
    """Prepare dataset by splitting into input X and output y."""
    data = np.genfromtxt(file_name_dataset, delimiter=',', skip_header=1).tolist()
    tv_data = get_column(data, 0)
    radio_data = get_column(data, 1)
    newspaper_data = get_column(data, 2)
    sales_data = get_column(data, 3)
    X = [tv_data, radio_data, newspaper_data]
    y = sales_data
    return X, y
