def collatz_count(n: int) -> int:
    count = 0
    while n!=1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        count += 1
    return count
if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    print(collatz_count(10))
