import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * n for _ in range(n)]
check = [False] * n
count = 0

for _ in range(m) :
    u, v = map(lambda x : x-1, map(int, sys.stdin.readline().split()))

    graph[u][v] = graph[v][u] = 1

def dfs(cur) :
    for next in range(n) :
        if graph[cur][next] and not check[next]:
            check[next] = True
            dfs(next)

for i in range(n) :
    if not check[i] :
        count += 1
        dfs(i)

print(count)