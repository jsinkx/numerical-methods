import numpy as np 

import math 

def stop_criterion(element, eps=1e-3):
    return abs(element) < eps

def get_max_abs_element(matrix):
    max_element = None
    
    for i in range(matrix.shape[0]):
        for j in range(i + 1, matrix.shape[1]):
            if max_element is None or matrix[i][j] > max_element:
                max_element = matrix[i][j]
    
    return max_element

def get_rotation_matrix(matrix, phi):
        sin_phi = math.sin(phi) 
        cos_phi = math.cos(phi) 
        
        if matrix.shape[0] == 2:
            matrix_H = np.array([
                [cos_phi, -sin_phi], 
                [sin_phi, cos_phi]
            ])
        else: 
            matrix_H = np.array([
                [cos_phi, 0, -sin_phi],
                [0, 1, 0],
                [sin_phi, 0, cos_phi]
            ])
            
        return matrix_H
    
def rotation_method(matrix_A, ep=1e-3):
    result = [[], []] # [eigen_values, eigen_vectors]
    
    while not stop_criterion(get_max_abs_element(matrix_A)):
        i = 1 
        j = matrix_A.shape[1]
        
        # step 2
        element = get_max_abs_element(matrix_A)
            
        # step 3    
        phi_arg = 2 * element / (matrix_A[i - 1][i - 1] - matrix_A[j - 1][j - 1])
        phi = 1/2 * math.atan(phi_arg)

        # step 4
        matrix_H = get_rotation_matrix(matrix_A, phi)              # for eigen vectors
        matrix_A = np.dot(matrix_H.T, np.dot(matrix_A, matrix_H))  # for eigen values
        
        vectors = []
        
        for vector_index in range(matrix_H.shape[1]):
            vectors.append(matrix_H.T[vector_index])
        
        result = [matrix_A.diagonal(), vectors]
        
    return result


# Test 1 
matrix_A_1 = np.array([
    [2, 1], 
    [1, 3]
], dtype='float64')
eigen_values_A_1, eigen_vectors_A_1 = rotation_method(matrix_A_1)

print('Eigen values matrix A_1', eigen_values_A_1)   # -> [1.38196601 3.61803399]
print('Eigen vectors matrix A_1', eigen_vectors_A_1) # -> [array([ 0.85065081, -0.52573111]), array([0.52573111, 0.85065081])]