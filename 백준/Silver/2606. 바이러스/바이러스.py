import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

web = [[0] * n for _ in range(n)]
visited = [False] * n

for _ in range(m) :
    start, end = map(lambda x : x - 1, map(int, sys.stdin.readline().split()))
    web[start][end] = web[end][start] = 1

def bfs(start) :
    q = deque()
    q.append(start)

    visited[start] = True

    ans = []

    while q :
        cur = q.popleft()

        for next in range(n) :
            if web[cur][next] and not visited[next] :
                visited[next] = True
                q.append(next)

                ans.append(next)

    return len(ans)

print(bfs(0))