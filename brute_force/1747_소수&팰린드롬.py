import math

n = int(input())


def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


def is_pal(x):
    pal_list = list(str(x).strip())
    che_list = [0] * len(pal_list)
    # print(pal_list)
    if len(che_list) != 1:
        for i in range(len(pal_list)):
            che_list[i] = pal_list[len(pal_list)-i-1]
    else:
        return True

    if che_list == pal_list:
        return True
    return False


check = True

while check:
    if n == 1:
        print(2)
        break
    if is_prime_number(n):
        if is_pal(n):
            print(n)
            check = False
    n += 1
# print(n)
