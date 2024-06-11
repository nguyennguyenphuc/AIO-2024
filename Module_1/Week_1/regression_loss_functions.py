import random
import math


def calculate_mae(predictions, targets):
    """
    Calculate Mean Absolute Error (MAE).

    Parameters:
    predictions (list): List of predicted values
    targets (list): List of target values

    Returns:
    float: The MAE value
    """
    n = len(predictions)
    mae = sum(abs(p - t) for p, t in zip(predictions, targets)) / n
    return mae


def calculate_mse(predictions, targets):
    """
    Calculate Mean Squared Error (MSE).

    Parameters:
    predictions (list): List of predicted values
    targets (list): List of target values

    Returns:
    float: The MSE value
    """
    n = len(predictions)
    mse = sum((p - t) ** 2 for p, t in zip(predictions, targets)) / n
    return mse


def calculate_rmse(predictions, targets):
    """
    Calculate Root Mean Squared Error (RMSE).

    Parameters:
    predictions (list): List of predicted values
    targets (list): List of target values

    Returns:
    float: The RMSE value
    """
    mse = calculate_mse(predictions, targets)
    rmse = math.sqrt(mse)
    return rmse


def generate_random_samples(num_samples):
    """
    Generate random predictions and targets.

    Parameters:
    num_samples (int): Number of samples

    Returns:
    tuple: Lists of predictions and targets
    """
    predictions = [random.uniform(0, 10) for _ in range(num_samples)]
    targets = [random.uniform(0, 10) for _ in range(num_samples)]
    return predictions, targets


if __name__ == "__main__":
    # Testing the function using assertions
    predictions, targets = generate_random_samples(5)

    assert calculate_mae(predictions, targets) == sum(abs(p - t)
                                                      for p, t in zip(predictions, targets)) / 5
    assert calculate_mse(predictions, targets) == sum(
        (p - t) ** 2 for p, t in zip(predictions, targets)) / 5
    assert calculate_rmse(predictions, targets) == math.sqrt(
        sum((p - t) ** 2 for p, t in zip(predictions, targets)) / 5)

    # Check for non-numeric sample input
    try:
        generate_random_samples("five")
    except ValueError:
        print("number of samples must be an integer number")

    print("All tests passed.")
