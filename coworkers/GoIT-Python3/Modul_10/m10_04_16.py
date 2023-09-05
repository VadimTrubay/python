''' Добавим в класс Animal переменную класса color, значение которой изначально равно "white",
и метод change_color, который должен менять значение переменной класса color.

Создайте экземпляры объекта: first_animal и second_animal

Вызовите функцию change_color("red") для любого экземпляра объекта Animal и измените значение переменной класса
color на "red". '''


class Animal:
    color = "white"

    def __init__(self, nickname, weight, color):
        self.nickname = nickname
        self.weight = weight
        self.color = color

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(color):
        Animal.color = color


first_animal = Animal('Aliska', 3, 'brown')
second_animal = Animal('Pusha', 2, 'white')
Animal.change_color('red')

print(first_animal.nickname + " " + first_animal.color)
print(second_animal.nickname + ' ' + second_animal.color)
print(Animal.color)
