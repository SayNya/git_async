import asyncio
import math


async def calculate_sin(number: int, degree: int):
    print(f'Task {number} start')
    result = math.sin(degree * math.pi / 180)
    await asyncio.sleep(0)
    print(result)


async def test_async():
    pass


if __name__ == '__main__':
    test_async()
