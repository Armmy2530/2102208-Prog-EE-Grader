import numpy as np

def find_outliers(X: np.array, alpha: float) -> np.array:
    bound = alpha * np.array([np.percentile(X, 25), np.percentile(X, 75)])
    return np.sort(X[(X<=bound[0]) | (X>=bound[1])])

# if __name__ == "__main__":
#     x= [1, 2, 3, 4, 5, 10, 15, 20, 25, 100]
#     x= np.array(x)
#     alpha = 2.0
#     print(find_outliers(x, alpha))

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line
