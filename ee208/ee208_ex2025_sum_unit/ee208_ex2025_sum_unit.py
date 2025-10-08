def sum_until_unit(n: int) -> int:
    ans = 10
    while ans >= 10:
        ans = 0
        n_list = [int(a) for a in str(n)]
        for i in n_list:
            ans += i
        n = str(ans)
    return ans

if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    print(sum_until_unit(1234560091077))
