import asyncio
import random


async def process_integer(n):
    await asyncio.sleep(random.randint(1, 5))
    return n * n


async def process_data(numbers):
    tasks = []
    for n in numbers:
        task = asyncio.create_task((process_integer(n)))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return sum(results)


async def main():
    data = [1, 2, 3, 4, 5]
    result = await process_data(data)
    print(f"The sum of the squares of the numbers {data} is: {result}")


if __name__ == "__main__":
    asyncio.run(main())
