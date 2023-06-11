import sys

input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
dp = [[0] * n for i in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n - 1):
    if a_list[i] == a_list[i + 1]:
        dp[i][i + 1] = 1

for cnt in range(n - 2):
    for i in range(n - 2 - cnt):
        j = i + 2 + cnt
        if a_list[i] == a_list[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1

k = int(input())

for i in range(k):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])
