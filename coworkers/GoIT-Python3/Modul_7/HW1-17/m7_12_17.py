'''Реализуйте функцию file_operations(path, additional_info, start_pos, count_chars),
которая добавляет дополнительную информацию в файл по пути path из параметра additional_info,
и после этого возвращает строку с позиции start_pos длиной count_chars.

Требования:

функция должна открывать файл с помощью with по пути path в режиме добавления информации
записывать в конец файла строку additional_info
после записи функция должна открыть тот же файл для чтения
прочитать и вернуть строку с позиции start_pos длиной count_chars с помощью функции seek.
Важно: для прохождения задачи необходимо использовать менеджер контекста with, методы seek, write и read.'''


def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as f:
        f.write(additional_info)
    with open(path, 'r') as f:
        f.seek(start_pos)
        return f.read(count_chars)
