#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


"""Получение курса доллара и евро от yahoo."""


# TODO: непонятно за какую дату находит
if __name__ == '__main__':
    url = 'https://query.yahooapis.com/v1/public/yql?q=select+*+from+yahoo.finance.xchange+where+pair+=+%22USDRUB,EURRUB%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='

    import requests
    rs = requests.get(url)

    text = 'Курс:'
    for rate in rs.json()['query']['results']['rate']:
        text += '\n' + rate['Name'].split('/')[0] + ' ' + rate['Rate']

    print(text)
