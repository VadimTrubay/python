from Programme.Animals.DomesticAnimals.DomesticAnimalsAbstract import DomesticAnimalsAbstract


class Dogs(DomesticAnimalsAbstract):
    '''Класс собаки'''

    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date, command)

    def eat(self):
        """Собака умеет есть"""
        pass

    def speak(self):
        """Собака умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Собака: кличка - {self.get_name()}, '
              f'дата рождения - {self.get_birth_date()}, '
              f'команды: {self.get_command()}')