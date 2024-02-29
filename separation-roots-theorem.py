# Theorem №3 
def evaluation_root_modules(values):
    values = list(reversed(values))
    a_arr = values[0:len(values)-1]
    b_arr = values[1:]

    
    A = max([abs(a) for a in a_arr])
    B = max([abs(a) for a in b_arr])    
    
    r = 1 / (1 + B / abs(values[0])) # Left part
    R = 1  + A / abs(values[-1]) # Right part
    
    return (r, R)
    
# Better use this theorems (№4 & 5)   
    
# Theorem №4 (Lagrange's theorem)    
def upper_lims_positive_roots(values):
    if values[0] < 0:
        values = [v * -1 for v in values]
        
    n = len(values) - 1
    C = max(abs(v) if v < 0 else 0 for v in values)

    i = 0
    
    for index in range(len(values)):
        if (values[index]) < 0:
            i = index + 1
            
            break    

    R = 1 + (C / values[0]) ** (1 / (n - i)) 
    
    return R

# Theorem №5
def lower_upper_lims_positive_roots(values):
    reversed_values = list(reversed(values)) 
    
    R_1_values = reversed_values
    R_2_values = [v * -1 for v in values] 
    R_3_values = [v * -1 for v in reversed_values]  
    
    # count R's
    R = upper_lims_positive_roots(values)
    R_1 = upper_lims_positive_roots(R_1_values)
    R_2 = upper_lims_positive_roots(R_2_values)
    R_3 = upper_lims_positive_roots(R_3_values)
    
    return ((1 / R_1, R), (-R_2, 1 / -R_3))

values_arr = [1, 2, -5, 8, -7, -3] 

# Found lims
print(evaluation_root_modules(values_arr))  # -> (0.27272727272727276, 9.0)

# Test
print(upper_lims_positive_roots(values_arr)) # -> 3.6457513110645907

# Found lims (best)
print (lower_upper_lims_positive_roots(values_arr)) # -> (((0.5-0.20710678118654754j), 2.632993161855452), (2.632993161855452, 3.6457513110645907))