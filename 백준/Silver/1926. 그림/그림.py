import sys
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(start) :
    q = deque()
    q.append(start)

    count = 1

    while q :
        y, x = q.popleft()

        for i in range(4) :
            dy = y + move[i][0]
            dx = x + move[i][1]

            if 0 <= dy < N and 0 <= dx < M and not visited[dy][dx] :
                if board[dy][dx] :
                    visited[dy][dx] = True
                    q.append((dy, dx))
                    count += 1

    return count

ans = [0]

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N) :
    for j in range(M) :
        if board[i][j] == 1 and not visited[i][j] :
            visited[i][j] = True
            ans.append(bfs((i, j)))

print(len(ans) - 1, max(ans), sep='\n')