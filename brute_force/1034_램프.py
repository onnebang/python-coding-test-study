import itertools
# from itertools import permutations,product

n, m = map(int, input().split())

bulb_map = [tuple(map(int, input().strip())) for _ in range(n)]
k = int(input())
# print(bulb_map)
# print(n,m,bulb_map,k)
zero_arr = [0, 1]
zero_combi = list(itertools.product(zero_arr, repeat=m))
print(zero_combi)
# zero_combi = list(permutations(zero_arr, m))'
# print(set(bulb_map))
zero_combi = list(set(bulb_map))
print(zero_combi)

zero_count = {}
for i in range(len(zero_combi)):
    zero_count[zero_combi[i]] = 0

print(zero_count)

for i in range(len(bulb_map)):
    # print(i)
    for j in range(len(zero_combi)):
        # print(j)
        # print(bulb_map[i], zero_combi[j])
        if bulb_map[i] == zero_combi[j]:
            # print(zero_count[zero_combi[j]])
            zero_count[zero_combi[j]] += 1
            # print(zero_count)
            break

print(zero_count)

sorted_dict = dict(sorted(zero_count.items(), key = lambda item: item[1], reverse = True))
print(sorted_dict)

ans = 0

for key, value in sorted_dict.items():
    print(k, key, value, list(key).count(0))
    if k == 0 and list(key).count(0) == 0:
        ans = max(ans, value)
        break

    elif k >= list(key).count(0):
        if k%2 == 0:
            if list(key).count(0)%2 == 0:
                print(key, value)
                print(list(key).count(0))
                ans = max(ans, value)
                break
        else:
            if list(key).count(0) % 2 != 0:
                ans = max(ans, value)
                break

    elif value == 0:
        ans = max(ans, value)
        break

print(ans)