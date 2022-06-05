"""
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
"""
# import sys
# N = int(sys.stdin.readline())
# K = 1
# if N == 0:
#     print(1)
# else:
#     for i in range(1, N+1):
#         K *= i
#     print(K)

def factorial(n):
    k = 1
    if n > 1:
        k = n * factorial(n-1)
    return  k

import sys
n = int(sys.stdin.readline())
print(factorial(n))