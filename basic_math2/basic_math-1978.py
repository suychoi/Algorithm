# ------------------------------------------------------------------------------------ 1978 번
# 풀이시간


N = int(input())
number = map(int, input().split())

def sosu():
    count = 0
    for num in number:
        error = 0
        if num > 1:
          if num == 2:
              count += 1
          for i in range(3, num-1):
              if num % i == 0:
                error += 1
                break
          if error == 0:
              count += 1
    return print(count)
sosu()