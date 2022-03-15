#11399

N = int(input())
data = list(map(int, input().split()))
data.sort()
sum = 0
for i in range(N):
    sum += data[i] * (len(data)-i)
print(sum)