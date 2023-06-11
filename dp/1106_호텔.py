c, n = map(int, input().split())

cost_list = [list(map(int, input().split())) for _ in range(n)]
dp = [10000000] * (c + 100)
dp[0] = 0

# for i in range(c + 1):
#     for j in cost_list:
#         if dp[i + j[1]] == 0:
#             dp[i + j[1]] = dp[i] + j[0]

#         else:
#             if i != 0 and dp[i] == 0:
#                 dp[i] = min(dp[i : i + j[1] + 1])
#             dp[i + j[1]] = min(dp[i + j[1]], dp[i] + j[0])
#             # print(dp)
# print(dp)
# print(dp[-(max_cost+1): ])

for cost, num_people in cost_list:
    for i in range(num_people, c + 100):
        dp[i] = min(dp[i - num_people] + cost, dp[i])

print(dp)
print(min(dp[c:]))
