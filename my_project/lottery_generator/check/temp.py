import sys
from datetime import datetime
import random
from sys import exit
from tqdm import tqdm
from calendar import monthrange
# list_ball = [num for num in range(1, 53)]
#
# lottery = [14, 15, 16, 23, 46, 51]
#
#
# my_seed = datetime(year=2023, month=11, day=5, hour=5, minute=5, second=5).timestamp()
# random.seed(my_seed)
# result = [14, 15, 16, 23, 46, 51]
# if lottery == result:
#     victory = "Success"
#     # print(victory)
#     # print(datetime.fromtimestamp(my_seed), f"{result}")
#     d = datetime.fromtimestamp(my_seed)
#     res_dat = d.strftime("%Y-%m-%d %H:%M:%S")
#     print(result)
#     with open("results.txt", "a") as fh:
#         fh.write(str(result) + " - " + res_dat + "\n")



# all_numbers = []
# numbers = list(range(1, 53))
# result = sorted(random.sample(numbers, k=6))
# my_seed = datetime(year=2023, month=11, day=23, hour=11, minute=11, second=11).timestamp()
# random.seed(my_seed)
#
# for i in tqdm(range(10)):
#     new_list = random.sample(numbers, k=6)  # generated random numbers
#     all_numbers.append(sorted(new_list))
#
# for j in tqdm(all_numbers):
#     print(f"{result}: {j}")
#     if result == j:
#         print(f"Success: {result} = {j}")
#         break
# else:
#     print("false")



# r = random.gauss(6)
#
# print(r)



d = datetime.now()
print(d)












