from abc import abstractmethod

from Programme.Animals.AnimalsAbstract import Animals


class PackAnimalsAbstract(Animals):
    """Абстрактный класс Вьючные животные"""

    @abstractmethod
    def eat(self):
        """Животное умеет есть"""
        pass

    @abstractmethod
    def speak(self):
        """Животное умеет подавать голос"""
        pass
