import numpy as np

def hankel_matrix(x):
    return np.flip(np.diag(x),axis=0)

# if __name__ == "__main__":
#     x = [1, 2, 3]
#     print(hankel_matrix(x))

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this lin
