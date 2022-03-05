# ------------------------------------------------------------------------------------ 2292 번
# 풀이시간 120분

import sys
N = int(sys.stdin.readline())
cycle = 1       #사이클 수
last_num = 1    #사이클 당 최고 숫자

if N == 1 :
    print(1)
else:
    while True:
        if N <= last_num:
            print(cycle)
            break
        else:
            last_num += 6 * cycle
            cycle += 1


