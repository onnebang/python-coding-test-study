from itertools import combinations
from math import prod

n = int(input())
list_1 = []
list_2 = []
for _ in range(n):
    a,b = list(map(int, input().split()))
    list_1.append(a)
    list_2.append(b)


min_s = 1000000000
for i in range(1,n+1):
    combi1 = list(combinations(list_1, i))
    combi2 = list(combinations(list_2, i))
    for j in range(len(combi1)):
        min_s = min(min_s,max(prod(combi1[j]),sum(combi2[j])) - min(prod(combi1[j]),sum(combi2[j])))

print(min_s)