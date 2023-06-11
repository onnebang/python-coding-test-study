import copy

L, K, C = map(int, input().split())
m = list(map(int, input().split()))
m = list(set(m))
m.sort()
m_2 = []
# print(m)
if len(m) <= C :
    m_2 = copy.deepcopy(m)
else:
    while len(m) > C :
        if len(m) == L and C >= (L-1):
            p = L//(C+1)
            while p < len(m):
                m_2.append(m[p-1])
                p += L//(C+1)
            break
        if max(m) == L:
            m.pop()
        # print(m)
        m_plus = []

        for i in range(len(m)):
            # print(i)
            # if i == 0 :
            #     m_plus.append(m[i])
            #     m_plus.append(m[i + 1] - m[i])
            # elif i == (len(m)-1):
            #     m_plus.append(L-m[i])
            # else:
            #     m_plus.append(m[i+1]-m[i])
            # print(m_plus)

            if i == 0 :
                m_plus.append(m[i+1])
            elif i == (len(m)-1):
                m_plus.append((L-m[i-1]))
            else:
                m_plus.append(m[i+1]-m[i-1])
            # print(m_plus)

        # print(m_plus.index(min(m_plus)))
        min = L
        index_m = 0
        for j in range(len(m_plus)):
            if m_plus[j] <= min:
                index_m = j
                min = m_plus[j]
                # print(index_m, min)
        m.pop(index_m)
        m_2 = copy.deepcopy(m)

# print(m_2)

m_plus = []
if len(m_2)==1:
    m_plus.append(m_2[0])
    m_plus.append(L-m_2[0])
else:
    for i in range(len(m_2)):
        if i == 0:
            m_plus.append(m_2[i])
        elif i == (len(m_2) - 1):
            m_plus.append((L - m_2[i]))
        else:
            m_plus.append(m_2[i] - m_2[i-1])
# print(m_plus)
print(max(m_plus), m_2[0])