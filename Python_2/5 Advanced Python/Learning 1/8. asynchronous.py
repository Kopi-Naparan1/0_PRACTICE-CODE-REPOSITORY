import asyncio
import time
import random
import asyncio
import aiohttp




async def file_downloader(n):
    start = time.perf_counter()
    print(f'Downloading file {n}...')
    await asyncio.sleep(random.uniform(1,5))
    end = time.perf_counter()
    print(f'File [{n}] downloaded in {end - start:.2f} secs.')


async def main():
    tasks = []
    for i in range(1, 11):
        tasks.append(asyncio.create_task(file_downloader(i)))

    await asyncio.gather(*tasks)

    print('\n---All Files are downloaded---\n')

asyncio.run(main())