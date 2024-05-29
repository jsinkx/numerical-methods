import math

import numpy as np

x_arr = [2, 3, 4, 5]
f_arr = [7, 5, 8, 7]

def SLE(matrix):
    A = matrix[:, :-1]
    b = matrix[:, -1].reshape(-1, 1)
    
    return np.linalg.solve(A, b).tolist()

def least_squares_method(x_arr, f_arr, m, cb=SLE):
    matrix = []

    s_0 = len(x_arr)
    s_arr = [s_0]
    
    t_0 = sum(f_arr)
    t_arr = [t_0]
    
    for i in range(1, 2 * m + 1):
        x_values = [x**i for x in x_arr]
        s_arr.append(sum(x_values))
        
        if i <= math.ceil((m + 1) / 2) + 1:
            x_f_values = [x * f for x, f in zip(x_values, f_arr)]
            
            t_arr.append(sum(x_f_values))

    for i in range(m + 1):
        matrix.append([*s_arr[i:i+m+1], t_arr[i]])
        
    matrix = np.array(matrix, dtype='float64')

    return(cb(matrix))
        
print(least_squares_method(x_arr, f_arr, 1)) # -> [[5.700000000000004], [0.2999999999999991]]
print(least_squares_method(x_arr, f_arr, 2)) # -> [[8.449999999999905], [-1.4499999999999404], [0.24999999999999156]]