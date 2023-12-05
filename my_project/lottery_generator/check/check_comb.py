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
months = 12
hours = 23
minutes = 59
seconds = 59

with open('s_l_res.csv', newline='') as fh:
    reader = csv.reader(fh)
    # headers = next(reader)  # Read the headers if present; skip this line if no headers

    for row in tqdm(reader):
        key, *values = row[0].split(';')
        int_values = list(map(int, values))
        result_dict = {key: int_values}
        # print(result_dict.get(key, result_dict))
        # break


        for month in range(1, months + 1):
            days = monthrange(year, month)[1]
            for day in range(1, days + 1):
                for hour in range(1, hours + 1):
                    for minute in range(0, minutes + 1):
                        for second in range(0, seconds + 1):
                            my_seed = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second).timestamp()
                            random.seed(my_seed)
                            result = sorted(random.sample(list_ball, k=6))
                            if result_dict.get(key, result_dict) == result:
                                victory = "Success"
                                # print(victory)
                                # print(datetime.fromtimestamp(my_seed), f"{result}")
                                d = datetime.fromtimestamp(my_seed)
                                res_dat = d.strftime("%Y-%m-%d %H:%M:%S")
                                with open("results.txt", "a") as file:
                                    file.write(str(result_dict.keys()) + " - " + str(result) + " - " + res_dat + "\n")
                                # sys.exit(4)
                            else:
                                victory = "False"
                            second += 1
                        minute += 1
                    hour += 1
                day += 1
            month += 1
        print(victory)





