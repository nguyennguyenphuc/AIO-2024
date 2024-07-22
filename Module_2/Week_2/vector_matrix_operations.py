import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum(np.square(vector)))
    return len_of_vector


def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result


def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result


def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result

# Test cases


def test_compute_vector_length():
    vector = np.array([1, 2, 3])
    expected_length = np.sqrt(1**2 + 2**2 + 3**2)
    assert np.isclose(compute_vector_length(vector), expected_length), f"Expected {
        expected_length}, got {compute_vector_length(vector)}"


def test_compute_dot_product():
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])
    expected_dot_product = 1*4 + 2*5 + 3*6
    assert np.isclose(compute_dot_product(vector1, vector2), expected_dot_product), f"Expected {
        expected_dot_product}, got {compute_dot_product(vector1, vector2)}"


def test_matrix_multi_vector():
    matrix = np.array([[1, 2], [3, 4]])
    vector = np.array([5, 6])
    expected_result = np.dot(matrix, vector)
    assert np.allclose(matrix_multi_vector(matrix, vector), expected_result), f"Expected {
        expected_result}, got {matrix_multi_vector(matrix, vector)}"


def test_matrix_multi_matrix():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected_result = np.dot(matrix1, matrix2)
    assert np.allclose(matrix_multi_matrix(matrix1, matrix2), expected_result), f"Expected {
        expected_result}, got {matrix_multi_matrix(matrix1, matrix2)}"


def test_inverse_matrix():
    matrix = np.array([[1, 2], [3, 4]])
    expected_result = np.linalg.inv(matrix)
    assert np.allclose(inverse_matrix(matrix), expected_result), f"Expected {
        expected_result}, got {inverse_matrix(matrix)}"


# Run test cases
if __name__ == "__main__":
    test_compute_vector_length()
    test_compute_dot_product()
    test_matrix_multi_vector()
    test_matrix_multi_matrix()
    test_inverse_matrix()
    print("All tests passed!")
