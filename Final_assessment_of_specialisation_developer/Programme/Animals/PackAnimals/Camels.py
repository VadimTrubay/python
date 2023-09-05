from Programme.Animals.PackAnimals.PackAnimalsAbstract import PackAnimalsAbstract


class Camels(PackAnimalsAbstract):
    '''Класс верблюды'''

    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date, command)

    def eat(self):
        """Верблюд умеет есть"""
        pass

    def speak(self):
        """Верблюд умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Верблюд: кличка - {self.get_name()}, '
              f'дата рождения - {self.get_birth_date()}, '
              f'команды - {self.get_command()}')
