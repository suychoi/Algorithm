'''
7/25 23:30 ~ X
카드 정렬하기

'''
import sys

N = int(sys.stdin.readline())
num = []

for i in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()
result = 0

for i in range(N):
    if N == 1:
        result = num[0]
    else:
        if i == 0 or i == 1:
            result += num[i] * (N-1)
        else:
            result += (num[i] * (N-i))

print(result)