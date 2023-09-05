''' В прошлую задачу добавим класс Owner — владельца собаки.
У класса есть три атрибута: имя — name, возраст — age и адрес — address.
Также необходимо реализовать метод info, который возвращает словарь с ключами 'name', 'age' и 'address',
и значениями равными соответствующим свойствам экземпляра класса.

Реализовать для класса Dog атрибут owner, который будет экземпляром класса Owner.
Добавить в класс Dog метод who_is_owner, который возвращает результат вызова метода info у экземпляра класса Owner,
т.е. словарь с ключами 'name', 'age' и 'address' владельца. '''

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        dict = {'name': self.name, 'age': self.age, 'address': self.address}
        return dict


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        dict = {'name': self.owner.name, 'age': self.owner.age, 'address': self.owner.address}
        return dict


Luda = Owner('Luda', 42, 'Odessa')
Aliska = Dog("Aliska", 4, 'chihuahua', Luda)

print(Luda.info())
print(Aliska.owner.name)
print(Aliska.who_is_owner())
