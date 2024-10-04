import asyncio


async def func1():
    await asyncio.sleep(2)
    print("func_1")


async def func2():
    await asyncio.sleep(1)
    print("func_2")


async def main():
    # task1 = asyncio.create_task(func1())
    # task2 = asyncio.create_task(func2())

    # await task1
    # await task2

    l1 = await asyncio.gather(func1(), func2())
    print(l1)


if __name__ == "__main__":
    asyncio.run(main())
