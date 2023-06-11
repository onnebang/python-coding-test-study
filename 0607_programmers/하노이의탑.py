def hanoi(src, thr, dst, answer, n):
    if n == 1:
        answer.append([src, dst])
        return

    hanoi(src, dst, thr, answer, n - 1)
    answer.append([src, dst])
    hanoi(thr, src, dst, answer, n - 1)
    return answer


def solution(n):
    return hanoi(1, 2, 3, [], n)


n = int(input())
print(solution(n))
