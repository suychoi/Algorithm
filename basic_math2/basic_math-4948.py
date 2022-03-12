# ------------------------------------------------------------------------------------ 4948 번
# 풀이시간 12시간
limit = (123456 * 2 + 1)

# 소수 목록을 만들어 놓는것
sosu_list = [True] * limit  # [True, True, True, True, ....]
for i in range(2, int(limit**(0.5))+1):  # i 는 나눠보는 까지...
    if sosu_list[i]:
        for z in range(2 * i, limit, i):  # 배수를 false로 바꾼다.
            sosu_list[z] = False
# print("0 = " + str(sosu_list[0]))   #True 가 소수다!
# print("1 = " + str(sosu_list[1]))
# print("2 = " + str(sosu_list[2]))
# print("3 = " + str(sosu_list[3]))
# print("4 = " + str(sosu_list[4]))
# print("5 = " + str(sosu_list[5]))
# print("6 = " + str(sosu_list[6]))

while True:
    N = int(input())
    if N == 0:
        break
    elif N == 1:
        print(1)
        continue
    count = 0
    for i in range(N+1, 2*N +1):    #소수 목록에서 N ~ 2N 까지의 True 개수를 세서 출력
        if sosu_list[i]:
            count += 1

    print(count)



#===================================================================================================

# import math
#
# while True:
#     N = int(input())
#     if N == 0:
#        break
#     elif N == 1:
#         print(1)
#         continue
#
#     count = 0
#     for i in range(N+1, (N*2 +1)):
#         for y in range(2, int(math.sqrt(i)) +1):
#             if i % y == 0:
#                 break
#         else:
#             count += 1
#     print(count)



#===================================================================================================




# import math
# import sys
#
# def ck(i, y):
#     # print("i 는" + str(i) + " y 는" + str(y))
#     if i % y == 0:
#         return False
#     if int(math.sqrt(i)) == y:
#         return True
#
# def sosu(num):
#     count = 0
#     for i in range(num+1, (num*2 +1)):
#         # error = False
#         if i == 2:
#             return print(1)
#         else:
#             for y in range(2, int(math.sqrt(i)) +1):
#                 result = ck(i, y)
#                 if result == True:
#                     count += 1
#                 elif result == False:
#                     break
#     return print(count)
#
# while True:
#     N = int(sys.stdin.readline())
#     if N != 0:
#         sosu(N)
#     else:
#         break



#===================================================================================================


#
# def sosu(num):
#     B = (int(math.sqrt(num) + 1))
#     sosu_list = []
#     count = 0
#
#     for i in range(2, num):
#         error = 0
#         for z in range(2, int(math.sqrt(i) + 1)):
#             if i % z == 0:
#                 error += 1
#                 break
#         if error == 0:
#             sosu_list.append(i)
#
#     for y in range(num +1, (num*2 +1)):
#         sosuCount = True
#         if y == 2:
#             return print(1)
#         for i in sosu_list:
#             if y != i and y % i == 0:
#                 sosuCount = False
#                 break
#         if sosuCount:
#             count += 1
#     print(count)
#
# while True:
#     N = int(sys.stdin.readline())
#     if N != 0:
#         sosu(N)
#     else:
#         break



