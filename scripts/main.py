import sys
from hello import main as greet
from bye import main as exitt


def main():
    try:
        if sys.argv[1] == 'greet':
            greet()
        elif sys.argv[1] == 'bye':
            exitt()
        else:
            print('Unknown command')
    except IndexError:
        print('argument myst be great or bye')


if __name__ == '__main__':
    main()