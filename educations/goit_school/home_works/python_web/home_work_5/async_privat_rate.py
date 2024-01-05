import platform
import aiohttp
import asyncio
from datetime import datetime, timedelta
from prettytable import PrettyTable
from colorama import init, Fore
from time import time
from typing import Callable
from functools import wraps
from sys import argv

init()

PRIVAT = "https://api.privatbank.ua/p24api/exchange_rates?json&date="


def async_timed(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time()
        try:
            return await func(*args, **kwargs)
        finally:
            total = round(time() - start_time, 2)
            print(Fore.RED + f"\nExecution time: {total} seconds")
    return wrapper


def get_date_range(input_days: int):
    delta = timedelta(days=input_days)
    current_date = datetime.now()
    end_date = current_date
    list_date_range = [(end_date - timedelta(days=x)).strftime("%d.%m.%Y") for x in range(delta.days)]

    return delta.days, list_date_range


def print_result(usd, eur, field_names):
    my_table = PrettyTable()
    my_table.field_names = field_names
    my_table.add_row(usd)
    my_table.add_row(eur)
    print(Fore.GREEN + "")
    print(my_table)


@async_timed
async def main(dates):
    async with aiohttp.ClientSession() as session:
        result = []
        for date in dates:
            try:
                result.append(asyncio.create_task(session.get(f'{PRIVAT}{date}', )))
            except aiohttp.ClientConnectorError as err:
                print(f'Connection error: {str(err)}')
        responses = await asyncio.gather(*result)
        return [await r.json() for r in responses]


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # user_input = int(argv[1])
    user_input = int(input('Enter days>: '))

    delta_days, date_range = get_date_range(user_input)

    if delta_days <= 10:

        list_response = asyncio.run(main(date_range))

        for rate_date in list_response:
            list_field_names = [Fore.GREEN + "date"]
            list_values_usd = [Fore.YELLOW + f"{rate_date['date']}"]
            list_values_eur = [Fore.YELLOW + f"{rate_date['date']}"]
            for i in rate_date['exchangeRate']:
                if i["currency"] == "CHF":
                    for k, v in i.items():
                        if not k == "purchaseRateNB":
                            list_field_names.append(Fore.GREEN + str(k))
                elif i["currency"] == "USD":
                    for k, v in i.items():
                        if not k == "purchaseRateNB":
                            list_values_usd.append(Fore.YELLOW + str(v))

                elif i["currency"] == "EUR":
                    for k, v in i.items():
                        if not k == "purchaseRateNB":
                            list_values_eur.append(Fore.YELLOW + str(v))
            print_result(list_values_usd, list_values_eur, list_field_names)

    else:
        print(Fore.YELLOW + '\ntoo many days (max 10 days), try again!')
        print(Fore.RED + "press <ENTER> for continue")
        input()
