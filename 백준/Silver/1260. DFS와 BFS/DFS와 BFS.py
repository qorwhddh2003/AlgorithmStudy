import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
board = [[0] * n for _ in range(n)]

dfsV = [False] * n
bfsV = [False] * n

for _ in range(m) :
    x, y = map(lambda x : x - 1, map(int, sys.stdin.readline().split()))
    board[x][y] = board[y][x] = 1

def dfs(start) :
    dfsV[start] = True
    print(str(start + 1), end = ' ')

    for next in range(n) :
        if board[start][next] and not dfsV[next]:
            dfs(next)

def bfs(start) :
    q = deque()
    q.append(start)
    bfsV[start] = True

    while q :
        cur = q.popleft()
        print(str(cur + 1), end = ' ')

        for next in range(n) :
            if board[cur][next] and not bfsV[next] :
                bfsV[next] = True
                q.append(next)

dfs(v - 1)
print()
bfs(v - 1)
