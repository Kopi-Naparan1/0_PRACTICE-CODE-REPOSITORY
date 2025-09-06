import asyncio
import random


async def greet(name):
    await asyncio.sleep(random.uniform(1,4))
    print(f"Hello, {name}!")


async def main():
    names = ['alice', 'bob', 'conor', 'dracu']
    tasks = []

    for name in names:
        tasks.append(asyncio.create_task(greet(name)))

    await asyncio.gather(*tasks)

asyncio.run(main())
