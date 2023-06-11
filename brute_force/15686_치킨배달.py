from itertools import combinations

n, m = map(int, input().split())

chicken_map = [list(map(int, input().split())) for _ in range(n)]

chicken_list = []
house_list = []

for i in range (n):
    for j in range(n):
        if chicken_map[i][j] == 1:
            house_list.append([i,j])
        elif chicken_map[i][j] == 2:
            chicken_list.append([i, j])

check2 = []

for i in range(len(chicken_list)):
    check = []
    for j in range (len(house_list)):
        check.append((abs(chicken_list[i][0]-house_list[j][0])+abs(chicken_list[i][1]-house_list[j][1])))

    check2.append(check)

# print(check2)

# nums = [i for i in range(len(chicken_list))]
combi = list(combinations(check2, m))

# print(combi)

min_x = 100000


for k in combi:
    ans = 0
    for j in range(len(house_list)):

        min_c = 1000

        for i in range(len(k)):
            min_c = min(min_c, k[i][j])

        ans += min_c

    min_x = min(min_x, ans)

print(min_x)