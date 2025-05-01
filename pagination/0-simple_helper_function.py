#!/usr/bin/env python3
'''
Paginations basics
'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Equation for paginating a dataset with the
    "page" and "page_size" parameters
    '''
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    dataset = (start_idx, end_idx)
    return dataset
