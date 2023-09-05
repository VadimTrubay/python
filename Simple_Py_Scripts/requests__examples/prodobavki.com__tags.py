#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import requests
rs = requests.get('https://prodobavki.com')
print(rs)

from urllib.parse import urljoin

from bs4 import BeautifulSoup
root = BeautifulSoup(rs.content, 'lxml')
dobavki = {a.text.strip(): urljoin(rs.url, a['href']) for a in root.select('#blk_tags > a.tg')}
print(dobavki)  # {'E-412': 'https://prodobavki.com/dobavki/E412.html', 'E-202': 'https://prodobavki.com/d ...

for name, url in sorted(dobavki.items(), key=lambda x: int(x[0].replace('E-', ''))):
    # E-102  -> https://prodobavki.com/dobavki/E102.html
    print('{:<6} -> {}'.format(name, url))
