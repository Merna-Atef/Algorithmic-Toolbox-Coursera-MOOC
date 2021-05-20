# python3
import random as r
import sys

def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max1 = 0
    index1 = -1
    for i in range(n):
        if numbers[i] > max1:
            max1 = numbers[i]
            index1 = i
    max2 = 0
    for j in range(n):
        if numbers[j] > max2 and numbers[j] <= max1 and j != index1: 
            max2 = numbers[j]
    max_product = max1 * max2
    return max_product

if __name__ == '__main__':

    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))