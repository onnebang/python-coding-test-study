from collections import Counter

n, m = list(map(int, input().split()))

dna_list = []
for i in range (n):
    dna_list.append(list(map(str, input().strip())))

min = 0
answer = []
for j in range(m):
    check_list = []
    for i in dna_list:
        check_list.append(i[j])
    check_list.sort()
    items = Counter(check_list)
    # print(items)
    min += (n-items.most_common(1)[0][1])
    answer.append(items.most_common(1)[0][0])

# for i in dna_list:
#     cnt = 0
#     for j in dna_list:
#         for k in range(m):
#            if i[k] != j[k]:
#
#                cnt += 1
#                print(k, i, j , cnt)
#
#     if min>=cnt:
#         print(i)
#         min = cnt
#         answer.append(i)


# answer.sort()
print("".join(answer))
print(min)

