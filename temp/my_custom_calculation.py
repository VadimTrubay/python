# Напишите программу, которая будет выполнять простейшие
# математические операции с числами последовательно,
# принимая от пользователя операнды (числа) и оператор.
# Приложение работает с целыми и дробными числами.
# Приложение принимает один операнд или один оператор за один цикл запрос-ответ.
# Все операции приложение выполняет по мере поступления — одну за одной.
# Приложение выводит результат вычислений, когда получает от пользователя =.
# Приложение заканчивает свою работу после того, как выведет результат вычисления.
# Пользователь по очереди вводит числа и операторы.
# Если пользователь вводит оператор два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
# Если пользователь вводит число два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
# Приложение корректно обрабатывает ситуацию некорректного ввода (exception).


operand = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
operator = ['+', '-', '*', '/']
wait_for_number = True
temp = ''
result = 0

while True:
    try:
        user_input = input('input >>>: ')
        if user_input == '=':
            print(result)
            break

        elif result == 0:
            if not user_input in operator:
                result = float(user_input)
            else:
                print('input operand')
        else:
            if user_input in operator:
                temp = user_input
                continue
            if temp == '+':
                result += float(user_input)
                temp = ''
            elif temp == '-':
                result -= float(user_input)
                temp = ''
            elif temp == '*':
                result *= float(user_input)
                temp = ''
            elif temp == '/':
                result /= float(user_input)
                temp = ''
            else:
                print('input number or operand')
    except ValueError as err:
        print('input number')
        continue
