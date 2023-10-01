from Programme.Animals.DomesticAnimals.DomesticAnimalsAbstract import DomesticAnimalsAbstract


class Cats(DomesticAnimalsAbstract):
    '''Класс кошки'''

    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date, command)

    def eat(self):
        """Кошка умеет есть"""
        pass

    def speak(self):
        """Кошка умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Кошка: кличка - {self.get_name()}, '
              f'дата рождения - {self.get_birth_date()}, '
              f'команды - {self.get_command()}')
