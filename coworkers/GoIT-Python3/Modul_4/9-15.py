first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
if (first < second):
    nod = first
else:
    nod = second
while not(first % nod == 0 and second % nod == 0):
    nod = nod - 1
print(nod)