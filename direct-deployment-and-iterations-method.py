import numpy as np

def stop_criterion(x_1, x_0, eps=1e-3):
    return np.abs(x_1 - x_0) < eps

# Direct deployment method

# TODO: Implement this method

# Iterations method

def iterations_method(A, eps=1e-3):
    x_0 = np.ones(len(A))
    x_1 = np.dot(A, x_0)
    
    lambda_0 = x_1[0] / x_0[0]
    lambda_1 = lambda_0
    
    i = 0
    
    while True:
        i += 1
        
        x_0 = x_1.copy()
        x_1 = np.dot(A, x_0)
        
        lambda_0 = lambda_1
        lambda_1 = x_1[0] / x_0[0]
            
        # Normalization eigen vector on each 5 step    
        if i % 5 == 0:
            x_1 /= np.linalg.norm(x_1)
        
        if stop_criterion(lambda_1, lambda_0, eps):
            break
    
    # Normalization eigen vector in end
    x_1 /= np.linalg.norm(x_1)
    
    return x_1, lambda_1

A_2 = np.array([[5, 1, 2], [1, 4, 1], [2, 1, 3]])

A_2_eigen_vector, A_2_eigen_value = iterations_method(A_1)

print("Eigen vector for A_2 matrix:", A_2_eigen_vector) # -> [0.75249496 0.4318604  0.49724031]
print("Eigen value, for A_2 matrix:" , A_2_eigen_value) # -> 6.8958704371104655

