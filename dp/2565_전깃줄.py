n = int(input())

ele_list = [list(map(int, input().split())) for _ in range(n)]
ele_list.sort()

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if ele_list[i][1] > ele_list[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
