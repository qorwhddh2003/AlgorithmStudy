dp = [-1] * 91
dp[0] = 0
dp[1] = 1

def f(n) :
    if dp[n] != -1 :
        return dp[n]

    dp[n] = f(n - 1) + f(n - 2)
    return  dp[n]

print(f(int(input())))