MOD = 1_000_000_000

n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]

for i in range(9) :
    dp[1][i] = 1

for i in range(2, n + 1) :
    for j in range(10) :

        #dp[자리수][수]

        if j < 9 :
            dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD

        if j > 0 :
            dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] %= MOD


print(sum(dp[n][:]) % MOD)