from collections import  deque

moveX = [1, -1, 0, 0]
moveY = [0, 0, 1, -1]

n, m = map(int, input().split())
road = [[int(x) for x in input().rstrip()] for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs() :
    q = deque()
    q.append((0, 0))

    while q :
        y, x = q.popleft()

        for i in range(4) :
            dx = x + moveX[i]
            dy = y + moveY[i]

            if 0 <= dx < m and 0 <= dy < n and not visited[dy][dx] and road[dy][dx] :
                road[dy][dx] = road[y][x] + 1
                visited[dy][dx] = True

                q.append((dy, dx))

    print(road[n - 1][m - 1])

bfs()