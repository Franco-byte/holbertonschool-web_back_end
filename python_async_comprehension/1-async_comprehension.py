#!/usr/bin/env python3
'''
More to async
'''


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Loop generator'''
    return [i async for i in async_generator()]
