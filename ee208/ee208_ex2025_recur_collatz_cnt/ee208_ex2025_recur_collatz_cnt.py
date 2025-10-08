def recur_collatz_count(n: int) -> int:
    if (n == 1):
        return 0
    if (n%2 == 0):
        n = n/2
    else:
        n = n*3 + 1
    return recur_collatz_count(n) + 1

if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    print(recur_collatz_count(10)) # Should print 6
    print(recur_collatz_count(6)) # Should print 8
    print(recur_collatz_count(3)) # Should print 7
