import math


def is_integer(value):
    """
    Check if the value is an integer.

    Parameters:
    value: The value to check

    Returns:
    bool: True if value is an integer, False otherwise
    """
    return isinstance(value, int)


def are_greater_than_zero(*values):
    """
    Check if all values are greater than zero.

    Parameters:
    *values: Variable number of values to check

    Returns:
    bool: True if all values are greater than zero, False otherwise
    """
    return all(value > 0 for value in values)


def calculate_f1_score(tp, fp, fn):
    """
    Calculate F1-Score for a classification model.

    Parameters:
    tp (int): True Positives
    fp (int): False Positives
    fn (int): False Negatives

    Returns:
    float: F1-Score or None if the input values are invalid
    """

    if not is_integer(tp):
        print("tp must be int")
        return None
    if not is_integer(fp):
        print("fp must be int")
        return None
    if not is_integer(fn):
        print("fn must be int")
        return None

    if not are_greater_than_zero(tp, fp, fn):
        print("tp and fp and fn must be greater than zero")
        return None

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)

    return f1_score


if __name__ == "__main__":
    # Testing the function using assertions
    assert math.isclose(calculate_f1_score(2, 3, 4), 0.3636363636363636)
    assert calculate_f1_score('a', 3, 4) is None
    assert calculate_f1_score(2, 'a', 4) is None
    assert calculate_f1_score(2, 3, 'a') is None
    assert calculate_f1_score(2, 3, 0) is None
    assert calculate_f1_score(2.1, 3, 4) is None

    print("All tests passed.")
