from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start, target) : 
    cnt = 1
    q = deque()
    q.append((start, cnt))

    while q : 

        cur, cnt = q.popleft()

        if cur[1] == target[1] - 1 and cur[0] == target[0] - 1 :   
            print(cnt)          
            break

        for i in range(4) : 
            curX = cur[1] + dx[i]
            curY = cur[0] + dy[i]

            if (curX >= 0 and curX < target[1] and curY >= 0 and curY < target[0]) and not visited[curY][curX] and map_[curY][curX] == 1: 
                visited[curY][curX] = True
                q.append(((curY, curX), cnt + 1))


n, m = map(int, input().split())
map_ = [[int(x) for x in input()] for y in range(n)]

visited = [[False] * m for _ in range(n)]
visited[0][0] = True

bfs((0, 0), (n, m))