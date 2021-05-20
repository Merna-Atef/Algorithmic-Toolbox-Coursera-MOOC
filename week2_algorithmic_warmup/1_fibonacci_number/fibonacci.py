# Uses python3
import numpy as np
import random as r

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fast_calc_fib(n):
    fibSeries = np.empty(n+1,int)
    fibSeries[0] = 0
    if n == 0:
        return fibSeries[0]
    elif n > 0:
        fibSeries[1] = 1
        for i in range(2, n + 1):
            fibSeries[i] = fibSeries[i-1]+fibSeries[i-2]
        return fibSeries[n]

""" while(1):
    n  = r.randint(0,45)
    print(n)
    
    res1 = calc_fib(n)
    res2 = fast_calc_fib(n)

    if res1 != res2:
        print('wrong answer'+ ' ' + str(res1) + ' ' + str(res2))
        break
    else:
        print('OK')  """
n = int(input())
print(fast_calc_fib(n))
