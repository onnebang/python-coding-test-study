def solution(msg):
    dict_num = [""] * 27
    answer = []

    for i in range(1, 27):
        dict_num[i] = chr(i + 64)
    count = 0

    for i in range(len(msg)):
        count -= 1

        if count <= 0:
            last_index = dict_num.index(msg[i])

            for j in range(i + 1, len(msg) + 1):
                if msg[i:j] in dict_num:
                    last_index = dict_num.index(msg[i:j])
                else:
                    dict_num.append(msg[i:j])
                    break

            answer.append(last_index)
            count = len(dict_num[last_index])

    return answer
