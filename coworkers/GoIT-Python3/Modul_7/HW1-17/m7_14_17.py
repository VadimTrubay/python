'''Напишите функцию to_indexed(start_file, end_file), которая будет считывать содержимое файла,
добавлять к считанным строкам порядковый номер и сохранять их в таком виде в новом файле.

Каждая строка в созданном файле должна начинаться с ее номера, двоеточия и пробела,
после чего должен идти текст строки из исходного файла. Нумерация строк идет от 0.'''

# def to_indexed(start_file, end_file):
#     with open(start_file, 'r') as reader:
#         text = reader.readlines()
#     with open(end_file) as writer:
#         count = 0
#         for i in text:
#             str = 'count' + ': ' + i
#             writer.write(str)

# def to_indexed(start_file, end_file):
#     with open(start_file, 'r') as reader:
#       with open(end_file, 'w') as writer:
#         count = 0
#         line = reader.readline()
#         while line != '':
#             writer.write('count: ' + line)
#             count += 1

def to_indexed(start_file, end_file):
    with open(start_file, 'r') as reader:
        with open(end_file, 'w') as writer:
            count = 0
            for i in reader:
                writer.write(str(count) + ': ' + i)
                count += 1


