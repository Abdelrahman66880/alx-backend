#!/usr/bin/env python3
"""
Write a function that takes two arguments
page, page_size

this function returns tuple of size two containing
a start index and an end index corresponding to

the range of indexes to return in a list for
those particular pagination parameters.
"""

from typing import Tuple



def index_range(page: int, page_size: int) -> Tuple[int, int]:
	"""Function that return tuple containing start index and end index"""
	start_index = (page - 1) * page_size
	end_index   = page * page_size
	return (start_index, end_index)

