#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from abc import ABC, abstractmethod
import requests


class IGoUrl(ABC):
    """Интерфейс для прокси и реального субъекта"""

    @abstractmethod
    def get(self, url: str) -> requests.Response:
        pass

    @abstractmethod
    def get_status_code(self, url: str) -> int:
        pass


class GoUrl(IGoUrl):
    """Реальный субъект"""

    def get(self, url: str) -> requests.Response:
        return requests.get(url)

    def get_status_code(self, url: str) -> int:
        return requests.head(url).status_code


class GoUrlCachedProxy(IGoUrl):
    """Прокси"""

    def __init__(self):
        self._url = GoUrl()
        self._cache = dict()
        self._cache_status_code = dict()

    def get(self, url: str) -> requests.Response:
        if url in self._cache:
            return self._cache[url]

        rs = self._url.get(url)
        self._cache[url] = rs

        return rs

    def get_status_code(self, url: str) -> int:
        if url in self._cache_status_code:
            return self._cache_status_code[url]

        code = self._url.get_status_code(url)
        self._cache_status_code[url] = code

        return code


if __name__ == '__main__':
    import time

    class TimeThis:
        def __enter__(self):
            self.start_time = time.clock()
            return self

        def __exit__(self, exc_type, exc_value, exc_traceback):
            print('Elapsed time: {:.6f} sec'.format(time.clock() - self.start_time))

    url = 'https://github.com/gil9red'

    go_url = GoUrl()

    with TimeThis():
        rs = go_url.get(url)
        code = go_url.get_status_code(url)
        print(rs, rs.status_code, code, rs.content)

    with TimeThis():
        rs = go_url.get(url)
        code = go_url.get_status_code(url)
        print(rs, rs.status_code, code, rs.content)

    with TimeThis():
        rs = go_url.get(url)
        code = go_url.get_status_code(url)
        print(rs, rs.status_code, code, rs.content)

    print()
    print('Cached proxy:')

    go_url = GoUrlCachedProxy()

    with TimeThis():
        rs = go_url.get(url)
        code = go_url.get_status_code(url)
        print(rs, rs.status_code, code, rs.content)

    with TimeThis():
        rs = go_url.get(url)
        code = go_url.get_status_code(url)
        print(rs, rs.status_code, code, rs.content)

    with TimeThis():
        rs = go_url.get(url)
        code = go_url.get_status_code(url)
        print(rs, rs.status_code, code, rs.content)
