# Uses python3
import math as m
import numpy as np
import random as r
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    fibSeries = np.empty(n+1,int)
    fibSeries[0] = 0
    fibSeries[1] = 1
    previous = 0
    current  = 1
    for i in range(2, n + 1):
        previous, current = current, previous + current        
        fibSeries[i] = current % 10 
    return fibSeries[n]

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    fibSeries = np.empty(n+1,int)
    fibSeries[0] = 0
    fibSeries[1] = 1    
    for i in range(2, n + 1):
        fibSeries[i] = (fibSeries[i-1]+fibSeries[i-2])%10
    return fibSeries[n]

if __name__ == '__main__':

    """ while(1):
        n = r.randint(0,10000000)
        print(n)
        
        res1 = get_fibonacci_last_digit_naive(n)
        res2 = get_fibonacci_last_digit(n)
        #print('OK',res2)

        if res1 != res2:
            print('wrong answer'+ ' ' + str(res1) + ' ' + str(res2))
            break
        else:
            print('OK')  """

    n = int(input())
    print(get_fibonacci_last_digit(n))
