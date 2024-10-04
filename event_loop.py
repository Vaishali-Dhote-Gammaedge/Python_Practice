# import asyncio


# async def fun():
#     for i in range(5):
#         print(5)
#     return 0


# loop = asyncio.get_event_loop()
# print(loop)
# loop.run_until_complete(fun())
# loop.close()

# print("Hello!!!")

import asyncio

import aiohttp


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "/https://www.geeksforgeeks.org/install-aiohttp-in-python/"
    response_text = await fetch(url)
    print(response_text)


if __name__ == "__main__":
    asyncio.run(main())
