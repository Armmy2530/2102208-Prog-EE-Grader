import numpy as np
def decomposition(X, c):
    X = np.array(X)
    X2 = X * c
    return X2@X.T# Return the resulting matrix

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line
