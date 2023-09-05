from typing import List

import requests
from bs4 import BeautifulSoup

from datetime import datetime
import json
import re

base_url = 'https://index.minfin.com.ua/ua/russian-invading/casualties/'


def get_urls() -> List[str]:
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div[class=ajaxmonth] h4 a')
    urls = ['']
    prefix = 'month.php?month='
    for el in content:
        urls.append(prefix + re.search(r"\d{4}-\d{2}", el.get('href')).group())
    return urls


def main(urls: List[str]):
    data = []
    for url in urls:
        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('ul[class=see-also] li[class=gold]')
        for element in content:
            result = {}
            date = element.find('span', attrs={'class': 'black'}).text
            try:
                date = datetime.strptime(date, "%d.%m.%Y").isoformat()
            except ValueError:
                print(f'Error for {date}')
                continue

            result.update({'date': date})
            losses, *rest = element.select('div div ul')
            for lose in losses:
                title, quantity = lose.text.split('—')
                title = title.strip()
                quantity = re.search(r"\d+", quantity).group()
                result.update({title: quantity})
            data.append(result)
    return data


if __name__ == '__main__':
    urls = get_urls()
    result = main(urls)
    print(result)
    with open('data.json', 'w', encoding='utf-8') as fd:
        json.dump(result, fd, ensure_ascii=False)
