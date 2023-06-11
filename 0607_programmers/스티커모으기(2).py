def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)

    dp = [[0 for _ in range(len(sticker))] for _ in range(2)]

    dp[0][0], dp[0][1], dp[0][2] = sticker[0], sticker[0], sticker[0]
    dp[1][1], dp[1][2] = sticker[1], sticker[1]

    for i in range(3, len(sticker)):
        dp[0][i] = max(((dp[0][i - 2]) + sticker[i - 1]), (dp[0][i - 1]))
        dp[1][i] = max(((dp[1][i - 2]) + sticker[i]), (dp[1][i - 1]))

    return max(max(map(max, dp)), max(dp[0][:-1]) + sticker[-1] - sticker[0])


##########################################################

# def solution(sticker):
#     if len(sticker) <=3:
#         return max(sticker)

#     dp = [[0] * (len(sticker)) for _ in range(3)]
#     for i in range(3):
#         dp[0][i] = sticker[0]
#         dp[1][i] = sticker[1]
#         dp[2][i] = sticker[2]

#     sticker.append(sticker[0])

#     for i in range(3,len(sticker)-1):
#         dp[0][i] = max(dp[0][:i-1]) + sticker[i-1]
#         dp[1][i] = max(dp[1][:i-1]) + sticker[i]
#         dp[2][i] = max(dp[2][:i-1]) + sticker[i+1]
#     # print(dp)
#     return max(map(max, dp))

##########################################################

# def solution(sticker):
#     if len(sticker) <=3:
#         return max(sticker)

#     dp = [[0 for _ in range(len(sticker))] for _ in range(2)]

#     dp[0][0], dp[0][1] = sticker[0], sticker[0]
#     dp[1][1] = sticker[1]

#     sticker.append(sticker[0])

#     for i in range(3,len(sticker)-1):
#         dp[0][i] = max(dp[0][:i-1]) + sticker[i-1]
#         dp[1][i] = max(dp[1][:i-1]) + sticker[i]
#         # dp[2][i] = max(dp[2][:i-1]) + sticker[i+1]
#     # print(dp)
#     return max(max(map(max, dp)),dp[0][-2] + sticker[-2] - sticker[-1])
