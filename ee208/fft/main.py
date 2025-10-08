import cmath
import math

def fft(a):
    n = len(a)
    if n ==  1:
        return a

    A = [0 + 0j] * n
    even = a[0::2]
    odd = a[1::2]

    return A # Return the FFT of the input array
if __name__ == "__main__":
    a = [1+0j, 2+0j, 3+0j, 4+0j]
    print(fft(a)) # [(10+0j), (-2+2j), (-2+0j), (-2-2j)]
