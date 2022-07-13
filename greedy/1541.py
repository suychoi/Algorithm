"""
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다.

그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
"""
# 문자와 기호로 분류 - 가 붙을때 다음 - 가 나오기 전까지 괄호로 묶는다.

# 2회차
f = input().split('-')
f_list = []

for n in f:
    y = list(map(int, n.split('+')))
    f_list.append(sum(y))

result = 0
for y in range(len(f_list)):
    if y == 0:
        result = f_list[y]
    else:
        result -= f_list[y]
print(result)
###############################################################################
# 1회차 ( eval 활용 )
# formula = input().split('-')
#
# result = 0
# for num in range(len(formula)):
#     f1 = formula[num].lstrip('0')
#     f1 = f1.strip()
#     if num == 0:
#         result = eval(f1)
#     elif formula[num]:
#         result -= eval(f1)
#
# print(result)

