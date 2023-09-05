from random import randint


def get_random_password():
    password = ''
    for i in range(8):
        password += str(randint(0, 9))
    return password



print(get_random_password())
