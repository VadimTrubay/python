class Verification:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__len_password

    def __len_password(self):
        if len(self.password) < 4:
            raise ValueError('Password must be at least 4 characters')

    def save(self):
        with open('data', 'a') as file:
            file.write(f'{self.login, self.password}' + ',')


class V2(Verification):
    def __init__(self, login, password, age):
        super().__init__(login, password)
        self.age = age
        self.__save()

    def __save(self):
        with open('data') as r:
            for i in r:
                if f'{self.login, self.password}' + ',' == i:
                    raise ValueError('password already in use')
        super().save()

    def show(self):
        with open('data') as file:
            return file.read()


a = V2('vad1', 'password1', 21)
a.save()
print(a.show())
