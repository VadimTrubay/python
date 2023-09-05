from hello import get_name


def bye(name):
    print(f'bye {name}')


def main():
    name = get_name()
    bye(name)


if __name__ == '__main__':
    main()
