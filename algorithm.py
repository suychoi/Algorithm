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

H, M = input().split()
H = int(H)
M = int(M)
if M >= 45:
    print(H + " " + (M-45))
elif M < 45 and H == 0:
    print(H+23 + " " + (M + 15))
elif M < 45:
    print((H-1) + " " + (M + 15))














