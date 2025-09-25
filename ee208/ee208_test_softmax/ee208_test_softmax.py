import numpy as np
def softmax(A):
    B = (np.exp(A))
    C = (np.sum(B,axis=1).reshape(-1,1))
    ans = B/C
    return ans
if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    A = np.array([[1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]])
    print(softmax(A))

