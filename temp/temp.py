class MyClass:
    def __init__(self, age):
        self.age = age

    def move(self):
        print('move')

    def get_age(self):
        print(self.age)

    def __str__(self):
        return 'i am'


a = MyClass(22)
print(dir(a))
