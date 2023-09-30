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
    print()
    print(my_table)


def create_list_field_usd(exchange_rate):
    list_field_names_usd = []
    list_values_usd = []
    list_field_names_usd.append(Fore.GREEN + 'date')
    list_values_usd.append(Fore.YELLOW + exchange_rate['date'])
    return list_field_names_usd, list_values_usd


def create_list_field_eur(exchange_rate):
    list_field_names_eur = []
    list_values_eur = []
    list_field_names_eur.append(Fore.GREEN + 'date')
    list_values_eur.append(Fore.YELLOW + exchange_rate['date'])
    return list_field_names_eur, list_values_eur


def get_rate(new_data):
    response = requests.get(f'{PRIVAT}{new_data}')
    exchange_rate = response.json()
    new_rate = exchange_rate["exchangeRate"]
    return new_rate, exchange_rate


while True:
    os.system('cls')
    # user_input = float(input(Fore.GREEN + "enter quantity days >>: "))
    user_input = float(argv[1])
    delta = timedelta(user_input)
    delta_days = delta.days

    if delta_days <= 10:
        current_date = datetime.now()
        new_data = (current_date - delta).strftime("%d.%m.%Y")
        new_rate, exchange_rate = get_rate(new_data)
        list_field_names_usd, list_values_usd = create_list_field_usd(exchange_rate)
        list_field_names_eur, list_values_eur = create_list_field_eur(exchange_rate)
        for i in new_rate:
            if i["currency"] == "USD":
                for k, v in i.items():
                    if not k == "purchaseRateNB":
                        list_values_usd.append(Fore.YELLOW + str(v))
                        list_field_names_usd.append(Fore.GREEN + str(k))

            elif i["currency"] == "EUR":
                for k, v in i.items():
                    if not k == "purchaseRateNB":
                        list_values_eur.append(Fore.YELLOW + str(v))
                        list_field_names_eur.append(Fore.GREEN + str(k))

        print_result(list_values_usd, list_values_eur, list_field_names_eur)

        question = input(Fore.BLUE + "\ntry again (y/n)?>: ")

        if question == 'y':
            continue
        else:
            print(Fore.MAGENTA + '\ngood bye!')
            sleep(1)
            break
    else:
        print(Fore.YELLOW + '\nquantity days is so big, try again!')
        print(Fore.RED + "\npress <ENTER> for continue")
        input()
        continue
