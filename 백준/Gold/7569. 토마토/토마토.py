import sys
from collections import deque
move = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)] #x y z
M, N, H = map(int, sys.stdin.readline().split())

start = []
board = [[] for _ in range(H)]

def bfs(start) :
    q = deque()

    for i in start :
        q.append(i)

    while q :
        x, y, z= q.popleft()

        for i in range(6) :
            dx = x + move[i][0]
            dy = y + move[i][1]
            dz = z + move[i][2]

            if 0 <= dx < M and 0 <= dy < N and 0 <= dz < H :
                if board[dz][dy][dx] == 0 :
                    board[dz][dy][dx] = board[z][y][x] + 1
                    q.append((dx, dy, dz))

for i in range(H) :
    for j in range(N) :
        board[i].append(list(map(int, sys.stdin.readline().split())))
        for k in range(M) :
            if board[i][j][k] == 1 :
                start.append((k, j, i)) #x y z

bfs(start)

check = False
ans = 0
for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if board[i][j][k] == 0 :
                check = True
            ans = max(ans, board[i][j][k])

print(-1 if check else ans-1)