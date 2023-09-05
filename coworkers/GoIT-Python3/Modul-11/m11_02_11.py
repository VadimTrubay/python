''' У класса Point через конструктор __init__ объявлены два атрибута: координаты x и y.
Скройте доступ к ним с помощью двойного подчеркивания: __x и __y

Реализуйте для класса Point механизмы setter и getter к атрибутам __x и __y с помощью декораторов property и setter. '''


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = int(value)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = int(value)