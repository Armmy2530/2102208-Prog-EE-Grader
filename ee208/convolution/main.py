def convolution(a, b):
    n, m = 0,0
    end =  len(a) + len(b) - 1
    result = []
    for i in range(end):
        sum = 0
        for n in range(0,i+1):
            for m in range(i - n + 1):
                # print(i,n,m,sum,result)
                if n >= len(a) or m >= len(b):
                    continue
                else:
                    if (n+m == i):
                        sum += a[n]*b[m]

        result.append(sum)
    return result # Return the resulting convolution array
if __name__ == "__main__":
    a = [1, 2, 3,6,7,8]
    b = [4, 5]
    print(convolution(a, b)) # [4, 13, 22, 15]
