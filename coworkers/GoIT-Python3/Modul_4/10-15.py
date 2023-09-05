from stringprep import in_table_a1


num = int(input("Введите целое число (0 для выхода): "))
sum = 0
while num != 0:
    for i in range(num +1):
      sum += i
      
        
    num = int(input("Введите целое число (0 для выхода): "))
print(sum)
print(i)