# python3
import random as r
import sys
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

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
        #if numbers[j] > max2 and numbers[j] < max1: # 2 numbers the same won't see them
        #if numbers[j] > max2 and numbers[j] <= max1: # not saving the index and skipping it so takes max1 squared
        if numbers[j] > max2 and numbers[j] <= max1 and j != index1: #CORRECT
            max2 = numbers[j]
    max_product = max1 * max2
    return max_product

if __name__ == '__main__':

    #input_numbers = [int(x) for x in input().split()]
    #print(max_pairwise_product_fast(input_numbers))
    
    while 1: # Infinite Loop
        a = []
        # Random test generator
        n = r.randint(2, 9) # Generate random array size
        print(n) 
        for i in range(n):  
# Generat array w/ n random numbers and output it so that in the process of the infinite loop we always know what is the current test
            a.append(r.randint(0, 9))
        print(a)
        
        res1 = max_pairwise_product(a) # Naive slow implementation
        res2 = max_pairwise_product_fast(a) # My implementation

        # Compare results if different stop and print answers
        if res1 != res2:
            print('wrong answer'+ ' ' + str(res1) + ' ' + str(res2))
            break
        else:
            print('OK')
        
