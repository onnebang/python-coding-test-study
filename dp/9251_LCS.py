arr_1 = list(map(str, input().strip()))
arr_2 = list(map(str, input().strip()))

dp = [[0] * (len(arr_2) + 1) for _ in range(len(arr_1) + 1)]

for i in range(1, len(arr_1) + 1):
    for j in range(1, len(arr_2) + 1):
        if arr_1[i - 1] == arr_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
