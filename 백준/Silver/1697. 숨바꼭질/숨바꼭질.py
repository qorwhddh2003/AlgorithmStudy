from collections import deque

def bfs(start, end) :
    max_ = 10**5
    q = deque()
    visited = [0] * (max_ + 1)
    q.append(start)

    while q :
        cur = q.popleft()

        if cur == end :
            return visited[cur]

        for x in (cur - 1, cur + 1, cur * 2) :
            if (0 <= x <= max_) and not visited[x] :
                visited[x] = visited[cur] + 1
                q.append(x)

n, k = map(int, input().split())

print(bfs(n, k))