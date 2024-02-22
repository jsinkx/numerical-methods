import numpy as np

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
     

arr = [-6, 11, -6, 1] # (x-1) * (x-2) * (x-3), the roots of equations x = {1, 2, 3}
x_0 = 10


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

def secant(f, x_0, eps = 10**(-3)):
    x_1 = x_0 - f(x_0, arr) / f(x_0, deriv(arr))
    x = [x_0, x_1] 
    
    while stop_criterion(x_1, x_0) > eps:
        temp = x[1] - f(x[1], arr) * (x[1] - x[0]) / (f(x[1], arr) - f(x[0], arr)) 
        x[0] = x[1]
        x[1] = temp

    return x[1]

print(newton(f, x_0, 10**(-5)))    # -> 3.0000000000000036
print(newton(f, x_0, 10**(-5), 3)) # -> 1.9999880265095271


print(secant(f, x_0, 10**(-5)))    # -> 3.0000000000000036
print(secant(f, x_0, 10**(-5)))    # -> 1.9999880265095271