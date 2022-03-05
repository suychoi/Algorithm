# ------------------------------------------------------------------------------------ 2869 번
# 풀이시간 30분

A, B, V = map(int, input().split())

up = A - B
except_last = V - A

if except_last % up > 0:
    D = except_last // up
    print(D+2)
else:
    D = except_last // up
    print(D + 1)

