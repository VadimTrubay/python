from pathlib import Path
import sys


def main():
    # if len(sys.argv) < 2:
    #     user_input = ''
    # else:
    #     user_input = sys.argv[1]
    user_input = input('>>> : ')
    path = Path(user_input)
    if path.exists():
        if path.is_dir():
            # items = path.iterdir()  # search directory
            # items = path.glob('*.py')  # search patterns
            items = path.glob('**/*.*')  # search all files
            for item in items:
                print(item)
        else:
            print(f'{path} is a file')
    else:
        print(f'{path.absolute()} not found')


if __name__ == "__main__":
    main()
