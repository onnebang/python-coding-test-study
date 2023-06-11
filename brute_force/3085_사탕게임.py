from itertools import groupby

def long_repeat(data):
	return max([len(list(g)) for k, g in groupby(data)], default=0)

n = int(input())
# st_list = [list(map(int, input().split())) for _ in range(N)]
candy_list = [list(map(str, input().strip())) for _ in range(n)]
print("".join(candy_list[][1]))

max = 0
#
# for i in range(n):
#     for j in range(n):
#         long_repeat("".join(candy_list))

