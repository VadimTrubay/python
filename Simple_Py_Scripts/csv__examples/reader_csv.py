#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import csv

with open('input.csv') as f:
    csv_reader = csv.reader(f, delimiter=";")
    for row in csv_reader:
        print(row)
