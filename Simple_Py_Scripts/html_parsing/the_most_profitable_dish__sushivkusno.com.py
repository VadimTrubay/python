#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import sys
import time
import re

# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webdriver import WebElement

sys.path.append('..')
from ascii_table import ascii_table


DEBUG_LOG = False


def do_page_down(driver: RemoteWebDriver, footer: WebElement):
    y_position = 0

    while True:
        DEBUG_LOG and print('y_position:', y_position)
        try:
            ActionChains(driver).move_to_element(footer).perform()
            break
        except MoveTargetOutOfBoundsException:
            y_position += 250
            driver.execute_script(f'window.scrollTo(0, {y_position});')
            time.sleep(1)


def print_the_most_profitable_dish(url: str):
    print(url)

    options = Options()
    options.add_argument('--headless')

    unknown_metrics_items = []
    items = []

    driver = None
    try:
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(2)
        driver.get(url)

        # Пролистывание страницы до низа
        footer_el = driver.find_element(By.CSS_SELECTOR, 'footer')
        do_page_down(driver, footer_el)

        for i, product_el in enumerate(driver.find_elements(By.CSS_SELECTOR, '.product-card'), 1):
            title = product_el.find_element(By.CSS_SELECTOR, '.card-title').text.strip()

            price = product_el.find_element(By.CSS_SELECTOR, '.price-value').text
            price = int(re.sub(r'\D', '', price))

            try:
                tag_subtitle = product_el.find_element(By.CSS_SELECTOR, '.parameters > .param-size').text.strip()
                weight, metrics = tag_subtitle.split()

            except Exception:
                unknown_metrics_items.append((title, price))
                continue

            # Определение метрики
            if metrics not in ['кг.', 'гр.', 'г.']:
                unknown_metrics_items.append((title, tag_subtitle, price))
                continue

            weight = float(weight)
            if metrics == 'кг.':
                weight *= 1000

            DEBUG_LOG and print(f'{i}. "{title}": {weight} г., {price} -> {weight / price:.3f}')
            items.append((title, weight, price, weight / price))

        print('Самые выгодные по количеству грамм за единицу цены:\n')

        # Сортировка по коэффициенту
        items.sort(key=lambda x: x[3], reverse=True)

        items = [
            [title, weight, price, f'{rate:.3f}']
            for title, weight, price, rate in items
        ]

        columns = ['Название', 'Вес (г.)', 'Цена', 'Коэффициент']
        items.insert(0, columns)
        print(ascii_table(items))

        if unknown_metrics_items:
            print('\nНе удалось обработать:')
            for i, item in enumerate(unknown_metrics_items, 1):
                print(f'  {i}. {", ".join(map(str, item))}')

        print('\n')

    finally:
        if driver:
            driver.quit()


if __name__ == '__main__':
    urls = [
        'https://sushivkusno.com/nabory-sety',
        # 'https://sushivkusno.com/goryachie-zakuski',
        # 'https://sushivkusno.com/salaty',
    ]

    for url in urls:
        print_the_most_profitable_dish(url)
