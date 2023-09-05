FILE_VERSION = 1.01


def greeting(name: str) -> str:
    print(f'hello {name}')
# всё что сверху при импорте исполняется
# то что ниже только в этом файле выполняется, при импорте, нет

if __name__ == "__main__":

    def summa(a: int, b: int) -> int:
        print(f'summa = {a + b}')


