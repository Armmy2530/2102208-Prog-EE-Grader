import numpy as np
def numpy_conditional(A):
    A[A<0] = A[A<0] + 2
    return A
if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    A = np.array([-1, 0, 1, -5, 3])
    print(numpy_conditional(A))

