import sys
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

M, N = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def bfs(start) :
    q = deque()
    for i in start : q.append(i)

    while q :
        y, x = q.popleft()

        for i in range(4) :
            dy = y + move[i][0]
            dx = x + move[i][1]

            if 0 <= dx < M and 0 <= dy < N and board[dy][dx] == 0 and not visited[dy][dx]:
                board[dy][dx] = board[y][x] + 1
                q.append((dy, dx))
                visited[dy][dx] = True



startList = []
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 1 :
            visited[i][j] = True
            board[i][j] = 0
            startList.append((i, j))

bfs(startList)

maxAns = 0
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 0 and not visited[i][j] :
            print(-1)
            exit()
        else :
          maxAns = max(maxAns, board[i][j])

print(maxAns)