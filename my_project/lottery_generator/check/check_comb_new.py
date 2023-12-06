import sys
from datetime import datetime
import csv
import random
from sys import exit
from tqdm import tqdm
from calendar import monthrange


print("start checking\n")
victory = ""
list_ball = [num for num in range(1, 53)]

year = 2023
month = 11
day = 15
hours = 23
minutes = 59
seconds = 59
microseconds = 999999

lottery = [9, 15, 31, 34, 43, 49]

for hour in range(1, hours + 1):
    for minute in range(0, minutes + 1):
        for second in range(0, seconds + 1):
            for microsecond in tqdm(range(0, microseconds + 1)):
                my_seed = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second, microsecond=microsecond).timestamp()
                random.seed(my_seed)
                result = sorted(random.sample(list_ball, k=6))
                if lottery == result:
                    victory = "Success"
                    d = datetime.fromtimestamp(my_seed)
                    res_dat = d.strftime("%Y-%m-%d %H:%M:%S.%f")
                    with open("results.txt", "a") as file:
                        file.write(str(result) + " - " + res_dat + "\n")
                    sys.exit(4)
                else:
                    victory = "False"
                microsecond += 1
            second += 1
        minute += 1

print(victory)





