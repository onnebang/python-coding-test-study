n = int(input())

pattern = list(map(str, input().split("*")))
length = len(pattern[0]) + len(pattern[1])
file_list = [list(map(str, input().strip())) for _ in range(n)]

for i in file_list:
    if ''.join(i[:len(pattern[0])]) == pattern[0] and ''.join(i[-len(pattern[1]):]) == pattern[1] and len(i) >= length:
        print("DA")
    else:
        print("NE")