n = int(input())
m = int(input())
ans = abs(n-100)

if m == 0:
    ans = min(ans, m)

elif n == 100:
    ans = 0

else:
    new_n = n
    break_remote = list(map(str, input().split()))
    bnt_check = True
    while bnt_check:
        count = 0
        now_num = list(str(new_n).strip())
        check = True
        for j in now_num:
            if check:
                for i in break_remote:
                    if j == i:
                        new_n += 1
                        check = False
                        break
                    elif j != i and i == break_remote[-1]:
                        count += 1
            else: break

        if count == len(now_num):
            ans = min(ans, abs(n - new_n) + len(now_num))
            bnt_check =False

            # print(ans, new_n)
    new_n = n
    bnt_check =True

    while bnt_check:
        if new_n == -1 :
            bnt_check = False
            break
        else :
            count = 0
            now_num = list(str(new_n).strip())
            # print(now_num)
            check = True
            for j in now_num:
                if check:
                    for i in break_remote:
                        if j == i:
                            new_n -= 1
                            check = False
                            break
                        elif j != i and i == break_remote[-1]:
                            count += 1
                else:
                    break

            if count == len(now_num):
                ans = min(ans, abs(n - new_n) + len(now_num))
                bnt_check =False

print(ans)