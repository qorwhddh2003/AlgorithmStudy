import sys
import heapq

d = dict()

for _ in range(int(sys.stdin.readline())) :
    book = sys.stdin.readline()

    if book in d :
        d[book] += 1
    else :
        d[book] = 1

m = max(d.values())
maxList = []

for key, value in d.items() :
    if value == m :
        maxList.append(key)

print(sorted(maxList)[0])