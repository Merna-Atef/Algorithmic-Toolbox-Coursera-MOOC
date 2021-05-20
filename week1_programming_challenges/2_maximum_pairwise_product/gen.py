import random as r
import sys as s

n = int(s.argv[1])
mx = int(s.argv[2])
myseed = int(s.argv[3])
r.seed(myseed)

with open("input.txt", 'w') as out_file:
    out_file.write(' '.join([str(r.randint(1, mx)) for i in range(n)]))
