import re


def normalize(name: str) -> str:
    CYRILLIC = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    TRANSLATION = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
        "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja")

    NEW_TRANSL = {}
    for c, l in zip(CYRILLIC, TRANSLATION):
        NEW_TRANSL[ord(c)] = l
        NEW_TRANSL[ord(c.upper())] = l.upper()
    normalize_name = name.translate(NEW_TRANSL)
    normalize_name = re.sub(r'\W', '_', normalize_name)
    return normalize_name

print(normalize('новый файл'))