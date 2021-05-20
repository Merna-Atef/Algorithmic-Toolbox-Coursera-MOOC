# python3
import sys

def compute_min_refills(distance, tank, stops):
    stops.append(distance)
    stops.insert(0,0)
    lastRefill = 0
    currentRefill = 0
    numRefills = 0
    while currentRefill < len(stops)-1:
        lastRefill = currentRefill
        while currentRefill != len(stops) - 1 and stops[currentRefill+1] - stops[lastRefill] <= tank:
            currentRefill = currentRefill + 1
            if currentRefill == len(stops) - 1:
                break
        if currentRefill == lastRefill:
            return -1
        if currentRefill != len(stops) - 1:
            numRefills = numRefills+1
    return numRefills

if __name__ == '__main__': 
    
    d, m, _, *stops = map(int, sys.stdin.read().split()) # Finish input by EOF - end of file- character ctrl+z then enter
    print(compute_min_refills(d, m, stops))

'''
950
400
4
200 375 550 750
'''
# Answer 2

'''
10
3
4
1 2 5 9
'''
# Answer -1 Impossible 9 is too far from 5 (tank = 3)

'''
200
250
2
100
150
'''

# Answer 0 No need to refuel 2slan
