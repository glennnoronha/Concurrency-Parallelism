import asyncio


async def foo():
    print("Canyon")
    await asyncio.sleep(2)
    print("Texas")


async def main():
    task = asyncio.create_task((foo()))
    print("W")
    await asyncio.sleep(1)
    print("T")
    await task

asyncio.run(main())
