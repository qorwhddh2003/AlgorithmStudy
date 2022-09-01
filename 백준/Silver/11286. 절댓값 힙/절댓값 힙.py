import sys
import heapq

#  tuple(절댓값, 기존 값) => heapq

heap = []

for _ in range(int(sys.stdin.readline())) :
    x = int(sys.stdin.readline())

    if x :
        heapq.heappush(heap, (abs(x), x))
    else :
        print(heapq.heappop(heap)[1] if heap else 0)