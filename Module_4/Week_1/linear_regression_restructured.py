from Module_4.Week_1.prepare_data import get_column
import numpy as np

def prepare_data(file_name_dataset):
    """Prepare dataset with added feature column x0 for linear regression."""
    data = np.genfromtxt(file_name_dataset, delimiter=',', skip_header=1).tolist()
    tv_data, radio_data, newspaper_data, sales_data = [get_column(data, i) for i in range(4)]
    X = [[1, x1, x2, x3] for x1, x2, x3 in zip(tv_data, radio_data, newspaper_data)]
    return X, sales_data

def predict(X_features, weights):
    """Predict output using y = x0 * b + x1 * w1 + x2 * w2 + x3 * w3."""
    return sum(x * w for x, w in zip(X_features, weights))
