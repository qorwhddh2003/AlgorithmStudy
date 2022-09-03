from collections import deque
from itertools import  combinations
import copy

moveX = [1, -1, 0, 0]
moveY = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = [[int(x) for x in input().split()] for _ in range(n)]
start, noneWall = [], set()
ans = 0

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0:
            noneWall.add((i, j))
        elif graph[i][j] == 2 :
            start.append((i, j))

def bfs(start) :
    q = deque()

    for i in start :
        q.append(i)

    while q :
        y, x = q.pop()

        for i in range(4) :
            dx = x + moveX[i]
            dy = y + moveY[i]

            if 0 <= dx < m and 0 <= dy < n and not copyGraph[dy][dx] :
                copyGraph[dy][dx] = 2
                q.append((dy, dx))

    count = 0
    for i in range(n) :
        count += copyGraph[i].count(0)

    return count

for i in combinations(noneWall, 3) :
    copyGraph = copy.deepcopy(graph)

    for wall in i :
        y, x = wall
        copyGraph[y][x] = 1

    ans = max(ans, bfs(start))

print(ans)


