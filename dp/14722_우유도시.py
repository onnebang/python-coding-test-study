n = int(input())
milk_list = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(i):
        milk_list[i][j]
