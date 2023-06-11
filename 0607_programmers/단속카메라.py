def solution(routes):
    routes.sort(key=lambda x: (-x[0], x[1]))
    answer, count = 1, 0

    while count < len(routes):
        for i in range(count + 1, len(routes)):
            if routes[count][0] > routes[i][1]:
                answer += 1
                count = i - 1
                break
        count += 1

    return answer
