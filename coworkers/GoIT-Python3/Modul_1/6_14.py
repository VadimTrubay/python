# У нас есть список показателей студентов группы — 
# это список с полученными балами по тестированию.
#  Необходимо список поделить на две части. 
# Напишите функцию split_list, которая принимает список (целые числа),
#  находит среднее значение балла в списке и делит его на два списка. 
# В первый попадают значения меньше среднего, включая среднее значение, 
# а во второй — строго больше среднего. 
# Функция возвращает кортеж этих двух списков.
#  Для пустого списка возвращаем два пустых списка.

def split_list(grade):
    list = grade.copy()
    list.sort()
    low_list = []
    high_list = []
    if len(list) > 1:
       midlle = sum(list) / len(list)
       for i in list:
          if i < midlle:
               low_list.append(i)
          elif i > midlle:
                high_list.append(i)
       return low_list, high_list
    elif len(list) == 0:
        return [], [] 
    elif len(list) == 1:
        for i in list:
            low_list.append(i)
        return low_list, []
        


print(split_list([1, 12, 3, 24, 5]))