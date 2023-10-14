class Human:
    default_name = "no name"
    default_age = 0

    @staticmethod
    def default_info():
        print(f'default_name: {Human.default_name}' + '\n'
                f'default_age: {Human.default_age}' + '\n')


    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None


    def info(self):
        print('========================')
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"money: {self.__money}")
        print(f"house: {self.__house}")
        print('========================')


    def __make_deal(self, house, price):
        if house:
            self.__house = house
            self.__money -= price

    def earn_money(self, money):
        self.__money += money
        print(f'you are have {self.__money} money')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money < price:
            print('dont have any money')
        else:
            self.__make_deal(house, price)
            print(f'congratulate, house been to buy!!! {price}')



class House:
    def __init__(self, area, price):
        self.__area = area
        self.__price = price


    def final_price(self, discount):
        # print(f'final price: {self.__price * (100 - discount) / 100}')
        return self.__price * (100 - discount) / 100

class SmallHouse(House):
    def __init__(self, area = 40, price=10_000):
        super().__init__(area, price)

if __name__ == '__main__':

    Human.default_info()
    h = Human('vad', 44)
    h.info()
    sh = SmallHouse()
    print(sh.final_price(20))
    h.buy_house(sh, 20)
    h.earn_money(8_000)
    h.info()
    print(sh.final_price(20))
    h.buy_house(sh, 20)
    h.info()
