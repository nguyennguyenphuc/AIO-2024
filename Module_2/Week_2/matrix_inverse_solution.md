# Tìm ma trận nghịch đảo  $A^{-1} $

Để giải bài toán tìm ma trận nghịch đảo $ A^{-1} $cho ma trận $ A $đã cho, chúng ta cần thực hiện các bước sau:

1. Tính định thức của ma trận $ A $.
2. Xác định ma trận phụ hợp của $ A $.
3. Tính ma trận nghịch đảo $ A^{-1} $ theo công thức $ A^{-1} = \frac{1}{\text{det}(A)} \text{adj}(A) $ .

Ma trận $ A $đã cho:

$
A = \begin{bmatrix}
-2 & 6 \\
8 & -4 
\end{bmatrix} 
$

### Bước 1: Tính định thức của ma trận $ A $

Định thức của ma trận $ A $được tính như sau:

$
\text{det}(A) = (-2) \cdot (-4) - 6 \cdot 8 = 8 - 48 = -40 
$

### Bước 2: Xác định ma trận phụ hợp của $ A $

Ma trận phụ hợp của $ A $là ma trận mà các phần tử được thay đổi vị trí và dấu như sau:

$
\text{adj}(A) = \begin{bmatrix}
d & -b \\
-c & a 
\end{bmatrix} 
= \begin{bmatrix}
-4 & -6 \\
-8 & -2 
\end{bmatrix} 
$

### Bước 3: Tính ma trận nghịch đảo $ A^{-1} $

Ma trận nghịch đảo $ A^{-1} $được tính theo công thức:

$
A^{-1} = \frac{1}{\text{det}(A)} \text{adj}(A) 
= \frac{1}{-40} \begin{bmatrix}
-4 & -6 \\
-8 & -2 
\end{bmatrix} 
= \begin{bmatrix}
\frac{-4}{-40} & \frac{-6}{-40} \\
\frac{-8}{-40} & \frac{-2}{-40} 
\end{bmatrix} 
= \begin{bmatrix}
\frac{1}{10} & \frac{3}{20} \\
\frac{1}{5} & \frac{1}{20} 
\end{bmatrix} 
$

Vậy, ma trận nghịch đảo $ A^{-1} $của ma trận $ A $đã cho là:

$
A^{-1} = \begin{bmatrix}
0.1 & 0.15 \\
0.2 & 0.05 
\end{bmatrix} 
$

### Kết quả

Ma trận nghịch đảo của ma trận $ A $là:

$
A^{-1} = \begin{bmatrix}
0.1 & 0.15 \\
0.2 & 0.05 
\end{bmatrix} 
$

Trên đây là toàn bộ các bước và kết quả tính toán ma trận nghịch đảo của ma trận $ A $theo lược đồ 1.5.
