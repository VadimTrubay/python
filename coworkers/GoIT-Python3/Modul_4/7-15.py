num = int(input("Введите целое число (0 до 100): "))
sum = 0

while num > 0:
  sum += num
  num -= 1
print(sum)