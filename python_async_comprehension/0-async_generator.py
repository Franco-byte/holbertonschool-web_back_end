#!/usr/bin/env python3
'''
More to async
'''


from asyncio import sleep
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''Generator whit delay'''
    for _ in range(10):
        yield uniform(0, 10)
        await sleep(1)
