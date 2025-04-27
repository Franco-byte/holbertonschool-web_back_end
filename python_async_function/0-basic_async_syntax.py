#!/usr/bin/env python3
'''
Takes in an integer argument named wait_random that waits for
a random delay between 0 and max_delay seconds and eventually returns it
'''


import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    delay = uniform(0.0, float(max_delay))
    await asyncio.sleep(delay)
    return delay
