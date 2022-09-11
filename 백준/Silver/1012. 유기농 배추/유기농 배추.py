from collections import deque

moveX = [0, 0, -1, 1]
moveY = [1, -1, 0, 0]

def bfs(start) :
    global ans
    q = deque()
    q.append(start)

    ans += 1

    while q :
        y, x = q.popleft()

        for i in range(4) :
            dy = y + moveY[i]
            dx = x + moveX[i]

            if 0 <= dy < M and 0 <= dx < N and not visited[dy][dx] and field[dy][dx] :
                visited[dy][dx] = True
                q.append((dy, dx))


for _ in range(int(input())) :
    ans = 0
    M, N, K = map(int, input().split())
    field = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    for i in range(K) :
        y, x = map(int, input().split())
        field[y][x] = 1

    for i in range(M) :
        for j in range(N) :
            if field[i][j] == 1 and not visited[i][j] :
                visited[i][j] = True
                bfs((i, j))

    print(ans)
