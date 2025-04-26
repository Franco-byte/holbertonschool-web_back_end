#!/usr/bin/env python3
'''
function sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float.
'''
# from typing import Union


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    # Union can be used instead of "|" -> list[Union[int, float]]
    '''Sum a list of flouts and ints and returns it'''
    result = 0.0
    for i in mxd_lst:
        result += i
    return result
