# ------------------------------------------------------------------------------------ 10809 번

S = input()
A = list(map(str, S.lower()))
result = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
# baekjoon

for i in range(0, 26):
    for x in range (len(A)):
        if result[i] == -1 and chr(i+97)==A[x]:                         #  아스키 코드(숫자->문자) 변환
            result[i] = x
for z in range(len(result)):
    print(str(result[z]), end=" ")                                       # 결과값 일자로 출력
