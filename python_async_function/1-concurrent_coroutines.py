#!/usr/bin/env python3
'''
Basics of async
'''


from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Create a list of the delays values'''
    delay_list: List[float] = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delay_list.append(delay)
    delay_list.sort()
    return delay_list
