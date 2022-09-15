import sys

for _ in range(int(sys.stdin.readline())) :
    n = int(sys.stdin.readline())

    dp = [0] * (n+1)
    dp[1] = 1
    if n > 1 : dp[2] = 1
    if n > 2 : dp[3] = 1
    if n > 3 : dp[4] = 2

    for i in range(5, n+1) :
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[-1])