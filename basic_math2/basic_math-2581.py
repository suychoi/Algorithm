# ------------------------------------------------------------------------------------ 2581 번
# 풀이시간 00:35~00:47


M = int(input())
N = int(input())
num_list = []
for i in range(M, N+1):
    error = 0
    if i == 1:
        continue
    elif i == 2:
        num_list.append(i)
        continue
    for z in range(2, i):
        if i % z == 0:
            error += 1
            break
    if error == 0:
        num_list.append(i)

if len(num_list) > 0:
    print(sum(num_list))
    print(num_list[0])
else:
    print(-1)


