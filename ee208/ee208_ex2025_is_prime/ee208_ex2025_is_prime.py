import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    print(is_prime(3))
    print(is_prime(10))
