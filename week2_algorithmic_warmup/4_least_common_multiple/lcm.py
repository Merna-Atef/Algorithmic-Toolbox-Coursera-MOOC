# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_eucl(a, b):
    if b == 0:
        return a
    else:
        return gcd_eucl(b, a%b)

def lcm_fast(a,b):
    const = a*b
    gcd = gcd_eucl(a, b)
    return int (a*b/gcd)

if __name__ == '__main__':
    a, b = [int(x) for x in input().split()]
    print(lcm_fast(a, b))

