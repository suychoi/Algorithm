'''
7/25 23:30 ~ X
카드 정렬하기
계산한 값을 다시 list에 넣어야 함!!!

heapq : 트리와 리스트의 장점 결합,
트리구조 : 요소 삽입 및 최솟값(or 최대값)의 제거시 발생하는 요소의 검색 및 swap의 수가
        일반적인 리스트를 사용할 때보다 현저히 작다.
리스트 : 완전 이진트리는 리스트로 코딩할 수 있다. 리스트가 클래스보다 빠르다.

# 참조 : https://namu.wiki/w/%ED%9E%99%20%ED%8A%B8%EB%A6%AC

'''
from heapq import *
import heapq
import sys

N = int(sys.stdin.readline())
num = []
result = 0
for _ in range(N):
    heappush(num, int(sys.stdin.readline()))

if N == 1:
    print(0)
else:
    while len(num) > 1:
        x = heapq.heappop(num)
        y = heapq.heappop(num)
        result += (x+y)
        heappush(num, (x+y))
    print(result)
