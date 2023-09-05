''' У нас есть именованный кортеж для хранения котов в переменной Cat.
На первом месте у нас кличка котика nickname, потом его возраст age и имя владельца кота owner.

Разработайте функцию convert_list(cats), которая будет работать в двух режимах.

Если функция convert_list принимает в параметре cats список именованных кортежей

[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
То функция вернет следующий список словарей:

[
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
И в то же время, если функция convert_list принимает в параметре cats список словарей,
то результатом будет обратная операция и функция вернет список именованных кортежей.

Для определения типа параметра cats используйте функцию isinstance. '''




import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    if not cats:
        return []
    if type(cats[0]) == Cat:
        return [{'nickname': cat.nickname, 'age': cat.age, 'owner': cat.owner} for cat in cats]
    else:
        return [Cat(cat['nickname'], cat['age'], cat['owner']) for cat in cats]


cats = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
cat = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
print(convert_list(cats))
print(convert_list(cat))

