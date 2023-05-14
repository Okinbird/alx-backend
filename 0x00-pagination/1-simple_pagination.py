#!/usr/bin/env python3
"""
    Description: Implement a method named get_page that takes two integer
                arguments page with default value 1 and page_size with
                default value 10.
"""

import csv
import math
from typing import List, Tuple


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
        """
            Get the page

            Args:
                page: Current page
                page_size: Total size of the page

            Return:
                List of the pagination done
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range: Tuple = index_range(page, page_size)
        start = range[0]
        end = range[1]
        pagination: List = self.dataset()

        try:
            return (pagination[start:end])
        except IndexError:
            return []

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return tuple containing pagination start index and end index. """
    start_size: int = page_size * (page - 1)
    end_size: int = page_size * page
    return (start_size, end_size)
