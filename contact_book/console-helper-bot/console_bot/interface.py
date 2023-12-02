from abc import ABC, abstractmethod
import tkinter as tk

class Interface(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def show_output(self, output):
        pass

    @abstractmethod
    def get_input(self):
        pass

class ConsoleInterface(Interface):

    def show_output(self, output):
        print(output)

    def get_input(self, text):
        return input(text)


