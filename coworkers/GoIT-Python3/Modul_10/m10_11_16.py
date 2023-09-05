''' Создайте класс NumberString, наследуйте его от класса UserString,
определите для него метод number_count(self), который будет считать количество цифр в строке. '''

from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for i in self.data:
            if i.isdigit():
                count += 1
        return count


num = NumberString('vlad1990')
num2 = NumberString('1234556')

print(num.number_count())
print(num2.number_count())
