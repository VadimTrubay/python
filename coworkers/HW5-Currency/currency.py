import asyncio
import platform
import sys
from datetime import datetime, timedelta
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


import aiohttp


class BigValue(Exception):
    pass

separator = "========================================"

async def main(currency:str, date:datetime):
    async with aiohttp.ClientSession() as connect:
        async with connect.get(f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date}") as response:
            result = await response.json()
            await currency_parser(result, currency = currency, date=date)


async def currency_parser(jsonfile:dict, currency:str, date):
     for currencies in jsonfile["exchangeRate"]:
         if currencies["currency"] == currency.upper():
            if currency.upper() in ["USD","EUR"]:
                print(separator)
                print(f"Поточна дата : {date}\nБазова валюта : {currencies['baseCurrency']}\nВалюта : {currencies['currency']}\nКурс продажу НБУ : {currencies['saleRateNB']}\nКурс продажу ПриватБанку : {currencies['saleRate']}\nКурс купівлі ПриватБанку : {currencies['purchaseRate']}")
                print(separator)
            else:
                print(separator)
                print(f"Поточна дата : {date}\nБазова валюта : {currencies['baseCurrency']}\nВалюта : {currencies['currency']}\nКурс продажу\купiвлi НБУ : {currencies['saleRateNB']} грн")
                print(separator)
                                                                #{'baseCurrency': 'UAH', 'currency': 'CAD', 'saleRateNB': 26.8541, 'purchaseRateNB': 26.8541}

async def data_parser(days:int,currency:str):
    if days > 10 or days <=0:
        print(f"\nYOU SET BIG OR SMALL VALUE FOR DAYS\nTRY ENTER VALUE FROM 1 TO 10\n")
        raise BigValue
        

    if days == 1:
        currentDate = datetime.now().date()
        date2 = currentDate.strftime("%d.%m.%Y")
        await main(currency= currency,date = date2)

    elif days > 1:
        for i in range(0,days):
            delta = timedelta(days=i)
            currentDate = datetime.now().date() - delta
            date2 = currentDate.strftime("%d.%m.%Y")
            await  main(currency=currency,date = date2)


currency_completer = WordCompleter(['USD', 'AUD', 'AZN', 'BYN', "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP", "ILS","JPY","KZT","MDL","NOK","PLN","SEK","SGD","TMT","TRY","UZS","XAU"])
days_completer = WordCompleter([str(i) for i in range(1,11)])

if __name__== "__main__":
    # curr = sys.argv[1]
    if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    print("\nPush TAB\SPACE in input to see all currencies ID!\n")

    CURRENCY_INPUT = prompt('Enter currency: ', completer=currency_completer)
    DAYS_INPUT =  int(prompt("Enter days: ",completer=days_completer))
    try:
        a = asyncio.run(data_parser(DAYS_INPUT,CURRENCY_INPUT))
    except BigValue:
        pass

#{'baseCurrency': 'UAH', 'currency': 'CAD', 'saleRateNB': 26.8541, 'purchaseRateNB': 26.8541}
#{'baseCurrency': 'UAH', 'currency': 'USD', 'saleRateNB': 36.5686, 'purchaseRateNB': 36.5686, 'saleRate': 37.72, 'purchaseRate': 37.22}