import sys
import heapq
from itertools import combinations

l = []

for _ in range(9) :
    l.append(int(sys.stdin.readline()))

for c in combinations(l, 7) :
    if sum(c) == 100 :
        print(*sorted(c), sep = '\n')
        break