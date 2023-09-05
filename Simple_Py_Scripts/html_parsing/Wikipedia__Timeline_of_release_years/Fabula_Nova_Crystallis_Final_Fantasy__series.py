#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# Хронология выхода игр


from common import get_parsed_two_column_wikitable


def is_match_table_func(table) -> bool:
    return 'TIMELINE OF RELEASE YEARS' in table.caption.text.strip().upper()


url = 'https://en.wikipedia.org/wiki/Fabula_Nova_Crystallis_Final_Fantasy'
for year, name in get_parsed_two_column_wikitable(url, is_match_table_func):
    print(f'{year}: {name}')

# 2009: Final Fantasy XIII
# 2011: Final Fantasy Type-0
# 2011: Final Fantasy XIII-2
# 2013: Lightning Returns: Final Fantasy XIII
# 2014: Final Fantasy Agito
# 2016: Final Fantasy XV
# 2016: Final Fantasy Awakening
