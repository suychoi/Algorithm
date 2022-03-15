#11047  20분정도

N, K = map(int, input().split())

coin = []
for i in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)
count = 0
for y in range(N):
    if K % coin[y] == 0:
        count += K // coin[y]
        break
    elif K > coin[y]:
        v = K // coin[y]
        count += v
        K -= v * coin[y]
print(count)