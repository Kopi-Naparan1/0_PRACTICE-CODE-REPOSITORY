import asyncio
import aiohttp

urls = [
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/1"
]


async def fetch(session, url):
    async with session.get(url) as response:
        print(f'Fetched [{url}] with status: {response.status}')
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        print("All request are completed")

asyncio.run(main())