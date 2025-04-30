#!/usr/bin/env python3
'''
More to async
'''

from asyncio import gather
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Using async.gather'''
    start = perf_counter()
    await gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    end = perf_counter()
    return end - start
