n = int(input())

for i in range(n):
    k = int(input())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))

    dp = [[0] * k for _ in range(2)]

    dp[0][0] = list1[0]
    dp[1][0] = list2[0]

    for j in range(1, k):
        if j == 1:
            dp[0][j] = dp[1][j - 1] + list1[j]
            dp[1][j] = dp[0][j - 1] + list2[j]

        else:
            dp[0][j] = max(
                dp[1][j - 1] + list1[j], max(dp[0][j - 2], dp[1][j - 2]) + list1[j]
            )
            dp[1][j] = max(
                dp[0][j - 1] + list2[j], max(dp[0][j - 2], dp[0][j - 2]) + list2[j]
            )
    print(max(max(dp[0]), max(dp[1])))
