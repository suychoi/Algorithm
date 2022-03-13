# ------------------------------------------------------------------------------------ 9020 번
# 풀이시간 20붐ㄴ


limit = (10001)
sosu_list = [True] * limit
for i in range(2, int(limit**(0.5))+1):
    if sosu_list[i]:
        for z in range(2 * i, limit, i):
            sosu_list[z] = False
sosu_list[0] = False
sosu_list[1] = False

T = int(input())

def sosu():
    n = int(input())
    for y in range(n//2, 0, -1):
        if sosu_list[y]:
            for z in range(n//2, limit):
                if sosu_list[z]:
                    if y + z == n:
                        return print(str(y) + " " + str(z))

for i in range(T):
    sosu()
