def md_nre_single_sample(y, y_hat, n, p):
    """
    Calculate the Mean Difference of nth Root Error for a single sample.

    Parameters:
    y (float): The true value
    y_hat (float): The predicted value
    n (int): The root to be applied to y and y_hat
    p (int): The power to which the difference is raised

    Returns:
    float: The MD_nRE value
    """
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    difference = abs(y_root - y_hat_root)
    md_nre = difference ** p
    return md_nre


if __name__ == "__main__":
    # Testing the function using assertions
    assert round(md_nre_single_sample(100, 99.5, 2, 1), 4) == 0.0250
    assert round(md_nre_single_sample(50, 49.5, 2, 1), 4) == 0.0354
    assert round(md_nre_single_sample(20, 19.5, 2, 1), 4) == 0.0563
    assert round(md_nre_single_sample(0.6, 0.1, 2, 1), 4) == 0.4584

    print("All tests passed.")
