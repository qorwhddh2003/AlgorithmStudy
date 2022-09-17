import sys
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        y, x = q.popleft()

        for i in range(4) :
            dy = y + move[i][0]
            dx = x + move[i][1]

            if 0 <= dy < N and 0 <= dx < M and board[dy][dx] == 1 and not visited[dy][dx] :
                board[dy][dx] = board[y][x] + 1
                visited[dy][dx] = True
                q.append((dy, dx))

for i in range(N) :
    for j in range(M) :
        if board[i][j] == 2 and not visited[i][j] :
            board[i][j] = 0
            visited[i][j] = True
            bfs((i, j))

for i in range(N) :
    for j in range(M) :
        if not visited[i][j] and board[i][j] == 1:
            board[i][j] = -1

    print(*board[i])