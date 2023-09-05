#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import os.path
os.makedirs('./dir1/dir2/dir3/dir4', exist_ok=True)

from pathlib import Path

n = 'dir3'
m = 'new_dir3'

# Рекурсивный поиск
items = list(Path('.').rglob(n))

# Если нашли папку
if items:
    path = items[0]
    path.rename(path.parent / m)
