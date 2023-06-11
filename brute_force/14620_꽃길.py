N = int(input())
st_list = [list(map(int, input().split())) for _ in range(N)]

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]


def check(a, b):
    for i in range(5):
        x = a + di[i]
        y = b + dj[i]
        if visited[x][y] == 1:
            return False
    return True


def bfs(cur):
    global total, answer

    if cur == 3:
        answer = min(answer, total)
        return

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if check(i, j):
                for k in range(5):
                    x = i + di[k]
                    y = j + dj[k]
                    visited[x][y] = 1
                    total += st_list[x][y]

                bfs(cur + 1)

                for k in range(5):
                    x = i + di[k]
                    y = j + dj[k]
                    visited[x][y] = 0
                    total -= st_list[x][y]


visited = [[0] * N for i in range(N)]
answer = 2000000
total = 0
bfs(0)
print(answer)
