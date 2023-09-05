import math

a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
c = int(input("Введите коэффициент c: "))

D = b ** 2 - 4 * a * c

if D > 0: 
    x1 = (-b + math.sqrt(D)) / (2 * a) 
    x2 = (-b - math.sqrt(D)) / (2 * a) 
x1 = a
x2 = b
print(f"Дискриминант: {D} Корни: { x1 } и { x2 }")