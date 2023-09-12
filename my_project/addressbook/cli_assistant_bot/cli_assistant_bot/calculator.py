import numexpr
import os
from time import sleep


def about():
    description = '******************** description *******************\n' \
                  'to use the calculator in the line, enter the\n' \
                  'mathematical operation of the example "5+12/9-18/2",\n' \
                  'and to get the result of the calculation, press Enter\n' \
                  '****************************************************\n'
    return description


def menu():
    menu = '********* menu *********\n' \
           '1| about\n' \
           '2| run calculator\n' \
           '3| exit\n' \
           '************************\n'
    return menu


def main():
    while True:
        os.system('cls')
        print(menu())
        item = input("Your choose >>>: ")
        if item == '1':
            os.system('cls')
            print(about())
            input('<press Enter to continue>')

        elif item == '2':
            os.system('cls')
            print(f"{'*' * 10} {'calculator'} {'*' * 10}")
            operation = input('enter math operation \n>>>: ')
            try:
                result = numexpr.evaluate(operation)
                print(f"{'*' * 32}\nresult: {result}\n{'*' * 32}")
                input('<press Enter to continue>')
            except Exception:
                print('incorrect input, try again')
                input('<press Enter to continue>')
                continue

        elif item == '3':
            print('good bye!')
            sleep(1.5)
            return 'exit'


if __name__ == '__main__':
    main()
