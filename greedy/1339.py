'''
민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.
단어 수학 문제는 N개의 단어로 이루어져 있으며,
각 단어는 알파벳 대문자로만 이루어져 있다.
이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다.
같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.
예를 들어, GCF + ACDEB를 계산한다고 할 때,
A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면,
두 수의 합은 99437이 되어서 최대가 될 것이다.
N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

'''

import sys
N = int(sys.stdin.readline())

alp = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alp_list = []
result = 0
s = []

for i in range(N):
    s.append(sys.stdin.readline().strip())

for a in s:
    for i in range(len(a)):
        num = 10 ** (len(a) - i -1)
        alp[a[i]] += num

for v in alp.values():
    if v > 0:
        alp_list.append(v)

sorted_list = sorted(alp_list, reverse=True)
for i in range(len(sorted_list)):
    result += sorted_list[i] * (9-i)

print(result)

