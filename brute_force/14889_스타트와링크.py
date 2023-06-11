from itertools import combinations, permutations

N = int(input())
st_list = [list(map(int, input().split())) for _ in range(N)]

com_list=[(i+1) for i in range(N)]

combi = list(combinations(com_list, N//2))
# print(combi)

ans = 20000000

for i in range((len(combi)//2)+1):
    team_a = 0
    team_b = 0
    # print(combi[i])
    # print(combi[(len(combi))-1-i])

    for k in range(len(combi[i])):
        for j in range(len(combi[i])):
            team_a += st_list[combi[i][k]-1][combi[i][j]-1]
            # print(combi[i][k],combi[i][j], "team_a :", team_a)
            team_b += st_list[combi[(len(combi))-1-i][k]-1][combi[(len(combi))-1-i][j]-1]
            # print(combi[(len(combi))-1-i][k],combi[(len(combi))-1-i][j],"team_b :", team_b)


    ans = min(ans, (max(team_a,team_b)-min(team_a,team_b)))
    if ans == 0:
        break

print(ans)