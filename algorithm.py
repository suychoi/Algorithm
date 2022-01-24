import sys

# a, b = input().split()
# if int(a) > int(b):
#     print(">")
# elif int(a) < int(b):
#     print("<")
# elif int(a) == int(b):
#     print("==")

# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
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

# a = int(input())
# if a % 4 == 0 and a % 100 != 0:
#     print("1")
# elif a % 400 == 0:
#     print("1")
# else:
#     print("0")

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

# n = int(input())
# for x in range(9):
#     print( str(n) + " * " + str((x+1)) + " = " + str(int(n * (x+1))))

# n = int(input())
# for x in range(n):
#     a, b = input().split()
#     print(int(a) + int(b))

# n = int(input())
# y = 0
# for x in range(n):
#     y = y + (x+1)
# print(y)


#
# n = int(input())
# for x in range(n):
#     a, b = map(int, sys.stdin.readline().split())   #반복문으로 여러 번 입력 받을 때
#     print(a + b)

# n = int(input())
# for x in range(n):
#     print(n-x)

import sys
T = int(input())
for x in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #" + str(int(x)+1)+ ": " + str(a) + " + " + str(b) + " = " + str(a + b))









