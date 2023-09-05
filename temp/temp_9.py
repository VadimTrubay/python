# import aiohttp
# import asyncio
# from time import time
# import platform
#
# data = ["13.04.2023", "15.04.2023", "21.04.2023", "22.04.2023", "23.04.2023", "24.04.2023"]
#
#
# async def get_exchange_rate():
#     async with aiohttp.ClientSession() as session:
#         for date in data:
#             async with session.get(f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date}") as response:
#                 response_json = await response.json()
#                 return response_json
#
#
# async def main():
#     a = []
#     exchange_rate = await get_exchange_rate()
#     for currency in exchange_rate:
#         a.append(currency)
    # return a
        # print(f"{currency['ccy']} to UAH: buy-{currency['buy']}, sale-{currency['sale']}")

# if __name__ == "__main__":
#     st = time()
#     if platform.system() == 'Windows':
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#     print(asyncio.run(main()))
#     print(time() - st)

# from concurrent.futures import ThreadPoolExecutor
# from time import sleep
#
#
# def return_after_5_secs(message):
#     sleep(3)
#     return message
#
#
# pool = ThreadPoolExecutor(3)
#
# future = pool.submit(return_after_5_secs, ("hello"))
# print(future.done())
# sleep(3)
# print(future.done())
# print(future.result())

# import asyncio
# import datetime
# import random
#
#
# async def my_sleep_func():
#     await asyncio.sleep(random.randint(0, 5))
#
#
# async def display_date(num, loop):
#     end_time = loop.time() + 50.0
#     while True:
#         print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await my_sleep_func()
#
#
# loop = asyncio.get_event_loop()
#
# asyncio.ensure_future(display_date(1, loop))
# asyncio.ensure_future(display_date(2, loop))
#
# loop.run_forever()

from time import time
import asyncio
import aiohttp
import platform
from pprint import pprint

data = ["13.04.2023", "15.04.2023", "21.04.2023",
        "22.04.2023", "23.04.2023", "24.04.2023"]


async def async_gather_http_get():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for date in data:
            tasks.append(asyncio.create_task(session.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}')))
        responses = await asyncio.gather(*tasks)
        return [await r.json() for r in responses]


if __name__ == '__main__':
    st = time()
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    pprint(asyncio.run(async_gather_http_get()))

    print(time() - st)






