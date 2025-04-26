#!/usr/bin/env python3
'''
function sum_list which takes a list input_list
of floats as argument and returns their sum as a float.
'''


def sum_list(input_list: list[float]) -> float:
    '''Sum a list of flout and returns it'''
    result = 0.0
    for i in input_list:
        result += i
    return result
