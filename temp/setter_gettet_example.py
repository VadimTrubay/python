from string import ascii_letters

class Person:
    def __init__(self, fio, passport, age, weight):
        self.verify_fio(fio)

        self.fio = fio
        self.passport = passport
        self.age = age
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('has been string')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('error format')

        let = ascii_letters
        for i in f:
            if len(i) < 1:
                raise TypeError('has been too many one symbol')
            if len(i.strip(let)) != 0:
                raise TypeError('only letter')

    @classmethod
    def verify_passport(cls, passport):
        pass


p = Person('vadim trub valent', 12332, 32, 12)
