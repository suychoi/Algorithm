# ------------------------------------------------------------------------------------ 2675 번
T = int(input())
P = []
Case = [[]]
for i in range(T-1):
    Case.append([])

for i in range(T):
     R, S = input().split()
     P.append([R, S])           #[['2', 'String'], ['3', 'STAR']]

     if i == T-1:
         for y in range (len(P)):
             B = list(P[y][1])                  #['S', 't', 'r', 'i', 'n', 'g']
             for z in range(len(B)):
                 ZZ = B[z] * int(P[y][0])
                 Case[y] += ZZ

for z in range(len(Case)):
    print(''.join(Case[z]))
