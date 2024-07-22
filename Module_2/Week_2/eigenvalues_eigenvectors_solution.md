# Eigenvector và Eigenvalue

Để giải bài toán tìm Eigenvector (v) đã được normalize và eigenvalue $ \lambda $ của ma trận $ A $, chúng ta cần thực hiện các bước sau:

1. Tính toán các eigenvalue của ma trận $ A $.
2. Tính toán các eigenvector tương ứng.
3. Normalize các eigenvector.

Ma trận $ A $ đã cho:

$ 
A = \begin{bmatrix}
0.9 & 0.2 \\
0.1 & 0.8 
\end{bmatrix} 
$

### Bước 1: Tính toán các eigenvalue của ma trận $ A $

Các eigenvalue của ma trận $ A $ được tính bằng cách giải phương trình đặc trưng:

$ 
\text{det}(A - \lambda I) = 0 
$

### Bước 2: Tính toán các eigenvector tương ứng

Eigenvector (v) tương ứng với eigenvalue $ \lambda $ được tính từ:

$ 
(A - \lambda I)v = 0 
$

### Bước 3: Normalize các eigenvector

Eigenvector (v) được normalize như sau:

$ 
\frac{v}{\|v\|}, \quad v_i = \frac{v_i}{\sqrt{\sum_{i=1}^{n} v_i^2}}
$

### Thực hiện tính toán bằng Python

```python
import numpy as np

def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    normalized_eigenvectors = eigenvectors / np.linalg.norm(eigenvectors, axis=0)
    return eigenvalues, normalized_eigenvectors

A = np.array([[0.9, 0.2],
              [0.1, 0.8]])

eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(A)
print("Eigenvalues:", eigenvalues)
print("Normalized Eigenvectors:\n", eigenvectors)
