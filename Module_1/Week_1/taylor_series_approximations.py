import math


def factorial(n):
    """
    Calculate the factorial of a number.

    Parameters:
    n (int): The number to calculate the factorial for

    Returns:
    int: The factorial of the number
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def approx_sin(x, n):
    """
    Approximate sin(x) using the Taylor series expansion.

    Parameters:
    x (float): The input value in radians
    n (int): The number of terms in the Taylor series

    Returns:
    float: The approximated value of sin(x)
    """
    result = 0
    for i in range(n):
        term = (-1)**i * (x**(2*i + 1)) / factorial(2*i + 1)
        result += term
    return result


def approx_cos(x, n):
    """
    Approximate cos(x) using the Taylor series expansion.

    Parameters:
    x (float): The input value in radians
    n (int): The number of terms in the Taylor series

    Returns:
    float: The approximated value of cos(x)
    """
    result = 0
    for i in range(n):
        term = (-1)**i * (x**(2*i)) / factorial(2*i)
        result += term
    return result


def approx_sinh(x, n):
    """
    Approximate sinh(x) using the Taylor series expansion.

    Parameters:
    x (float): The input value in radians
    n (int): The number of terms in the Taylor series

    Returns:
    float: The approximated value of sinh(x)
    """
    result = 0
    for i in range(n):
        term = (x**(2*i + 1)) / factorial(2*i + 1)
        result += term
    return result


def approx_cosh(x, n):
    """
    Approximate cosh(x) using the Taylor series expansion.

    Parameters:
    x (float): The input value in radians
    n (int): The number of terms in the Taylor series

    Returns:
    float: The approximated value of cosh(x)
    """
    result = 0
    for i in range(n):
        term = (x**(2*i)) / factorial(2*i)
        result += term
    return result


if __name__ == "__main__":
    # Testing the functions using assertions
    assert round(approx_sin(3.14, 10), 4) == 0.0016
    assert round(approx_cos(3.14, 10), 4) == -0.9999
    assert round(approx_sinh(3.14, 10), 4) == 11.5487
    assert round(approx_cosh(3.14, 10), 4) == 11.5919

    print("All tests passed.")
