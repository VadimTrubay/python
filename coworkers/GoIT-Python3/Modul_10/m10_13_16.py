''' Как мы уже говорили, полиморфизм — это способность программы выбирать различные реализации
при вызове операций с одним и тем же названием.
Но полиморфизм — это также способность объектов притворяться чем-то другим.
В приведённом выше примере Chupakabra притворялась собакой и кошкой.
Для кода из задания вам необходимо реализовать класс CatDog, не используя наследование от класса Animal,
но, чтобы экземпляр класса CatDog вел себя так же, как экземпляр класса Cat, т.е. он должен притвориться,
что он класс Cat. '''

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return "MeowWoof"


catdog = CatDog('Pusha', 3)
print(catdog.say())