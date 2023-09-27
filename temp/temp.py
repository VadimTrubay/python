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

# a = [i for i in range(7)]
# for i in iter(a):
#     print(i)

# m, n = list(map(int, input('>>>: ').split()))
# zero = []

# for i in range(m):
#     zero.append([0] * n)
# print(zero)
# for i in range(m):
#     for j in range(n):
#         zero[i][j] = 1
# print(zero)


# a = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 16],
#      ]

# for i in a:
#     for j in i:
#         print(j, end='\t')
#     print()

# for i in range(len(a)):
#     for j in range (i + 1, len(a)):
#         a[i][j], a[j][i] = a[j][i], a[i][j]


# for i in a:
#     for j in i:
#         print(j, end='\t')
#     print()


# TRIANGLE PASCAL

# N = 7
# RES = []

# for i in range(N):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if j != 0 and j !=i:
#             row[j] = RES[i-1][j-1] + RES[i-1][j]
#     RES.append(row)

# for i in RES:
#     print(i)


# d_inp = input('>>>: ')
#
# a = [int(i) for i in d_inp.rstrip().split(' ')]
# print(a)

# A = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# A = [[row[i] for row in A] for i in range(len(A[0]))]
#
# print(A)


# d = {'house': 'дом',
#      'car': 'машина',
#      'tree': 'дерево',
#      'river': 'река'}
#
# print(d['tree4'])








































