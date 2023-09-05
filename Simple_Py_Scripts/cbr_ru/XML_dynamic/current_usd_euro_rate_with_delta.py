#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


def current_rate(ccy_rq_id):
    """
    Функция возвращает кортеж из двух элементов: курс валюты и разница с предыдущим курсом.

    ccy_rq_id с значением "R01235" -- это USD

    :type ccy_rq_id: str
    """

    # Т.к. курс назначается не каждый день, разница может быть в несколько дней,
    # поэтому на всякий случай берем разницу от текущего дня и на 7 дней назад
    from datetime import date, timedelta
    date_req1 = (date.today() - timedelta(days=7)).strftime('%d/%m/%Y')
    date_req2 = date.today().strftime('%d/%m/%Y')
    # date_req2 = (date.today() + timedelta(days=1)).strftime('%d/%m/%Y')

    url = 'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={}&date_req2={}&VAL_NM_RQ={}'.format(
        date_req1, date_req2, ccy_rq_id
    )

    from urllib.request import urlopen
    with urlopen(url) as f:
        from bs4 import BeautifulSoup
        root = BeautifulSoup(f.read(), "xml")

        # Получаем список курсов
        values = root.select('Record > Value')
        if len(values) < 2:
            raise Exception('Что-то пошло не так. Не хватает значений.\nurl: {}\nroot:\n{}'.format(url, root))

        # Вытаскиваем последние два элемента и преобразуем в число
        values = [values[-2], values[-1]]
        values = [float(price.text.replace(',', '.')) for price in values]

        delta = values[1] - values[0]
        return values[1], delta


if __name__ == '__main__':
    # R01235 -- USD, доллары, 840
    price, delta = current_rate('R01235')
    print('USD: {} ({}{:.4f})'.format(price, ('+' if delta > 0 else ''), delta))

    # R01239 -- EUR, евро, 978
    price, delta = current_rate('R01239')
    print('EUR: {} ({}{:.4f})'.format(price, ('+' if delta > 0 else ''), delta))
