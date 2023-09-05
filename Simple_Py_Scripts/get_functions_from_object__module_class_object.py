#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


def get_name_by_func(obj: object) -> dict:
    import inspect
    is_ok = lambda name, func: inspect.isroutine(func) and not name.startswith('_')

    return {name: func for name, func in inspect.getmembers(obj) if is_ok(name, func)}


if __name__ == '__main__':
    import math
    print(get_name_by_func(math))

    import builtins
    print(get_name_by_func(builtins))

    class Foo:
        def a(self):
            return 1

    print(get_name_by_func(Foo))
    print(get_name_by_func(Foo()))
