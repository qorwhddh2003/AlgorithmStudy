MOD = 10007

n = int(input())
dp = [-1] * (n + 1)

dp[0] = 1
dp[1] = 1

for i in range(2, n + 1) :
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= MOD

print(dp[n])

