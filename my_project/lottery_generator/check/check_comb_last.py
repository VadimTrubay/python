import sys
from datetime import datetime
import csv
import random
from sys import exit
from tqdm import tqdm
from calendar import monthrange


print("start checking\n")
list_ball = [num for num in range(1, 53)]

year = 2023
months = 11
days = 25
hours = 23
minutes = 59
seconds = 59


with open('s_l_res.csv', newline='') as fh:
    reader = csv.reader(fh)

    for row in reader:
        key, *values = row[0].split(';')
        int_values = list(map(int, values))
        result_dict = {key: int_values}

        for month in tqdm(range(1, months + 1)):
            days = monthrange(year, month)[1]
            print(f"month: {month}")
            for day in range(1, days + 1):
                for hour in range(1, hours + 1):
                    for minute in range(0, minutes + 1):
                        for second in range(0, seconds + 1):
                            my_seed = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second).timestamp()
                            random.seed(my_seed)
                            result = sorted(random.sample(list_ball, k=6))
                            if result_dict.get(key, result_dict) == result:
                                d = datetime.fromtimestamp(my_seed)
                                res_dat = d.strftime("%Y-%m-%d %H:%M:%S.%f")
                                with open("results.txt", "a") as file:
                                    file.write(str(result_dict.keys()) + " - " + str(result) + " - " + res_dat + "\n")
                            second += 1
                        minute += 1
                    hour += 1
                day += 1
            month += 1
with open("results.txt") as file:
    f = file.read()
    print(f)




