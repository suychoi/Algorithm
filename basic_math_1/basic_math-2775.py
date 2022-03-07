# ------------------------------------------------------------------------------------ 2775 번
# 풀이시간  힌트참고해서 1시간
#


case = int(input())

for i in range(case):
    k = int(input())
    n = int(input())
    if n == 1:
        print(1)
        continue
    room_num = [x for x in range(1, n+1)]  # 0층 리스트 1~N
    for Y in range(k):
        for Z in range(n-1, -1, -1):
            room_num[Z] += sum(room_num[:Z])
    print(room_num[-1])



