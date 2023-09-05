#Способ 1 - перебрать положительные значения и суммировать их
def amount_payment(payment):
    result = 0
    for char in payment:
      if char > 0:
        result += char
        return result

# #Способ 2 - удалить со списка отрицательные значения и посчитать сумму списка
# def amount_payment(payment):
#     result = 0
#     for char in payment:
#       if char <= 0:
#         payment.remove(char)
#     result = sum(payment)
#     return result