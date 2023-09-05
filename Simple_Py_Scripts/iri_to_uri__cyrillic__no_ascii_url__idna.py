#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# SOURCE: https://ru.stackoverflow.com/a/487922/201445


from urllib.parse import quote, urlsplit, urlunsplit


def iri_to_uri(iri):
    parts = urlsplit(iri)
    uri = urlunsplit((
        parts.scheme,
        parts.netloc.encode('idna').decode('ascii'),
        quote(parts.path),
        quote(parts.query, '=&'),
        quote(parts.fragment),
    ))
    return uri


if __name__ == '__main__':
    url = 'https://сайт.рф/документы?номер=1234&устройство=телефон'
    new_url = iri_to_uri(url)
    print(new_url)
    assert new_url == 'https://xn--80aswg.xn--p1ai/%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B?%D0%BD%D0%BE%D0%BC%D0%B5%D1%80=1234&%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%BE=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD'

    url = 'https://anapa.russianrealty.ru/Продажа-квартир/'
    new_url = iri_to_uri(url)
    print(new_url)
    assert new_url == 'https://anapa.russianrealty.ru/%D0%9F%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80/'

    url = 'http://www.a\u0131b.com/a\u0131b'
    new_url = iri_to_uri(url)
    print(new_url)
    assert new_url == 'http://www.xn--ab-hpa.com/a%C4%B1b'

    url = 'https://ya.ru'
    new_url = iri_to_uri(url)
    print(new_url)
    assert new_url == 'https://ya.ru'

    url = 'https://google.com'
    new_url = iri_to_uri(url)
    print(new_url)
    assert new_url == 'https://google.com'

    url = 'http://домены.рф'
    new_url = iri_to_uri(url)
    print(new_url)
    assert new_url == 'http://xn--d1acufc5f.xn--p1ai'
