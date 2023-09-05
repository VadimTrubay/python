# from random import randint
#
# N = 10
# a = []
# for i in range(N):
#     a.append(randint(1, 99))
# print(a)
#
# for i in range(len(a) - 1):
#     for j in range(len(a) - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
# print(a)


import turtle

t = turtle.Pen()
for i in range(100):
    t.forward(i)
    t.left(90+1)

