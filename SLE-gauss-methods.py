import numpy as np

# Define utils and main functions
def back(matrix):
    roots = []
    
    for i in range(len(matrix) -1, -1, -1):
        for j in range(i+1, len(matrix[i])-1):
            matrix[i][j] *= roots[::-1][j-i-1]
    
        solved = (matrix[i][i:][-1] - sum(matrix[i][i:][1:-1])) / matrix[i][i:][0] 
        roots.append(solved)
    
    return [*reversed(roots)]

def get_support_element(row, bias = 0):
    if row[bias] == 0:
        return get_support_element(row, bias + 1)
    return row[bias]

def forward_single_div(matrix):
    for i in range(len(matrix)):
        support_element = get_support_element(matrix[i])
        
        for t in range(len(matrix[i])):
            matrix[i][t] /= support_element
    
        if (len(matrix) != i+1):
            support_element_next = get_support_element(matrix[i+1])    
            
            for t in range(len(matrix[i + 1])):
                matrix[i + 1][t] -= matrix[i][t] * support_element_next
        else:
            for k in range(len(matrix) - 1):         
                support_element = get_support_element(matrix[i])
                
                for t in range(len(matrix[i])):
                    matrix[i][t] -= matrix[k][t] * support_element
        
    return matrix

def forward_excluded(matrix):
    n = len(matrix)
    
    for i in range(n - 1):
        divisor = matrix[i, i]
        matrix[i, :] /= divisor
        
        for j in range(i + 1, n):
            for k in range(i + 1, n + 1):
                matrix[j, k] -= matrix[j, i]*matrix[i, k]
                
            matrix[j, i] = 0
    
    last_divisor = matrix[-1, -2]
    matrix[-1, :] /= last_divisor
    
    return matrix

# Modification matrix with return statement
def select_leading_element(_matrix):
    for index in range(_matrix.shape[0]):
        matrix = _matrix.copy()
        _max = matrix[index:, index].flatten().argmax()
        t = matrix[index, :].copy()
        matrix[index, :], matrix[index + _max, :] = matrix[index + _max, :], t
        
    return matrix

# Testing on 3 matrices

# Single division method 
INIT_MATRIX_1 = np.array([
    [5, 0, 1, 11],
    [2, 6, -2, 8],
    [-3, 2, 10, 6]
], dtype='float64')

print(back(forward_single_div(INIT_MATRIX_1)))  # -> [2.0, 1.0, 1.0000000000000002]

# Excluded (triangle) method
INIT_MATRIX_2 = np.array([
    [2, 1, 4, 16],
    [3, 2, 1, 10],
    [1, 3, 3, 16],
], dtype='float64')

print(back(forward_excluded(INIT_MATRIX_2)))    # -> [1.0, 2.0, 3.0] 

INIT_MATRIX_3 = np.array([
    [-3, 2.099, 6, 3.901],
    [10, -7, 0, 7],
    [5, -1, 5, -6]
], dtype='float64')

# The Gauss method with the choice of the leading element
print(back(forward_excluded(select_leading_element(INIT_MATRIX_3)))) # -> [-3.35888037320883, -5.798400533155473, 0.9992002665778078]