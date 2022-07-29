# 11100001110001
# 20분 정도..?

S = input()
S_0 = S.split("1")
S_1 = S.split("0")

S_0 = list(filter(None, S_0))
S_1 = list(filter(None, S_1))

if len(S_0) >= len(S_1):
    print(len(S_1))
else:
    print(len(S_0))




