# Dichotomy or bisection method
# While stop criterion has not worked yet, we're dividing the interval into two parts
def dichotomy(f, x_0, x_1, eps = 10 ** (-2)):
    x = [x_0, x_1]  
        
    while abs(x[1] - x[0]) >= eps:
        x_mid = (x[0] + x[1])/2

        left = f(x[0]) * f(x_mid) # Will first check 
        right = f(x[1]) * f(x_mid) # After fall left part, will check the second
        
        if left <= 0: # Left part of the function does not satisfy
            x[1] = x_mid
        elif right <= 0:
            x[0] = x_mid
        else:
            return None
    
    return x[1]
    
# The equation func
def f(x):
    return (x - 1) * (x - 2) * (x - 3) # The roots of equations x = {1, 2, 3}

# Tests     
print(dichotomy(f, 1, 1.5))               # -> 1.0078125
print(dichotomy(f, 1, 1.5, 10 ** (-5)))   # -> 1.0000076293945312
print(dichotomy(f, 1, 1.5, 10 ** (-10)))  # -> 1.0000000000582077
print(dichotomy(f, -3, 5))                # -> 1
print(dichotomy(f, 2, 5))                 # -> 2.005859375
print(dichotomy(f, 0, 5))                 # -> 3.0078125
    