
while True:
    n = list(map(int, input().strip()))
    m = list(map(int, input().strip()))
    m.sort(reverse=True)
    print(m)
    for i in m:
        index = 0
        for j in range(len(n) - 1):
            print(j, len(n)-j-1, n[len(n)-j-1])
            if i == n[len(n)-j-1]:
                if n[len(n)-j-2] <= n[len(n)-j-1]:
                    if index == 0:
                        index = len(n) - j - 1
                else:
                    index = len(n)-j-1
                    print("index:", index)

            if j == (len(n) - 2):
                if i == n[0] and n[0] < n[1]:
                    n.pop(0)

                else:
                    n.pop(index)

        print(*n, sep="")
    print(*n, sep="")


# while True:
#     n = list(map(int, input().strip()))
#     m = list(map(int, input().strip()))
#     m.sort()
#     print(m)
#     for i in m:
#         index = 0
#         for j in range(len(n) - 1):
#             if i == n[j]:
#                 if n[j] < n[j + 1]:
#                     n.pop(j)
#                     break
#                 else:
#                     index = j
#
#             if j == (len(n) - 2):
#                 if i == n[j + 1]:
#                     n.pop(j + 1)
#
#                 else:
#                     n.pop(index)
#         print(*n, sep="")
#     print(*n, sep="")