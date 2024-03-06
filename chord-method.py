import numpy as np

def deriv(arr):
    return arr[1:] * np.array(range(1, len(arr)))

def f(x):
    return x**3 - x + 1 

def custom_f(arr, x):
    return sum(list(reversed(arr))[i]*(x**i) for i in range(len(arr)))

def stop_criterion(x_1, x_0):
    return abs(x_1 - x_0)

def first_case(arr, a, x):
    return a - custom_f(arr, a) * (x - a) / (custom_f(arr, x) - custom_f(arr, a))

def second_case(arr, b, x):
    return x - custom_f(arr, x) * (b - x) / (custom_f(arr, b) - custom_f(arr, x))

def chord_method(arr, a, b, eps = (10**-3)):
    a_2der = custom_f(deriv(deriv(arr)), a)
    b_2der = custom_f(deriv(deriv(arr)), b)
    
    if (a_2der < 0):
        arr = list(map(lambda x: -1 * x, arr))
    
    if custom_f(arr, a) > 0:
        fixed_value = a
        x = b
        using_case = first_case 
    else:
        fixed_value = b
        x = a 
        using_case = second_case
        
    x_1 = using_case(arr, fixed_value, x)
    
    while stop_criterion(x_1, x) >= eps:
        x_1 = x
        x = using_case(arr, fixed_value, x)
    return x
    
arr = [1, 0, -1, 1]
a = -2
b = -1

print(chord_method(arr, a, b)) # -> -1.3249377846633381