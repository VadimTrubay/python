#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# Для интереса написать аналог NPM leftpad.
#
# leftpad = require('left-pad')
#
# leftpad('foo', 5)
# // => "  foo"
#
# leftpad('foobar', 6)
# // => "foobar"
#
# leftpad(1, 2, 0)
# // => "01"


def leftpad(text, size, ch=' '):
    text = str(text)
    ch = str(ch)

    text_size = len(text)
    return ch * (size - text_size) + text


# Версия с использованием общего алгоритм
def leftpad2(text, size, ch=' '):
    text = str(text)
    ch = str(ch)

    text_size = len(text)
    result = ''

    pad_len = size - text_size
    if pad_len <= 0:
        return text

    for i in range(pad_len):
        result += ch
    result += text

    return result


if __name__ == '__main__':
    assert leftpad('foo', 5) == "  foo"
    assert leftpad('foobar', 6) == "foobar"
    assert leftpad(1, 2, 0) == "01"

    assert leftpad('foo', 5) == leftpad2('foo', 5)
    assert leftpad('foobar', 6) == leftpad2('foobar', 6)
    assert leftpad(1, 2, 0) == leftpad(1, 2, 0)
