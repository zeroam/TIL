import random
import asyncio


class AsyncCounter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < self.stop:
            t = random.randint(1, 5)
            print(f"wait: {t}s")
            await asyncio.sleep(t)
            r = self.current
            self.current += 1
            return r
        else:
            raise StopAsyncIteration


async def main():
    async for i in AsyncCounter(5):
        print(i, end=" ")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
