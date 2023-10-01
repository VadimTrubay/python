import requests
from datetime import datetime, timedelta
from prettytable import PrettyTable
from colorama import init, Fore
import os
from time import sleep
from sys import argv

init()

PRIVAT = "https://api.privatbank.ua/p24api/exchange_rates?json&date="


def print_result(list_values_usd, list_values_eur, list_field_names):
    my_table = PrettyTable()
    my_table.field_names = list_field_names
    my_table.add_row(list_values_usd)
    my_table.add_row(list_values_eur)
    print(Fore.GREEN + "")
    print(my_table)


def get_rate(new_data):
    response = requests.get(f'{PRIVAT}{new_data}')
    exchange_rate = response.json()
    new_rate = exchange_rate["exchangeRate"]
    return new_rate


user_input = float(argv[1])
delta = timedelta(user_input)
delta_days = delta.days

if delta_days <= 10:
    current_date = datetime.now()
    new_data = (current_date - delta).strftime("%d.%m.%Y")
    new_rate = get_rate(new_data)
    list_field_names = [Fore.GREEN + "date"]
    list_values_usd = [Fore.YELLOW + f"{new_data}"]
    list_values_eur = [Fore.YELLOW + f"{new_data}"]
    for i in new_rate:
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
