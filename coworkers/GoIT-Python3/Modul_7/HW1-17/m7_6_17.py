'''Реализуйте функцию solve_riddle(riddle, word_length, start_letter, reverse=False)
 для нахождения искомого слова в строке ребуса.

Параметры функции:

riddle - строка с зашифрованным словом.
word_length - длина зашифрованного слова.
start_letter - буква, с которой начинается слово (подразумевается, что до начала слова буква не встречается в строке).
reverse - указывает, в каком порядке записано слово. По умолчанию — в прямом.
Для значения True слово зашифровано в обратном порядке, к примеру, в строке mi1rewopret зашифровано слово power.
Функция должна возвращать первое найденное искомое слово. Если слово не найдено, вернуть пустую строку.'''


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    start = riddle.find(start_letter)
    if start != -1:
        if reverse == False:
            end = start + word_length
            result = riddle[start:end]
        if reverse == True:
            end = start - word_length
            reverse_str = riddle[::-1]
            result = reverse_str[-1 - start:-1 - end]
    else:
        result = ''
    return result

print(solve_riddle('mi1powperet', 3, 'r', True))
print('test')
