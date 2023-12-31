from abc import ABC, abstractmethod

import requests
import xmltodict  # https://pypi.org/project/xmltodict/


class Connection(ABC):
    @abstractmethod
    def get_data_xml_from_url(self, url):
        pass


class RequestConnection(Connection):
    def __init__(self, request: requests):
        self.request = request

    def get_data_xml_from_url(self, url):
        return self.request.get(url).text


class ApiClient:
    def __init__(self, fetch: RequestConnection):
        self.fetch = fetch

    def get_xml(self, url):
        return self.fetch.get_data_xml_from_url(url)


def xml_adapter(xml):
    parse = dict(xmltodict.parse(xml))
    return parse


def parse_course(adapter, data):
    data_ = adapter(data)
    course_usd = None
    exchangerates = data_.get('exchangerates', None)
    if exchangerates:
        course_usd = exchangerates.get(
            'row')[0].get('exchangerate').get('@buy')
    return course_usd


if __name__ == '__main__':
    api_client = ApiClient(RequestConnection(requests))
    data_xml = api_client.get_xml(
        'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
    print(parse_course(xml_adapter, data_xml))