#!/usr/bin/env python3
'''
function sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    # Optional: mxd_lst: List[int | float]
    '''Sum a list of flouts and ints and returns it'''
    return sum(mxd_lst)
