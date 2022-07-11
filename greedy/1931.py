"""
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데
이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

(1,4), (5,7), (8,11), (12,14) 를 이용할 수 있다.

"""

from operator import  itemgetter
import sys
N = int(sys.stdin.readline())
end_time = 0
time =[]

for i in range(N):
    reservation = list(map(int, sys.stdin.readline().split()))
    time.append(reservation)
    if end_time < reservation[1]:
        end_time = reservation[1]

# 끝나는 시간 순 정렬
time.sort(key=itemgetter(1))

# start_time = end_time
#
# for n in range(N):
#     if start_time > time[n][0]:
#         start_time = time[n][0]

# time_ck = [True] * (end_time - start_time)
time_ck = [True] * end_time

cnt = 0

for i in time:
    if all(time_ck[time[i][0]:time[i][1]+1]):
        time_ck[time[i][0]:time[i][1]] = [False] * (time[i][1]-time[i][0])
        cnt += 1
print(cnt)

for z in time:
    print(z)




