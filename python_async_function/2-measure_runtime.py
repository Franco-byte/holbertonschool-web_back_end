#!/usr/bin/env python3
'''
Basics of async
'''


import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''Count average execution time'''
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
