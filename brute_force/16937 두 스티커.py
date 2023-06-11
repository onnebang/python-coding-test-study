H, W = map(int, input().split())
N = int(input())
st_list = [list(map(int, input().split())) for _ in range(N)]
st_list.sort(key=lambda x: (-x[0], -x[1]))

cnt = 0

for i in range(N-1):
    if st_list[i][0] <= max(H,W) and st_list[i][1] <= max(H,W):
        for j in range(i+1,N):
            if st_list[j][0] <= max(H, W) and st_list[j][1] <= max(H, W):
                if min(H - st_list[i][0], W) >= min(st_list[j][0],st_list[j][1]) and max(H - st_list[i][0], W) >= max(st_list[j][0],st_list[j][1]):
                    cnt = max(cnt, st_list[i][0] * st_list[i][1] + st_list[j][0]*st_list[j][1])

                if min(H - st_list[i][1], W) >= min(st_list[j][0],st_list[j][1]) and max(H - st_list[i][1], W) >= max(st_list[j][0],st_list[j][1]):
                    cnt = max(cnt, st_list[i][0] * st_list[i][1] + st_list[j][0]*st_list[j][1])

                if min(W - st_list[i][0], H) >= min(st_list[j][0], st_list[j][1]) and max(W - st_list[i][0], H) >= max(st_list[j][0], st_list[j][1]):
                    cnt = max(cnt, st_list[i][0] * st_list[i][1] + st_list[j][0]*st_list[j][1])

                if min(W - st_list[i][1], H) >= min(st_list[j][0], st_list[j][1]) and max(W - st_list[i][1], H) >= max(st_list[j][0], st_list[j][1]):
                    cnt = max(cnt, st_list[i][0] * st_list[i][1] + st_list[j][0]*st_list[j][1])

print(cnt)

