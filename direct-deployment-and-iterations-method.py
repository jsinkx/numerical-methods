import numpy as np

# utils for direct deployment method

def stop_criterion_newton(x_n1, x_n):
    numerator = x_n1 - x_n
    denominator = 1 - ((x_n1 - x_n) / (x_n - x_n1))
   
    return abs(numerator / denominator)

def deriv_newton(arr):
    return arr[1:] * np.array(range(1, len(arr)))

def f_newton(x, arr):
    sum = 0
    
    for i in range(1, len(arr) + 1):
        sum += x**i * arr[i - 1]
    
    return sum

def newton(f, arr, x_0, eps = 10 ** (-2), c = 1):
    x_1 = x_0 - f_newton(x_0, arr) / f_newton(x_0, deriv_newton(arr))
    x = [x_0, x_1] 
      
    # Default (weak criterion): while abs(x[1] - x[0]) >= eps:
    while stop_criterion_newton(x[1], x[0]) >= eps: 
        temp = x[1] 
        x[1] = x[1] - c * f_newton(x[1], arr) / f_newton(x[1], deriv_newton(arr)) 
        x[0] = temp
        
    return x[1]

# Direct deployment method

def create_equation(A):
    if len(A) == 2:
        return [A[0][0]*A[1][1] - A[0][1]*A[1][0], -(A[1][1]+A[0][0]), 1]
    elif len(A) == 3:
        return [A[0][0]*A[1][1]*A[2][2] + A[0][1]*A[1][2]*A[2][0] + A[0][2]*A[1][0]*A[2][1]
                - A[0][2]*A[1][1]*A[2][0] - A[0][1]*A[1][0]*A[2][2] - A[0][0]*A[1][2]*A[2][1],
                A[0][0]*A[1][1] - A[0][0]*A[2][2] - A[1][1]*A[2][2] + A[0][2]*A[2][0]
                + A[0][1]*A[1][0] + A[1][2]*A[2][1],
                A[0][0] + A[1][1] + A[2][2],
                1]
    return []

A_1 = np.array([[2, 2, 3], [4, 5, 6], [7, 8, 9]]) # -> 0.11596922694376219
equation = create_equation(A_1)

print(newton(f_newton, equation, 1))

# utils for iterations method

def stop_criterion(x_1, x_0, eps=1e-3):
    return np.abs(x_1 - x_0) < eps

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

A_2_eigen_vector, A_2_eigen_value = iterations_method(A_2)

print("Eigen vector for A_2 matrix:", A_2_eigen_vector) # -> [0.75249496 0.4318604  0.49724031]
print("Eigen value, for A_2 matrix:" , A_2_eigen_value) # -> 6.8958704371104655

