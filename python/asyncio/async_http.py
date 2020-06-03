import httpx


# Traditional python
def do_stuff():
    resp = httpx.get("https://www.example.com/")
    return resp.json()


# With Async
async def do_stuff_async():
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://www.example.com")
        return resp.json


if __name__ == "__main__":
    print("Start Async")
    print(do_stuff_async())
    print("Start Non Async")
    print(do_stuff())
