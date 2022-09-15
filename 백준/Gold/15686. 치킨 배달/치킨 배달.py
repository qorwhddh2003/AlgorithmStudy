import sys
from itertools import combinations

def getDistance(chickenXY, houseXY):
    hy, hx = houseXY
    cy, cx = chickenXY

    return abs(hy - cy) + abs(hx - cx)

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 99999
chicken = []
house = []

for i in range(N) :
    for j in range(N) :
        if board[i][j] == 1 :
            house.append((i, j))
        elif board[i][j] == 2 :
            chicken.append((i, j))

for com in combinations(chicken, M) :
    tot = 0
    for h in house :
            tot += min(getDistance(chi, h) for chi in com)

    ans = min(tot, ans)

print(ans)