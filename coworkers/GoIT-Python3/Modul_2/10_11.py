def factorial(n):
    if n < 2:
        return 1  # Базовый случай
    else:
        return n * factorial(n - 1)  # Рекурсивный случай
        
def factorial(k):
    if k < 2:
        return 1  # Базовый случай
    else:
        return k * factorial(k - 1)  # Рекурсивный случай
        
def factorial(s):
    if s < 2:
        return 1  # Базовый случай
    else:
        return s * factorial(s - 1)  # Рекурсивный случай

def number_of_groups(n, k):
    s = n - k
    result = int(factorial(n) / (factorial(s) * factorial(k)))
    return result

print(number_of_groups (50, 7))