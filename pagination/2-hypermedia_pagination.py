#!/usr/bin/env python3
"""
Hypermedia-based pagination implementation module
"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate pagination indices and return a tuple of start and end index for pagination
    """
    # Calculate the starting index for the current page
    start_index = (page - 1) * page_size
    # Calculate the ending index for the current page
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        # Private dataset cache initialization
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset"""
        # Load dataset only if not already cached
        if self.__dataset is None:
            # Read CSV file and process data
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Cache dataset excluding header row
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve the appropriate page of the dataset"""
        # Validate page parameter type and value
        if not isinstance(page, int) or page <= 0:
            raise ValueError("page must be a positive integer")
        # Validate page_size parameter type and value
        if not isinstance(page_size, int) or page_size <= 0:
            raise ValueError("page_size must be a positive integer")
        
        # Get index boundaries for current page
        start_index, end_index = index_range(page, page_size)
        # Load the complete dataset
        data = self.dataset()
        
        # Check if requested page is beyond available data
        if start_index >= len(data):
            return []
        
        # Return the data slice for the requested page
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Generate hypermedia pagination dictionary with navigation metadata
        Return a dictionary with hypermedia pagination info
        """
        # Get the current page data
        data = self.get_page(page, page_size)
        # Calculate total number of records
        total_items = len(self.dataset())
        # Calculate total pages needed
        total_pages = math.ceil(total_items / page_size)
        
        # Determine next page number (if exists)
        next_page = page + 1 if (page * page_size) < total_items else None
        # Determine previous page number (if exists)
        prev_page = page - 1 if page > 1 else None
        
        # Return hypermedia pagination response
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
