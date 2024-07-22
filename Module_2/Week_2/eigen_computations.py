import numpy as np


def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


def test_compute_eigenvalues_eigenvectors():
    # Test case 1: 2x2 matrix
    matrix1 = np.array([[1, 2], [2, 1]])
    eigenvalues1, eigenvectors1 = compute_eigenvalues_eigenvectors(matrix1)
    print("Test case 1:")
    print("Matrix:")
    print(matrix1)
    print("Eigenvalues:", eigenvalues1)
    print("Eigenvectors:")
    print(eigenvectors1)
    print()

    # Test case 2: 3x3 matrix
    matrix2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    eigenvalues2, eigenvectors2 = compute_eigenvalues_eigenvectors(matrix2)
    print("Test case 2:")
    print("Matrix:")
    print(matrix2)
    print("Eigenvalues:", eigenvalues2)
    print("Eigenvectors:")
    print(eigenvectors2)
    print()


if __name__ == "__main__":
    test_compute_eigenvalues_eigenvectors()
