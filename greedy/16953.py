'''
08/01 19:17 ~ X
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다.
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
만들 수 없는 경우엔 -1 출력
'''

# B = A * 10 + 1
# B = A * 2

import sys
A, B = map(int, sys.stdin.readline().split())
n = 1
# bottom-up vs top-down 방식으로 접근,
# B -> A로 만들자.

while A != B:
    n += 1
    C = B
    if str(B)[-1] == '1':   # B%10 == 1:
        B = ( B -1 ) // 10  # B //= 10 몫!
    elif B % 2 == 0:
        B //= 2
    if C == B:
        print(-1)
        break
else:
    print(n)

# BFS 너비우선탐색 방식 풀이(Breadth First Search) ##############################3

from collections import deque
A, B = map(int, input().split())

# 큐를 준비하고, a 를 1과 함께 넣어준다.
q = deque()
q.append((A,1))

# 루프를 돌며 큐에 원소가 존재할 때 큐에서 pop 한다.
while(q):
    n, t = q.popleft()

    # b 보다 크다면, 다음 루프로 넘어간다.
    if n > B:
        continue
    # pop 한 원소가 b 와 같다면, 멈춘 뒤 연산 횟수를 출력한다.
    elif n == B:
        print(t)
        break
    q.append((int(str(n) + "1"), t + 1))
    q.append((n * 2, t + 1))
else:
    print(-1)






# b 보다 작다면, ..




