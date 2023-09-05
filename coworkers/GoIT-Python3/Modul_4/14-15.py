pool = 1000
quantity = int(input("Введите количество рассылок: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
    print('Выполнено деление на ноль!')

print(chunk)