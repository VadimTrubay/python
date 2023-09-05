#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import sys
from pathlib import Path

from collections import defaultdict

# pip install psutil
import psutil

sys.path.append(str(Path(__file__).resolve().parent.parent))
from human_byte_size import sizeof_fmt


column_width = defaultdict(int)
process_list = []

for p in psutil.process_iter():
    memory = p.memory_info().rss
    cols = p.name(), str(memory) + ' bytes', sizeof_fmt(memory)
    process_list.append(cols)

    for i, x in enumerate(cols):
        column_width[i] = max(column_width[i], len(x))

# Sort by memory size
process_list.sort(key=lambda x: int(x[1].split(' ')[0]), reverse=True)

for p in process_list:
    row = [x.rjust(column_width[i]) for i, x in enumerate(p)]
    print(' | '.join(row))
