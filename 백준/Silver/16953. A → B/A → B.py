import sys
sys.setrecursionlimit(10**9*2)
A, B = map(int, sys.stdin.readline().split())
ans = -1
dp = {}

def recur(count, num) :
    if num > B :
        return

    try :
        dp[num] = min(count, dp[num])
    except :
        dp[num] = count

    recur(count + 1, num * 2)
    recur(count + 1, num * 10 + 1)

recur(1, A)

try:
    print(max(dp[B], ans))
except :
    print(-1)