def solution(record):
    answer = []
    open_chat = {
        k.split()[1]: k.split()[2]
        for k in record
        if k.split()[0] == "Enter" or k.split()[0] == "Change"
    }

    for i in record:
        k = i.split()
        if k[0] == "Enter":
            str1 = open_chat[k[1]] + "님이 들어왔습니다."
            answer.append(str1)
        elif k[0] == "Leave":
            str1 = open_chat[k[1]] + "님이 나갔습니다."
            answer.append(str1)
    return answer

    # for k in record:
    #     check = k.split()
    #     if check[0]
    #     open_chat.append([check, id, name])
    #     if check == "Change":
    #         for i in len(open_chat):
    #             if open_chat[i][1] == id:
    #                 open_chat[i][2] = name

    # for k in open_chat:
    #     check, id, name = k.split()
    #     if check == "Enter":
    #         str1 = name+"님이 들어왔습니다."
    #         answer.append(str1)
    #     elif check == "Leave":
    #         str1 = name+"님이 나갔습니다."
    #         answer.append(str1)

    # return answer
