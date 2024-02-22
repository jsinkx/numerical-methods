def stop_criterion(x_n1, x_n):
    numerator = x_n1 - x_n
    denominator = 1 - ((x_n1 - x_n) / (x_n - x_n1))
   
    return abs(numerator / denominator)

def root(a, x_0, eps = 10**(-3)):
    x = [x_0, 0.5 * (x_0 + a/x_0)]
    
    # Default (weak criterion): while abs(x[1] - x[0]) >= eps:
    while stop_criterion(x[1], x[0]) >= eps: 
        temp = x[1]
        x[1] = 0.5 * (x[1] + a/x[1]) # type: ignore
        x[0] = temp
        
    return x[1]
 
x_0 = 10 

print(root(16, x_0, 10**(-5))) # -> 4.000000000013422
print(root(256, 5, 10**(-5)))  # -> 16.0
print(root(49, 16, 10**(-5)))  # -> 7.000000000001278
print(root(25, 30, 10**(-5)))  # -> 5.0
