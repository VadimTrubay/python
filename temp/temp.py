# count = 1
# summ = 0
#
# while count <= 1000:
#     summ += count
#     count += 1
# print(summ)

# def add(a, b, c):
#     print(f'Add slug equals {a + b + c}')


# user_input = int(input('enter n: '))
# res = 1
# for i in range(1, user_input + 1):
#     res *= i
# print(res)

# TRANSLATION = ("a", "b", "v", "g", "d", "e",
#                "j", "z", "i", "y", "k",
#                "l", "m", "n", "o", "p", "r",
#                "s", "t", "u", "f", "h", "c",
#                "ch", "sh", "sch", "", "i",
#                "", "e", "yu", "ya")

# start_index = ord('а')
# print(start_index)
# for i in range(1500):
#     print(f'{i}: {chr(i)}')

# string = 'Добрый, добрый Python - уроки для начинающих Ё ма ё'
# slug = ''
#
# for i in string:
#     if 1072 <= ord(i.lower()) <= 1103:
#         slug += TRANSLATION[(ord(i.lower()) - 1104)]
#     elif i == 'ё' or i == 'Ё':
#         slug += 'yo'
#     elif i in ' !?:;.,':
#         slug += '-'
#     else:
#         slug += i
#         # print(ord(i))
# slug = slug.replace('---', '-')
# slug = slug.replace('--', '-')
# print(slug)

a = [i for i in range(7)]
for i in iter(a):
    print(i)














