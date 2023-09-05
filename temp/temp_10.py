import aiohttp
import asyncio

async def main():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
    timeout = aiohttp.ClientTimeout(total=0.5)
    async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
        try:
            async with session.get('http://httpbin.org/get') as response:
                print(response.status, response.headers)
                body = await response.text()
                print(body)

                if response.status >= 300:
                    print("HTTP error")
        except TimeoutError as error:
            print("timeout")
if __name__ == '__main__':
    asyncio.run(main())