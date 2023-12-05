import sys
from datetime import datetime
import random
from sys import exit
from tqdm import tqdm
from calendar import monthrange

victory = ""
list_ball = [num for num in range(1, 53)]

lottery = [14, 15, 16, 23, 46, 51]

print("start checking")


year = 2023
months = 12
days = monthrange(datetime.now().year, months)[1]
hours = 24
minutes = 60
seconds = 60
print(days)

month = 1
for mon in range(1, months):
    day = 1
    for d in tqdm(range(1, days)):
        hour = 1
        for h in range(1, hours):
            minute = 0
            for m in range(0, minutes):
                second = 0
                for s in range(0, seconds):
                    my_seed = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second).timestamp()
                    random.seed(my_seed)
                    result = sorted(random.sample(list_ball, k=6))
                    # print(f"day {d} hour {h} minute {m} second {s}: {result}")
                    # print(result)
                    if lottery == result:
                        victory = "Victory"
                        print(victory, f"{result}")
                        sys.exit(4)
                    else:
                        victory = "False"
                    second += 1
                minute += 1
            hour += 1
        day += 1
    month += 1


print(victory)





