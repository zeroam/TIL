import time
import asyncio


async def add(a, b):
    print(f"add: {a} + {b}")
    await asyncio.sleep(3)
    # time.sleep(3)
    return a + b


async def print_add(a, b):
    result = await add(a, b)
    print(f"print_add: {a} + {b} = {result}")


async def main():
    await asyncio.gather(print_add(1, 3), print_add(2, 3), print_add(4, 5))


asyncio.run(main())
