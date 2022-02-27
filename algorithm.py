# a, b = input().split()
# if int(a) > int(b):
#     print(">")
# elif int(a) < int(b):
#     print("<")
# elif int(a) == int(b):
#     print("==")
#
# # 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# a = int(input())
# if 90 <= a <= 100:
#     print("A")
# elif 80 <= a < 90:
#     print("B")
# elif 70 <= a < 80:
#     print("C")
# elif 60 <= a < 70:
#     print("D")
# else :
#     print("F")
#
# print('FFFFFFDCBAA'[int(input())//10])
#
# a = int(input())
# if a % 4 == 0 and a % 100 != 0:
#     print("1")
# elif a % 400 == 0:
#     print("1")
# else:
#     print("0")
#
# a = int(input())
# b = int(input())
# if a < 0 and b < 0:
#     print("3")
# elif a > 0 and b > 0:
#     print("1")
# elif a < 0 and b > 0:
#     print("2")
# elif a > 0 and b < 0:
#     print("4")
#
# H, M = input().split()
# if int(M) >= 45:
#     print(H,str(int(M)-45))
# elif int(M) < 45 and int(H) == 0:
#     print(str(int(H)+23),str(int(M)+15))
# elif int(M) < 45:
#     print(str(int(H)-1),str(int(M)+15))
#
# a, b = map(int, input().split())
# print((a - (b < 45)) % 24, (b - 45) % 60)
#
# n = int(input())
# for x in range(9):
#     print( str(n) + " * " + str((x+1)) + " = " + str(int(n * (x+1))))
#
# n = int(input())
# for x in range(n):
#     a, b = input().split()
#     print(int(a) + int(b))
#
# n = int(input())
# y = 0
# for x in range(n):
#     y = y + (x+1)
# print(y)
#
#
#
# n = int(input())
# for x in range(n):
#     a, b = map(int, sys.stdin.readline().split())       #반복문으로 여러 번 입력 받을 때
#     print(a + b)
#
# n = int(input())
# for x in range(n):
#     print(n-x)
#
# import sys
# T = int(input())
# for x in range(T):
#     a, b = map(int, sys.stdin.readline().split())
#     print("Case #" + str(int(x)+1)+ ": " + str(a) + " + " + str(b) + " = " + str(a + b))
#
# T = int(input())
# for x in range(T):
#     print("*" * (x+1))
#

# N = int(input())
# for x in range(N):
#     print((" " * (N - (x+1))) + ("*" * (x+1)))

# N, X = input().split()
# A = list(map(int, input().split()))
# for x in A:
#     if x < int(X):
#         print(x)

## While

# import sys
# while True:
#     try:
#         a, b = map(int, sys.stdin.readline().split())
#         print(a + b)
#     except:
#         break

# N = int(input())
# T = N
# C = 0
# while True:
#     C = C+1
#     if N < 10:
#         N = int("0" + str(N))
#
#     a = N//10
#     b = N%10
#     c = (a + b)
#     M = (b * 10) + (c%10)
#
#     if M == T:
#         print(C)
#         break
#     else:
#         N = M
                                                                ##List

# N = int(input())
# A = [0 for i in range(N)]
# A = list(map(int, input().split()))
# print(str(min(A)) + " " + str(max(A)))

                                                                # 2526 번 문제, max 를 ASCII 로 읽을 수 있다(조심)
# import sys
# A = [0 for i in range(9)]
# for x in range(9):
#     A[x] = int(sys.stdin.readline().strip())
#
# print(max(A))
# print(A.index(max(A))+1)

# import sys
# Num = [0 for i in range(3)]
# for x in range(3):
#     Num[x] = int(sys.stdin.readline().strip())
# a = SUM.count('0')                                    #요소 count
# print(a)

# import sys
# Num = set()
# for x in range(10):
#     A = int(sys.stdin.readline().strip())
#     Num.add(A % 42)
# print(len(Num))                                      # 요소 수

# import sys
# N = int(input())
# Num = list(map(int, sys.stdin.readline().split()))          #여러번 입력
# #a = [int(x) for x in input().strip.split()]
# # print(Num.pop(Num.index(max(Num))))
# M = max(Num)
# for x in range(N):
#     Num[x] = Num[x] / M * 100
# print(sum(Num) / N)                                     # 요소 총 합

# import sys
# N = int(input())
# for x in range(N):
#     Q = sys.stdin.readline().strip()
#     R = list(Q)                                             # 문자열을 List로
#     Sum = 0
#     S = 0
#     for y in range(len(R)):
#         if R[y] == 'O':
#             S = S + 1
#             Sum = Sum + S
#         elif R[y] == 'X':
#             S = 0
#     print(Sum)

# import sys
# C = int(input())
# for x in range(C):
#     Q = list(map(int, sys.stdin.readline().split()))
#     AVG = sum(Q[1:]) / Q[0]                                  #Index Slicing
#     Num = 0
#     for y in range(len(Q)-1):
#         if Q[y+1] > AVG:
#             Num = Num + 1
#     Z = round(Num/Q[0]*100, 3)
#     print(f'{Z:.3f}' + "%")                                 #소수점 3자리까지 출력 하기( format )
#

# N = 10000
# A = list(range(1, N))
#
# def solve(x):
#     y = x
#     for z in range(len(str(x))):                                #자리수 계산
#         y = y + int(str(x)[z])
#     if y in A:
#         A.remove(y)
#     return A
#
# for x in range(N):
#     solve(x+1)
#
# for i in range(len(A)):
#     print(A[i])
# ------------------------------------------------------------------------------------ 1065번
# num = int(input()) # 1001
#
# def hansu(num):
#     hansu_count = 0
#     for z in range(1, num+1):
#         num_list = list(map(int, str(z)))
#         if z < 100:
#             hansu_count = hansu_count + 1
#         elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
#             hansu_count = hansu_count + 1
#     print(hansu_count)
#
# hansu(num)



# ------------------------------------------------------------------------------------문자열
#
# A = ord(input())
# print(A)

# ------------------------------------------------------------------------------------ 11720 번
# N = input()
# num = list(input())
#
# def sume(num):
#     num_sum = 0
#     for i in range(len(num)):
#         num_sum += int(num[i])
#     print(num_sum)
#
# sume(num)
# ------------------------------------------------------------------------------------ 10809 번
#
# S = input()
# A = list(map(str, S.lower()))
# result = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
# # baekjoon
#
# for i in range(0, 26):
#     for x in range (len(A)):
#         if result[i] == -1 and chr(i+97)==A[x]:                           아스키 코드(숫자->문자) 변환
#             result[i] = x
# for z in range(len(result)):
#     print(str(result[z]), end=" ")                                        결과값 일자로 출력



# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------



































