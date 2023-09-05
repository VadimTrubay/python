#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


def get_logger(name, file='log.txt', encoding='utf-8'):
    import logging
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s] %(filename)s:%(lineno)d %(levelname)-8s %(message)s')

    # Simple file handler
    # fh = logging.FileHandler(file, encoding=encoding)
    # or:
    from logging.handlers import RotatingFileHandler
    fh = RotatingFileHandler(file, maxBytes=10000000, backupCount=5, encoding=encoding)
    fh.setFormatter(formatter)
    log.addHandler(fh)

    import sys
    sh = logging.StreamHandler(stream=sys.stdout)
    sh.setFormatter(formatter)
    log.addHandler(sh)

    return log


log = get_logger(__file__)


if __name__ == '__main__':
    log.debug('foo')
    log.debug('bar')
    log.debug(__file__)
