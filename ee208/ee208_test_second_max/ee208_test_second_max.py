import numpy as np
def second_max_per_column(A):
    ans = A.copy()
    min_v = np.min(ans)
    A_fliter = np.max(A,axis=0).reshape(1,-1)
    ans[ans==A_fliter] = min_v
    ans = np.max(ans,axis=0)
    return ans
if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    A = np.array([
    [7.0, 3.0, 5.0, 5.0],
    [7.0, 1.0, 9.0, 2.0],
    [4.0, 3.0, 9.0, -1.0],
    [0.0, 8.0, 9.0, 5.0]
    ])
    print(second_max_per_column(A))

