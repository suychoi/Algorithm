#1931  23:20 ~
#today is my birthday

N = int(input())

end = 0
time_table = []
for i in range(N):
    S, D = map(int, input().split())
    time_table.append([S, D])
    if end < D :
        end = D
#[[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
limit = [False] * end
count = 0
for z in range(end):        #최대 시간까지 반복
    for i in range(N):      #예약 체크
        A = int(time_table[i][0])    #1 3
        B = int(time_table[i][1])    #4 5
        if B - A == z+1:
            chek = True
            for k in range(A, B-1):   #12시 부터
                if limit[k]:   #구간 모두가 False 여야됨 예약없는(True 인 경우 chk false)
                    chek = False
            if chek:
                count += 1
                for y in range(A, B-1):
                    limit[y] = True
                print(A, B)
print(limit)
print(count)


