from time import time
import requests
from pprint import pprint

data = ["13.04.2023", "15.04.2023", "21.04.2023",
        "22.04.2023", "23.04.2023", "24.04.2023"]


def main():
    content = []
    for date in data:
        res = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}')
        content.append(res.json())
    return content


if __name__ == "__main__":
    st = time()
    pprint(main())
    print(time() - st)