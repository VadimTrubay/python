import platform
import aiohttp
import asyncio
from datetime import datetime, timedelta
from prettytable import PrettyTable
from colorama import init, Fore
from time import sleep, time
from sys import argv

init()

PRIVAT = "https://api.privatbank.ua/p24api/exchange_rates?json&date="


def get_date_range(user_input):
    delta = timedelta(user_input)
    delta_days = delta.days
    current_date = datetime.now()
    new_date = (current_date - delta).strftime("%d.%m.%Y")
    current_date_str = datetime.now().strftime("%d.%m.%Y")
    end = datetime.strptime(current_date_str, "%d.%m.%Y")
    start = datetime.strptime(new_date, "%d.%m.%Y")
    date_range = [(start + timedelta(days=x)).strftime("%d.%m.%Y") for x in range(0, (end - start).days)]
    return delta_days, date_range


def print_result(list_values_usd, list_values_eur, list_field_names):
    my_table = PrettyTable()
    my_table.field_names = list_field_names
    my_table.add_row(list_values_usd)
    my_table.add_row(list_values_eur)
    print(Fore.GREEN + "")
    print(my_table)


async def main(date_range):
    async with aiohttp.ClientSession() as session:
        result = []
        for date in date_range:
            try:
                result.append(asyncio.create_task(session.get(f'{PRIVAT}{date}', )))
            except aiohttp.ClientConnectorError as err:
                print(f'Connection error: {str(err)}')
        responses = await asyncio.gather(*result)
        return [await r.json() for r in responses]


if __name__ == "__main__":
    st = time()

    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    user_input = float(argv[1])

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

    end = round(time() - st, 2)
    print(Fore.RED + f"\ntime execute: {end}")
