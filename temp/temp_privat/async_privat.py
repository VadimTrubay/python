import platform
from time import time
import aiohttp
import asyncio
from pprint import pprint

data = ["13.04.2023", "15.04.2023", "21.04.2023",
        "22.04.2023", "23.04.2023", "24.04.2023"]


async def main():
    async with aiohttp.ClientSession() as session:
        result = []
        for date in data:
            response = await session.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}')
            result.append(await response.json())
        return result


if __name__ == "__main__":
    st = time()

    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    pprint(asyncio.run(main()))

    print(time() - st)