import numpy as np

def cosine_of_difference(x):
    x = np.array([x])
    A =  x - x.T
    A = np.cos(A)
    return A # Return the resulting matrix
    
exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line
