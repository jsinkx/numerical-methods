import numpy as np

# utils

def stop_criterion(x_n1, x_n):
    numerator = x_n1 - x_n
    denominator = 1 - ((x_n1 - x_n) / (x_n - x_n1))
   
    return abs(numerator / denominator)

def deriv(arr):
    return arr[1:] * np.array(range(1, len(arr)))

def f(x, arr):
    sum = 0
    
    for i in range(1, len(arr) + 1):
        sum += x**i * arr[i - 1]
    
    return sum

# solve methods

# Newton's method with Broyden's 
# By default c = 1 and using default Newton method, but you can set c and it will be use Broyden's
def newton(f, x_0, eps = 10 ** (-2), c = 1):
    x_1 = x_0 - f(x_0, arr) / f(x_0, deriv(arr))
    x = [x_0, x_1] 
      
    # Default (weak criterion): while abs(x[1] - x[0]) >= eps:
    while stop_criterion(x[1], x[0]) >= eps: 
        temp = x[1] 
        x[1] = x[1] - c * f(x[1], arr) / f(x[1], deriv(arr)) 
        x[0] = temp
        
    return x[1]

# Newton's simplify method
def newton_simple(f, x_0, eps = 10 ** (-2)):
    x_1 = x_0 - f(x_0, arr) / f(x_0, deriv(arr))
    x = [x_0, x_1] 
      
    # Default (weak criterion): while abs(x[1] - x[0]) >= eps:
    while stop_criterion(x[1], x[0]) >= eps: 
        temp = x[1] 
        x[1] = x[1] - f(x[1], arr) / f(x_0, deriv(arr)) 
        x[0] = temp
        
    return x[1]

# Secant method
def secant(f, x_0, eps = 10**(-3)):
    x_1 = x_0 - f(x_0, arr) / f(x_0, deriv(arr))
    x = [x_0, x_1]
    
    while stop_criterion(x[1], x[0]) > eps:
        curr = x[1]
        x[1] = x[0] - (f(x[0], arr) * (curr - x[0])) / (f(curr, arr) - f(x[0], arr))
        x[0] = curr 

    return x[-1]

# Vars

arr = [-6, 11, -6, 1] # (x-1) * (x-2) * (x-3), the roots of equations x = {1, 2, 3}
x_0 = 10

# Usage

# Newton default
print(newton(f, x_0, 10**(-5)))        # -> 3.0000000000000036

# Newton with Broyden
print(newton(f, x_0, 10**(-5), 3))     # -> 1.9999880265095271

# Newton simplify
print(newton_simple(f, x_0, 10**(-5))) # -> 3.0062591799208933

# Secant 
print(secant(f, x_0, 10**(-5)))        # -> 3.0000002668821484