import sys
from collections import deque

N, P = map(int, sys.stdin.readline().split())
guitar = [[] for _ in range(7)]
ans = 0

for _ in range(N) :
    line, P  = map(int, sys.stdin.readline().split())

    while guitar[line] and guitar[line][-1] > P :
        guitar[line].pop()
        ans += 1

    if guitar[line] and guitar[line][-1] == P :
        continue
        
    guitar[line].append(P)
    ans += 1

print(ans)