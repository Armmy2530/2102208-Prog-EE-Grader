import numpy as np

def matrix_norm(d, v, A):
    d = np.array(d).reshape(-1, 1)
    v = np.array(v).reshape(1, -1)
    A = np.array(A)
    return d*A*v# Return the resulting matrix

# if __name__ == "__main__":
#     d = [2 ,3 ,1]
#     v = [1 ,2 ,4]
#     A = [[1, 2, 3],
#     [4, 5 ,6],
#     [7, 8 ,9]]
#     print(matrix_norm(d, v, A))

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line

# diag(d)
# d1 0 0
# 0  d2 0
# 0  0  d3

# A
# A11 A12 A13
# A21 A22 A23
# A31 A32 A33

# A@D
# A11*d1 A12*d1 A13*d1
# A21*d2 A22*d2 A23*d2
# A31*d3 A32*d3 A33*d3

# A@D@V.T
# v1*A11*d1 v2*A12*d1 v3*A13*d1
# v1*A21*d2 v2*A22*d2 v3*A23*d2
# v1*A31*d3 v2*A32*d3 v3*A33*d3