# ------------------------------------------------------------------------------------ 2908 번

A, B = input().split()
A_list = list(A)
B_list = list(B)
A_list.reverse()                            # reverse (반대로 정렬)
B_list.reverse()
A_list = ''.join(A_list)                    # join
B_list = ''.join(B_list)
if int(A_list) > int(B_list):
    print(int(A_list))
elif int(B_list) > int(A_list):
    print(int(B_list))

