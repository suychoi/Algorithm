N = list(input())
result = 0
for i in range(len(N)):
    if result == 0:
        result += int(N[i])
    else:
        if int(N[i]) == 0:
            continue
        elif int(N[i]) == 1 or result == 1:
            result += int(N[i])
        else:
            result *= int(N[i])
print(result)

