
# 30분
N = int(input())

data = list(map(int, input().split()))
data.sort()
result = []
count = 0
for i in range(0, len(data)-1):
    result.append(data[i])
    if data[i] != data[i+1] or i == len(data)-2:    # 1 1 1 1 2 2 2 2 3 3 3 3
        count += len(result) // data[i]
        result.clear()
print(count)