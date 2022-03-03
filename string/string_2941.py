# ------------------------------------------------------------------------------------ 2941 번

T = str(input())                                        #replace 함수
T = T.replace('c=','a')
T = T.replace('c-','a')
T = T.replace('dz=','a')
T = T.replace('d-','a')
T = T.replace('lj','a')
T = T.replace('nj','a')
T = T.replace('s=','a')
T = T.replace('z=','a')

print(len(list(map(str, T))))


