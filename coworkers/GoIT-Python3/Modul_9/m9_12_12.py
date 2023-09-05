''' Вернемся к нашей первой задаче с четвертого модуля и перепишем ее с помощью функции reduce.

payment = [1, -3, 4]


def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum
Напомним условие. У нас есть список показаний задолженностей по коммунальным услугам в конце месяца — список payment.
Задолженности могут быть отрицательными — у нас переплата, или положительными, если необходимо оплатить по счетам.
С помощью reduce просуммируйте положительные значения и сумму платежа в конце месяца верните из функции amount_payment. '''

from functools import reduce

def amount_payment(payment):
    temp = list(filter(lambda x: x > 0, payment))
    result = reduce(lambda x, y: x + y, temp)
    return result

print(amount_payment([1, -3, 4]))