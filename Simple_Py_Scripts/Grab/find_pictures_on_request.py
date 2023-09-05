__author__ = 'ipetrash'


# Find images on request search engine


from grab import Grab
import urllib.parse
import re


if __name__ == '__main__':
    url = 'http://yandex.ru/images/search?text='
    rq_text = 'husky puppies'

    url += urllib.parse.quote(rq_text)

    g = Grab()
    g.go(url)

    images = g.doc.select('//a[@class="serp-item__link"]/@onmousedown')
    print('Total: %s' % images.count())

    for im in images:
        im_href = re.search(r'"href":"(.+)"', im.text()).group(1)
        print(im_href)