# ------------------------------------------------------------------------------------ 1712 번

N = int(input())
words = []
for i in range(N):
    X = str(input())
    words.append(X.lower())

for y in range(N):
    w = words[y]
    for z in range(len(w)-1):
        if w[z] == w[z+1]:
            pass
        elif w[z] in w[z+1:]:
            N -= 1
            break

print(N)
