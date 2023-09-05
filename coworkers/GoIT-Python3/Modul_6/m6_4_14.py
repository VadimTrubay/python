'''Реализуйте функцию add_employee_to_file(record, path),
 которая в файл (параметр path - путь к файлу) будет добавлять сотрудника (параметр record) в виде строки "Drake Mikelsson, 19".

Требования:

параметр record - сотрудник в виде строки вида "Drake Mikelsson, 19"
каждая запись в файл должна начинаться с новой строки.
необходимо, чтобы старая информация в файле тоже сохранялась,
поэтому при работе с файлом, откройте файл в режиме "a", добавьте сотрудника record в файл и закройте его
мы пока не используем менеджер контекста with'''

def add_employee_to_file(record, path):
    fh = open(path, 'a', encoding='utf-8')
    fh.write(record + '\n')
    fh.close()

add_employee_to_file("Drake Mikelsson, 19", 'test.txt')