import numpy as np

def prepare_matrix(matrix):
    A = matrix[:, :-1]
    b = matrix[:, -1].reshape(-1, 1)
    
    return A, b

def LUDecomposition(matrix, rightPart):
    n = len(matrix)
    lu = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            sum_val = 0
            for k in range(i):
                sum_val += lu[i, k] * lu[k, j]
            lu[i, j] = matrix[i, j] - sum_val
        for j in range(i + 1, n):
            sum_val = 0
            for k in range(i):
                sum_val += lu[j, k] * lu[k, i]
            lu[j, i] = (matrix[j, i] - sum_val) / lu[i, i]

    y = np.zeros(n)
    for i in range(n):
        sum_val = 0
        for k in range(i):
            sum_val += lu[i, k] * y[k]
        y[i] = rightPart[i] - sum_val

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_val = 0
        for k in range(i + 1, n):
            sum_val += lu[i, k] * x[k]
        x[i] = (y[i] - sum_val) / lu[i, i]

    return x

A_1, b_1 = prepare_matrix(np.array([
    [5, 0, 1, 11],
    [2, 6, -2, 8],
    [-3, 2, 10, 6]
], dtype='float64'))

A_2, b_2 = prepare_matrix(np.array([
    [2, 1, 4, 16],
    [3, 2, 1, 10],
    [1, 3, 3, 16],
], dtype='float64'))

A_3, b_3 = prepare_matrix(np.array([
    [-3, 2.099, 6, 3.901],
    [10, -7, 0, 7],
    [5, -1, 5, -6]
], dtype='float64'))

print(" ".join(map(str, LUDecomposition(A_1, b_1)))) # -> 2.0 1.0 1.0
print(" ".join(map(str, LUDecomposition(A_2, b_2)))) # -> 1.0 2.0 3.0
print(" ".join(map(str, LUDecomposition(A_3, b_3)))) # -> -3.3588803732091357 -5.798400533155909 0.9992002665778078
