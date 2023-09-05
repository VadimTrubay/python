from abc import ABC, abstractmethod


class Animals(ABC):
    """Абстрактный класс Животные (Друзья человека)"""

    def __init__(self, name, birth_date, command):
        self.__name = name
        self.__birth_date = birth_date
        self.__command = command

    def get_name(self) -> str:
        return self.__name

    def get_birth_date(self) -> str:
        return self.__birth_date

    def get_command(self) -> str:
        return self.__command

    @abstractmethod
    def print_animal(self):
        """Распечатать свойства животного"""
        pass
