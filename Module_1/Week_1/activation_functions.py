import math


def is_number(n):
    """
    Check if the input is a number.

    Parameters:
    n: The input to check

    Returns:
    bool: True if n is a number, False otherwise
    """
    return isinstance(n, float)


def sigmoid(x):
    """
    Compute the sigmoid activation function.

    Parameters:
    x (float): The input value

    Returns:
    float: The output of the sigmoid function
    """
    return 1 / (1 + math.exp(-x))


def relu(x):
    """
    Compute the ReLU activation function.

    Parameters:
    x (float): The input value

    Returns:
    float: The output of the ReLU function
    """
    return max(0, x)


def elu(x, alpha=0.01):
    """
    Compute the ELU activation function.

    Parameters:
    x (float): The input value
    alpha (float): The alpha value for ELU, default is 0.01

    Returns:
    float: The output of the ELU function
    """
    return x if x > 0 else alpha * (math.exp(x) - 1)


def calculate_activation_function(x, activation_function):
    """
    Calculate the specified activation function.

    Parameters:
    x: The input value
    activation_function (str): The name of the activation function ('sigmoid', 'relu', 'elu')

    Returns:
    float: The result of the activation function or None if the input is invalid
    """
    if not is_number(x):
        print("x must be a number")
        return None

    x = float(x)

    if activation_function == 'sigmoid':
        result = sigmoid(x)
    elif activation_function == 'relu':
        result = relu(x)
    elif activation_function == 'elu':
        result = elu(x)
    else:
        print(f"{activation_function} is not supported")
        return None

    return result


# Example usage
if __name__ == "__main__":
    # Testing the function using assertions
    assert math.isclose(calculate_activation_function(
        1.5, 'sigmoid'), 0.8175744761936437)
    assert calculate_activation_function('abc', 'sigmoid') is None
    assert calculate_activation_function(1.5, 'belu') is None
    assert calculate_activation_function(3, 'relu') == 3
    assert calculate_activation_function(-1, 'relu') == 0
    assert calculate_activation_function(1, 'elu') == 1
    assert math.isclose(calculate_activation_function(-1,
                        'elu'), -0.009516258196404042)

    print("All tests passed.")
