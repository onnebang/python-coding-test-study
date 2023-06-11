n = int(input())
count = list(map(int, input().split()))

dp = [0] * n
dp[0] = count[0]

for i in range(1, n):
    dp[i] = max(count[i], dp[i - 1] + count[i])  # arr[i] 혹은 이전 최대 연속합+arr[i]
print(max(dp))
