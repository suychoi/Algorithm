# ------------------------------------------------------------------------------------ 11720 번
N = input()
num = list(input())

def sume(num):
    num_sum = 0
    for i in range(len(num)):
        num_sum += int(num[i])
    print(num_sum)

sume(num)