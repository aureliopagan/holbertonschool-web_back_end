#!/usr/bin/env python3
"""
Simple pagination implementation module
"""
import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indices for pagination range.
    Returns a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters
    """
    # Calculate starting position based on page number (1-indexed)
    start_index = (page - 1) * page_size
    # Calculate ending position
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        # Initialize private dataset attribute
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset loader method"""
        # Check if dataset is already loaded
        if self.__dataset is None:
            # Open and read the CSV file
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Store dataset without header row
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page from the dataset
        based on the pagination parameters
        """
        # Validate page parameter
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        # Validate page_size parameter
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"
        
        # Get the index range for this page
        start_index, end_index = index_range(page, page_size)
        # Load the dataset
        dataset = self.dataset()
        
        # Return empty list if start index is beyond dataset bounds
        if start_index >= len(dataset):
            return []
        
        # Return the requested slice of data
        return dataset[start_index:end_index]
