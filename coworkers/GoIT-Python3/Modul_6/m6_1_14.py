'''Пусть у нас есть текстовый файл, который содержит данные с месячной заработной платой по каждому разработчику компании.

Пример файла:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
Как видим, структура файла — это фамилия разработчика и значение его заработной платы, разделенной запятой.

Разработайте функцию total_salary(path) (параметр path - путь к файлу),
 которая будет разбирать построчно файл и возвращать общую сумму заработной платы всех разработчиков компании.

Требования к задаче:

функция total_salary возвращает значение типа float
для чтения файла функция total_salary использует только метод readline
мы пока не используем менеджер контекста with'''




import re
def total_salary(path):
    file = open(path, 'r')
    result = 0
    while True:
        line = file.readline()
        list = re.findall(r"\d+", line)
        for i in list:
            result += float(i)
        if not line:
          break
    file.close()

    return result

fh = open('test.txt', 'w')
fh.write('Alex Korp,3000,Nikita Borisenko,2000,Sitarama Raju,1000')
fh.close()

print(total_salary('test.txt'))
