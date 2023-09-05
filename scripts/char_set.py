from string import *


def char_set(text):
    """
    Функция разбивает строку на буквы и символы без дублей в множестве set()
    """
    alphabet = ascii_lowercase
    char_set = set()
    symbol_set = set()
    for el in text:
        if el.lower() in alphabet:
            char_set.add(el)
        else:
            symbol_set.add(el)
    return print(f'Chars = {char_set}'), print(f'Symbols = {symbol_set}')
