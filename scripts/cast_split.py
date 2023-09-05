from string import *


def cast_split(text):
    """
    Функция делает разбивку строки на список слов и символов(аналог split())
    """
    alphabet = ascii_lowercase
    words = []
    start = 0
    for index, char in enumerate(text):
        if not char.lower() in alphabet:
            word = text[start:index]
            words.append(word.strip())
            start = index
    words.append(words[-1])
    return print(words)
