import numpy as np

def new_grader(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
  return (np.sum(A, axis=1), np.sum(A, axis=0))

if __name__ == "__main__":
  # You can test anything inside this block and can send it to grader
  # The grader will use only the function that you have implemented
  # !!! DO NOT write anything outside this block
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  print(new_grader(A))
