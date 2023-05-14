#!/usr/bin/env python3
"""Hypermedia pagination
"""


import csv
from math import ceil
from typing import List, Tuple, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            Range of the page

            Args:
                page: Current page
                page_size: Total size of the page

            Return:
                Dict with different arguments
                page_size: the length of the returned dataset page
                page: the current page number
                data: the dataset page
                (equivalent to return from previous task)
                next_page: number of the next page, None if no next page
                prev_page: number of the previous page,
                None if no previous page
                total_pages: the total number of pages
                in the dataset as an integer
        """

        data = []
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataset: List = self.dataset()
        totalpage: int = len(dataset) if dataset else 0
        totalpages = ceil(totalpage / page_size)
        prevpage: int = (page - 1) if (page - 1) >= 1 else None
        nextpage: int = (page + 1) if (page + 1) <= totalpages else None

        hypermedia: Dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': nextpage,
            'prev_page': prevpage,
            'total_pages': totalpages,
        }

        return hypermedia


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return tuple containing pagination start index and end index. """
    start_size: int = page_size * (page - 1)
    end_size: int = page_size * page
    return (start_size, end_size)
