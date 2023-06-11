def rotate(m):
    n = len(m)
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret[j][n - 1 - i] = m[i][j]
    return ret


def check(key, lock, lock_key):
    for i in range(len(key) - 1, len(key) + len(lock) - 1):
        for j in range(len(key) - 1, len(key) + len(lock) - 1):
            if lock_key[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = False

    lock_key = [
        [0 for j in range(len(lock) + (len(key) - 1) * 2)]
        for i in range(len(lock) + (len(key) - 1) * 2)
    ]

    for i in range(len(lock)):
        for j in range(len(lock)):
            lock_key[i + (len(key) - 1)][j + (len(key) - 1)] = lock[i][j]

    if check(key, lock, lock_key):
        return True

    count = 0
    while count < 4:
        key = rotate(key)
        for i in range(len(key) + len(lock) - 1):
            for j in range(len(key) + len(lock) - 1):
                for k in range(len(key)):
                    for q in range(len(key)):
                        lock_key[i + k][j + q] += key[k][q]

                if check(key, lock, lock_key):
                    return True

                for k in range(len(key)):
                    for q in range(len(key)):
                        lock_key[i + k][j + q] -= key[k][q]

        count += 1
    return False

    # left, right, up, down = len(lock),0,len(lock),0
    # for i in range(len(lock)):
    #     for j in range(len(lock)):
    #         if lock[i][j] == 0:
    #             left = min(i, left)
    #             up = min(j,up)
    #             right = max(i, right)
    #             down = max(j,down)

    # lock_key = [[0 for j in range(right-left+1)] for i in range(down-up+1)]

    # for i in range(left,right+1):
    #     for j in range(up,down+1):
    #         lock_key[i-left][j-up] = (lock[i][j] + 1) %2

    # count = 0
    # while(count<3):
    #     for i in range(len(lock_key)):
    #         if key[i][:len(lock_key[0])] != lock_key[i]:
    #             break

    #     1
    return answer
