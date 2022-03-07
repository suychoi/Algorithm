# ------------------------------------------------------------------------------------ 10250 번
# 풀이시간 24시간...

Count = int(input())

for i in range(Count):
    H, W, N = map(int, input().split())
    if N % H == 0:
        a = H * 100     #층수
        b = N //H  #호수
    else:
        a = (N % H) * 100
        b =  1 + N //H
    print(a + b)






