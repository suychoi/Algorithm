# ------------------------------------------------------------------------------------ 1157 번

T = str(input())
T = T.upper()
alp = []
for i in range (0, 26):
    alp.append(0)

def max_string(T):
    str_list = list(map(str, T))        #['S', 'A', 'F', 'E'] 65=A 90=Z
    for i in range(len(str_list)):
        S = str_list[i]
        for y in range(len(alp)):
            if S == chr(y+65):
                alp[y] += 1
    alpck = sorted(alp, reverse=True)
    if alpck[0] == alpck[1]:
        return print("?")
    else:
        return print(chr(alp.index(max(alp)) + 65))

max_string(T)


