from abc import abstractmethod

from Programme.Animals.AnimalsAbstract import Animals


class DomesticAnimalsAbstract(Animals):
    """Абстрактный класс Домашние животные"""

    @abstractmethod
    def eat(self):
        """Животное умеет есть"""
        pass

    @abstractmethod
    def speak(self):
        """Животное умеет подавать голос"""
        pass
