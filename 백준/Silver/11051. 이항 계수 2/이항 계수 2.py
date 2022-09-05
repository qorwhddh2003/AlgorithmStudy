import sys
sys.setrecursionlimit(10 ** 7)
MOD = 10007

n, k = map(int, input().split())

dp = [[0] * 1001 for _ in range(1001)]

def bino(n, k) :
    if dp[n][k] : return dp[n][k]
    elif k == 0 or k == n : return 1

    dp[n][k] = bino(n-1, k-1) + bino(n-1, k)
    dp[n][k] %= MOD

    return dp[n][k]


print(bino(n, k))