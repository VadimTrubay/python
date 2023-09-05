''' Для предыдущей задачи реализуйте в классе Animal метод change_weight, который должен менять вес животного.

Вызовите функцию change_weight(12) для объекта animal и измените значение изначального веса с 10 на 12 единиц. '''


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return f"{'Gav-gav'}"

    def change_weight(self, weight):
        self.weight = weight


animal = Animal('Pusha', 2)
animal.change_weight(12)
print(animal.say())
print(animal.nickname)
print(animal.weight)
