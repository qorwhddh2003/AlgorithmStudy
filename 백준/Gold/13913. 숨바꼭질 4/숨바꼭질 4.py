from collections import deque

def bfs(start, end) :
    q = deque()
    q.append(start)

    while q :
        cur = q.popleft()

        if cur == end :
            result = []
            print(visited[cur])

            while cur != start :
                result.append(cur)
                cur = path[cur]

            result.append(start)
            result.reverse()
            print(' '.join(map(str, result)))
            return

        for x in (cur - 1, cur + 1, cur * 2) :
            if (0 <= x < max_) and not visited[x] :
                visited[x] = visited[cur] + 1
                path[x] = cur
                q.append(x)

n, k = map(int, input().split())

max_ = 100001
visited = [0] * max_
path = [0] * max_

bfs(n, k)