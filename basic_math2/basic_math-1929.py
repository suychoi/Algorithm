# ------------------------------------------------------------------------------------ 1929 번
# 풀이시간 4 시간...
import sys
import math
M, N = map(int, sys.stdin.readline().split())
sosu_list = []
n_list=[]
A = int(N-M+1)
B = (int(math.sqrt(N) + 1))

for i in range(2, B):
    error = 0
    for z in range(2, i):
        if i % z == 0:
            error += 1
            break
    if error == 0:
        sosu_list.append(i)

for y in range(M, N+1):
    sosuCount = True
    if y == 1:
        sosuCount = False
    for i in sosu_list:
        if y != i and y % i == 0:
            sosuCount = False
            break
    if sosuCount:
        n_list.append(y)

for x in range(0, len(n_list)):
     print(n_list[x])

