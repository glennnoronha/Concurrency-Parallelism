import asyncio


async def laptop():
    print("Experiment 1 results available")
    return 10


async def morgan(future):
    future.set_result(await laptop())
    await asyncio.sleep(5)
    print("Experiment 2 is done")
    print("Morgan's work is done")


async def john():
    future = asyncio.Future()
    task = asyncio.create_task((morgan(future)))
    await asyncio.sleep(2)
    result = await future
    print("John's work is done: ", result)
    await task


asyncio.run(john())
