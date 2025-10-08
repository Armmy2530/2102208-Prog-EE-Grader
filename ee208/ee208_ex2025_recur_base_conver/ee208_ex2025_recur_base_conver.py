def recur_base_convert(b: int, n: int) -> str:
    if(n < b):
        return str(n)
    return recur_base_convert(b, n//b) + str(n%b)

if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    print(recur_base_convert(2, 10)) # Should print "1010"
    print(recur_base_convert(8, 255)) # Should print "377"
