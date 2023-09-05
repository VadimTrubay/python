'''В предыдущей задаче мы записали сотрудников в файл в следующем виде:

Robert Stivenson, 28
Alex Denver, 30
Drake Mikelsson, 19
Выполним теперь обратную задачу и создадим функцию read_employees_from_file(path),
 которая будет читать данные из файла и возвращать список сотрудников в виде:

['Robert Stivenson, 28', 'Alex Denver, 30', 'Drake Mikelsson, 19']
Помните про присутствие символа конца строки \n при чтении данных из файла.
Его необходимо убирать при добавлении прочитанной строки в список.

Требования:

прочтите содержимое файла, используя режим "r".
мы пока не используем менеджер контекста with
верните из функции список сотрудников из файла'''

def read_employees_from_file(path):
    fh = open(path, 'r')
    list = []
    while True:
        lines = fh.readlines()
        for i in lines:
            j = i.removesuffix('\n')
            list.append(j)
        if not lines:
            break
    fh.close()
    return list



