def get_grade(key):
    # key = input('Введите оценку: ')
    if key == 'F':
      return 1
    if key == 'FX':
      return 2
    if key == 'E':
      return 3
    if key == 'D':
      return 3
    if key == 'C':
      return 4
    if key == 'B':
      return 5
    if key == 'A':
      return 5
    else: 
      return
    
    


def get_description(key):
    # key = input('Введите оценку: ')
    if key == 'F':
      return 'неудовлетворительно'
    if key == 'FX':
      return 'неудовлетворительно'
    if key == 'E':
      return 'достаточно'
    if key == 'D':
      return 'удовлетворительно'
    if key == 'C':
      return 'хорошо'
    if key == 'B':
      return 'очень хорошо'
    if key == 'A':
      return 'отлично'
    else:
      return

print(get_grade('A'))
print(get_description('A'))