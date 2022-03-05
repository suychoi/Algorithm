# ------------------------------------------------------------------------------------ 1193 번
# 풀이시간 60분

import sys
X = int(sys.stdin.readline())
L = []
if X ==1:
    print("1/1")
elif X ==2:
    print("1/2")
else:
    for i in range(1, X):
        if sum(L) < X:
            L.append(i)
        elif sum(L) > X:
            break
    c = L[0] + L[-1]
    if c % 2 == 0:
        L.reverse()
    d = sum(L)-(c-2)
    a = L[(X-d)]
    print(str(a) + "/" + str(c-a))
