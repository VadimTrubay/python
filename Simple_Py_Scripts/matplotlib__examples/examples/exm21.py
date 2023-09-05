__author__ = 'ipetrash'


## Использование библиотеки Matplotlib. Как рисовать графики в разных окнах
# В заметке Как нарисовать несколько графиков в одном окне описывалось, как можно
# рисовать несколько независимых графиков в одном окне. На этот раз мы посмотрим,
# как можно рисовать графики в разных окнах.
# Делается это очень просто. Достаточно перед выводом очередного графика вызвать
# функцию figure() из пакета pylab и в качестве параметра передать целочисленный
# идентификатор окна, в который мы хотим поместить график. Если окна с таким
# идентификатором до этого не было, то оно создастся. Если же окно с таким
# идентификатором уже есть, то оно станет "активным", и в дальнейшем все функции
# рисования будут применяться уже к нему.
# Рассмотрим пример, в котором мы поочередно добавляем графики то в одно окно, то
# в другое:


import math

# Импортируем один из пакетов Matplotlib
import pylab

# Импортируем пакет со вспомогательными функциями
from matplotlib__examples import mlab


# Будем рисовать график этой функции
def func (x):
    """
    sinc (x)
    """
    if x == 0:
        return 1.0
    return math.sin (x) / x


if __name__ == '__main__':
    # Интервал изменения переменной по оси X
    xmin = -20.0
    xmax = 20.0

    # Шаг между точками
    dx = 0.01

    # Создадим список координат по оиси X на отрезке [-xmin; xmax], включая концы
    xlist = mlab.frange (xmin, xmax, dx)

    # Вычислим значение функции в заданных точках
    ylist1 = [func (x) for x in xlist]
    ylist2 = [func (x * 0.2) for x in xlist]
    ylist3 = [func (x * 2) for x in xlist]

    # !!! Нарисуем график в первом окне
    pylab.figure (1)
    pylab.plot (xlist, ylist1, label = "f(x)")

    # !!! Нарисуем график во втором окне
    pylab.figure(2)
    pylab.plot (xlist, ylist2, label = "f(x * 0.2)")
    pylab.legend()

    # !!! Нарисуем еще один график в первом окне
    pylab.figure (1)
    pylab.plot (xlist, ylist3, label = "f(x * 2)")
    pylab.legend()

    # Покажем окна с нарисованными графиками
    pylab.show()