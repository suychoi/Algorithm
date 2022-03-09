# ------------------------------------------------------------------------------------ 1978 번
# 풀이시간


N = int(input())
number = map(int, input().split())
count = 0

for num in number:
    error = 0
    if num == 1:
        continue
    if num == 2:
        count += 1
        continue
    for i in range(2, num):
      if num % i == 0:
        error += 1
        break
    if error == 0:
        count += 1
print(count)
