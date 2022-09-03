from collections import deque

n, k = map(int, input().split())

max_ = 100001
visited = [0] * max_

def bfs(start, end) :
    q = deque()
    q.append((start, 0))

    while q :
        cur, time = q.popleft()


        if cur == end :
            return time

        for i, j in ((cur * 2, 0), (cur - 1, 1), (cur + 1, 1)) :
            if 0 <= i < max_ and not visited[i] :
                visited[i] = cur
                q.append((i, time + j))

print(bfs(n, k))

