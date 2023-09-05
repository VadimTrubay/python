def counter_char(text):
    """
    Функция считает количество вхождений символа в строке
    """
    dict_counter = {}
    for char in text:
        # try:
        #     count = dict_counter[char]  # получаем значение по ключу
        # except KeyError:
        #     count = 0
        count = dict_counter.get(char, 0)  # получаем значение по ключу
        count += 1
        dict_counter[char] = count  # записываем значение по ключу
    return print(dict_counter)