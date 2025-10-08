def recur_avg(a: list[int]) -> float:
    n = len(a)
    if(n == 0):
        return 0
    if(n == 1):
        return a[0]
    return ((recur_avg(a[:n-1]) * (n-1)) + a[-1]) / n
   
if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    print(recur_avg([1, 2, 3, 4, 5]))
    print(recur_avg([]))
