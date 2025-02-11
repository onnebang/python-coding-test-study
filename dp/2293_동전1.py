n, k = map(int, input().split())
count = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

for i in count:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]

print(dp[k])
