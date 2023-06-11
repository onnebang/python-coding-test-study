n = int(input())
if n == 0:
    print(1)

else:
    dp = [1] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = 1 + dp[i - 2] + dp[i - 1]

    print(dp[-1] % 1000000007)
