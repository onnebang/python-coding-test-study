n = int(input())
step_point = [int(input()) for _ in range(n)]

dp = [0] * n

dp[0] = step_point[0]
dp[1] = step_point[0] + step_point[1]

if n <= 2:
    print(sum(step_point))

else:
    for i in range(2, n):
        dp[i] = max(
            dp[i - 2] + step_point[i], dp[i - 3] + step_point[i - 1] + step_point[i]
        )

    print(dp[-1])
