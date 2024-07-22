
# Cosine Similarity

Để giải bài toán tính Cosine Similarity $ \text{cs}(x, y) $ cho các vector $ x $ và $ y $ đã cho, chúng ta cần thực hiện các bước sau:

1. Tính tích vô hướng của hai vector $ x $ và $ y $.
2. Tính độ dài (norm) của từng vector.
3. Tính Cosine Similarity theo công thức:

$ 
\text{cs}(x, y) = \frac{x \cdot y}{\| x \| \| y \|} = \frac{\sum_{i=1}^N x_i y_i}{\sqrt{\sum_{i=1}^N x_i^2} \sqrt{\sum_{i=1}^N y_i^2}} 
$

Vector $ x $ và $ y $ đã cho:

$
x = \begin{bmatrix}
1 \\
2 \\
3 \\
4 
\end{bmatrix}, \quad y = \begin{bmatrix}
1 \\
0 \\
3 \\
0 
\end{bmatrix} 
$

### Bước 1: Tính tích vô hướng của hai vector $ x $ và $ y $

$ 
x \cdot y = 1 \cdot 1 + 2 \cdot 0 + 3 \cdot 3 + 4 \cdot 0 = 1 + 0 + 9 + 0 = 10 
$

### Bước 2: Tính độ dài của từng vector

$ 
\| x \| = \sqrt{1^2 + 2^2 + 3^2 + 4^2} = \sqrt{1 + 4 + 9 + 16} = \sqrt{30} 
$

$ 
\| y \| = \sqrt{1^2 + 0^2 + 3^2 + 0^2} = \sqrt{1 + 0 + 9 + 0} = \sqrt{10} 
$

### Bước 3: Tính Cosine Similarity

$ 
\text{cs}(x, y) = \frac{10}{\sqrt{30} \cdot \sqrt{10}} = \frac{10}{\sqrt{300}} = \frac{10}{10\sqrt{3}} = \frac{1}{\sqrt{3}} \approx 0.577 
$
