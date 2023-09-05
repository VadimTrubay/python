'''Напишите функцию real_len, которая подсчитывает и 
возвращает длину строки без следующих управляющих символов: [\n, \f, \r, \t, \v]

Для проверки правильности работы функции real_len ей будут переданы следующие строки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'''

def real_len(text):
    count = 0
    for i in text:
        if i not in '\n\f\r\t\v':
            count += 1
    return count


print(real_len('Alex\nKdfe23\t\f\v.\r'))
print(real_len('Al\nKdfe23\t\v.\r'))