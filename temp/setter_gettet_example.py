from string import ascii_letters

class Person:
    def __init__(self, fio, passport, age, weight):
        self.verify_fio(fio)

        self.__fio = fio
        self.passport = passport
        self.age = age
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('has been string')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('error format fio')

        let = ascii_letters
        for i in f:
            if len(i) < 1:
                raise TypeError('has been too many one symbol')
            if len(i.strip(let)) != 0:
                raise TypeError('only letter')

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 14 or age > 120:
            raise TypeError('age has been in range (14-120)')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('weight has been float > 20 kg')

    @classmethod
    def verify_passport(cls, passport):
        if type(passport) != str:
            raise TypeError('passport has been string')

        p = passport.split()
        if len(p) != 2 or len(p[0]) != 2 or len(p[1]) != 6:
            raise TypeError('error format passport')

        if not p[1].isdigit():
            raise TypeError('passport has been digit')

    @property
    def fio(self):
        return self.__fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport

p = Person('vadim trubay valent', 'kk 222275', 32, 34.0)

print(p.__dict__)

p.age = 99
p.weight = 44.7
p.passport = 'rr 234567'

print(p.__dict__)




