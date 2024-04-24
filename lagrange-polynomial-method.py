def lagrange_polynomial(x, y, eval_point):
    '''
    
    [!] Disclaimer
    I decided to code a function to calculate the Lagrange polynomial with setting the value that we're looking for directly (eval_point) to the basic decomposition. 
    As a result, we will have an approximately function, and the sum of the basic extensions with an approximately point.
    
    '''
    
    n = len(x) # Count of x points

    result = 0 # Init result equation value 

    # Our parts of Lagrange polynomial basis polynomial 
    for i in range(n):
        '''
        
        e.g. f(x)_i * ( (x - x_2) * (x - x_3) * (x - x_4)) / ( (x_0 - x_2) * (x_0 - x_3) * (x_0 - x_4) )
        Where x is the value of eval_point and we substitute it into the expression
        Also in first iteration we need to multiple on function value, so I set first value when init
        I divide it to iterations with product of parts in loop:
           
        ---
            iter 1: f(x)_0 * (x - x_2) / (x_0 - x_2) -> 7 * (2.5 - 3) / (2 - 3)
            iter 2:          (x - x_3) / (x_0 - x_3) ->     (2.5 - 4) / (2 - 4)
            iter 3:          (x - x_4) / (x_0 - x_4) ->     (2.5 - 5) / (2 - 5)
        ---
        
        We multiply all these iterations with each other, and then add them to the overall result
     
        
        '''
        
        t = y[i] # Before count part of values, we need to set the value of y[i] (this is f(x)_i), in next iteration we will multiple by next value
           
        for j in range(n):
            # Ignore the same point
            if j != i:
                t *= (eval_point - x[j]) / (x[i] - x[j])
        
        # Add eval_point value in basis polynomial to global result 
        result += t

    return result

# test 1
init_x_values_1 = [2, 3, 4, 5]
init_y_values_1 = [7, 5, 8, 7]

print(lagrange_polynomial(init_x_values_1, init_y_values_1, 2.5)) # -> 4.8125

# test 2
init_x_values_2 = [-1, 0, 1, 3]
init_y_values_2 = [2, 4, 5, 0]

print(lagrange_polynomial(init_x_values_2, init_y_values_2, 0.5)) # -> 4.6875