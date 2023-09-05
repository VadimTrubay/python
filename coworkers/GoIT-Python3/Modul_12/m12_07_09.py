""" Для копирования экземпляра класса Person из предыдущего примера реализуйте функцию copy_class_person.
В качестве параметра она принимает экземпляр класса person,
и возвращает "поверхностную" копию объекта с помощью функции copy из пакета copy.

Пример кода:

person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy_class_person(person)

print(copy_person == person)  # False
print(copy_person.name == person.name)  # True
... """

import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    copy_class = copy.copy(person)
    return copy_class
