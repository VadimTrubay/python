'''Вернемся к предыдущей задаче и выполним обратную задачу.
Напишите рекурсивную функцию encode для кодирования списка или строки.
 В качестве аргумента функция принимает список (например ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"])
 или строку (например "XXXZZXXYYYZZ").
  Функция должна вернуть закодированный список элементов (пример ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).'''

def encode(data):
    result = []
    if len(data) == 0:
        return result
    last, counter = data[0], 0
    for i in range(len(data)):
        if data[i] == last:
            counter += 1
        else:
            result.extend([last, counter])
            result.extend(encode(data[i:]))
            break
    else:
        result.extend([last, counter])
    return result