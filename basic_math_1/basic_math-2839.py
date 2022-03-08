# ------------------------------------------------------------------------------------ 2839 번
# 풀이시간
#

N = int(input())

def delivery(N):
    for n in range(0, 1002):
        a_case = [x for x in range(0, n+1)]     #[0, 1, 2]
        b_case = [x for x in range(n, -1, -1)]  #[2, 1, 0]
        for i in range (len(a_case)):
            if (a_case[i] * 3) + (b_case[i] * 5) == N:
                return a_case[i] + b_case[i]
                break

    return -1

result = delivery(N)
print(result)

