#!/usr/bin/env python3
'''
Paginations basics
'''


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple[int, int]:
    '''
    Equation for paginating a dataset with the
    "page" and "page_size" parameters
    '''
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    dataset = (start_idx, end_idx)
    return dataset


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Return the list of bb´s names page per page
        '''
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()

        index = index_range(page, page_size)

        return data[index[0]:index[1]]
