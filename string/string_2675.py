# ------------------------------------------------------------------------------------ 2675 번
T = int(input())
P = []
Case = []
for i in range(T):
     R, S = input().split()
     P.append([R, S])
     if i == T-1:
         for y in range (len(P)):
             B = list(P[y][1])                  #ABC
             for z in range(len(B)):
                 ZZ = B[z] * int(P[y][0])
                 Case.append([y][ZZ])

# for i in range(len(Case)):
print(Case)
# T = input()
# print((T * 10))
#




# N, X = input().split()
# A = list(map(int, input().split()))
