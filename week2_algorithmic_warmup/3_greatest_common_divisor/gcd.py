# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1): #coz stop value not included
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_eucl(a, b):
    if b == 0:
        return a
    else:
        return gcd_eucl(b, a%b)


if __name__ == "__main__":

    a, b = [int(x) for x in input().split()]
    #print(gcd_naive(a, b))
    print(gcd_eucl(a, b))
