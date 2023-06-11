def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list, str2_list = [], []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1_list.append(str1[i] + str1[i + 1])

    for j in range(len(str2) - 1):
        if str2[j].isalpha() and str2[j + 1].isalpha():
            str2_list.append(str2[j] + str2[j + 1])

    str1_result = str1_list.copy()
    str1_temp = str1_list.copy()
    srt_gyo = []

    for i in str2_list:
        if i not in str1_temp:
            str1_result.append(i)
        else:
            str1_temp.remove(i)
            srt_gyo.append(i)

    if len(srt_gyo) == 0 and len(str1_result) == 0:
        answer = 65536
    else:
        answer = (len(srt_gyo) / len(str1_result)) * 65536

    return int(answer)
