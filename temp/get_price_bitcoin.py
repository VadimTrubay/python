from typing import Union
import enum
import requests

class BinanceError(ValueError):
    pass

class SymbolPrice:
    def __init__(self, symbol: str, price: Union[str, float, int]):
        self.symbol = symbol
        self.price = price
        if isinstance(price, (int, str)):
            self.price = float(price)

    def __str__(self):
        return f'symbol: {self.symbol} | price: {self.price}'


class SymbolEnum(enum.Enum):
    BIT = 'BNBBTC'
    ETH = 'ETHBTC'


class Binance:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def is_success(self, status_code: int) -> bool:
        return 200 <= status_code <= 299


    def get_price(self) -> SymbolPrice:
        resp = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={self.symbol}")
        if not self.is_success(resp.status_code):
            raise BinanceError(resp.content.decode())
        data = resp.json()
        return SymbolPrice(data.get('symbol'), data.get('price'))
        # return SymbolPrice(**resp.json())

bit = Binance(SymbolEnum.BIT.value)
eth = Binance(SymbolEnum.ETH.value)
print(bit.get_price())
print(eth.get_price())