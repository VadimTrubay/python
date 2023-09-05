from random import randint
from faker import Faker

fake = Faker()


def get_dict(n):
    data = list()
    for i in range(n):
        i = dict()
        i["title"] = fake.company()
        i['gas'] = randint(25, 27)
        i['dp'] = randint(51, 55)
        i['nf'] = randint(45, 51)
        i['nf_plus'] = randint(47, 52)
        i['nt'] = randint(46, 48)
        data.append(i)
    return data


a = '47.90'
b = float(a)
print(a, b)