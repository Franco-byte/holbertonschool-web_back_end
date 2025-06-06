#!/usr/bin/env python3
'''
Task 9. Let's duck type an iterable object
'''


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with their sequence and longitude
    """
    return [(i, len(i)) for i in lst]
