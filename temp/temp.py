# count = 1
# summ = 0
#
# while count <= 1000:
#     summ += count
#     count += 1
# print(summ)

# def add(a, b, c):
#     print(f'Add result equals {a + b + c}')


user_input = int(input('enter n: '))
res = 1
for i in range(1, user_input+1):
    res *= i
print(res)





















