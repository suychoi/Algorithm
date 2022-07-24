'''
7/24 15:45 ~ 16:21
4
2 3 1
5 2 4 1

'''


town = int(input())
length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

total_price = oil_price[0] * length[0]
compare = oil_price[0]

for i in range(town-2):
    if compare >= oil_price[i+1]:
        compare = oil_price[i+1]
        total_price += compare * length[i+1]
    elif compare < oil_price[i+1]:
        total_price += compare * length[i+1]

print(total_price)

######################################
# 더 나은 풀이법
# for 문을 돌면서 매번 더해준다.
# 지금까지 지난 주유소의 가격중 가장 작은 값으로 도로를 앞으로이동한다는 개념 .. !
# 더 싼 값이 나올때까지 주유한다는 가정이므로..!
# 따라서 주유소 가격은 지금까지의 주유소 가격보다 작을 때 갱신됨.

T = int(input())
l = list(map(int, input().split()))
price = list(map(int, input().split()))

res = 0
m = price[0]
for i in range(T-1):
    if price[i] < m:
        m = price[i]
    res += m * l[i]

print(res)



