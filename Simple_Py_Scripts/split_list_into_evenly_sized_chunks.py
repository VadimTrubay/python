#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# SOURCE: https://stackoverflow.com/a/312464/5909792


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i: i + n]


if __name__ == '__main__':
    print(list(chunks('hello_world!', n=3)))  # ['hel', 'lo_', 'wor', 'ld!']
    print(list(chunks('hello_world!', n=5)))  # ['hello', '_worl', 'd!']
    print()

    print(list(chunks(list(range(9)), n=3)))  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    print(list(chunks(list(range(9)), n=5)))  # [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
