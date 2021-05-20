# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge_fast(n, m):
    if n <= 1:
        return n
    # Calculate Fi modulo m  from i = 0, till you get 0 then 1 stop and period = i-2

    F = [0,1]
    Fmod = [0,1]
    period = 1
    i = 2
    while 1:
        F.append(F[i-1]+F[i-2])
        current = F[i] % m
        nxt = (F[i] + F[i-1]) % m
        
        if current == 0 and nxt == 1:
            period = i
            break
        else:
            Fmod.append(current)
        i = i + 1
    index = n % period
    assert(index <= len(F)-1)

    return Fmod[index]

if __name__ == '__main__':
    input = sys.stdin.read() # reads as file so ctrl+z then Enter
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))