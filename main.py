import asyncio
import math


async def calculate_sin(number: int, degree: int):
    print(f'Task {number} start')
    result = math.sin(degree * math.pi / 180)
    if number != 5:
        await asyncio.sleep(0)
    print(f'---------------------\n'
          f'Task {number} end; '
          f'Result = {result:.5f}; '
          f'Degree = {degree}')


async def test_async():
    tasks = [
        asyncio.create_task(calculate_sin(int(x / 30) + 1, x)) for x in range(0, 360, 30)
    ]
    for t in tasks:
        await t


if __name__ == '__main__':
    asyncio.run(test_async())
