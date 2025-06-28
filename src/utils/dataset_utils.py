"""
Functions to generate datasets for benchmarking Quicksort algorithms.

Supports generating random, sorted, and reverse-sorted integer lists.
"""

import random
from typing import List


def generate_test_data(size: int, data_type: str) -> List[int]:
    """
    Generate a list of integers according to specified size and distribution.

    Args:
        size (int): Number of elements to generate.
        data_type (str): One of ['random', 'sorted', 'reversed'].

    Returns:
        List[int]: Generated list.

    Raises:
        ValueError: If data_type is invalid.
    """
    if data_type == "random":
        return [random.randint(0, size) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reversed":
        return list(range(size, 0, -1))
    else:
        raise ValueError(
            f"Invalid data_type '{data_type}'. Use 'random', 'sorted', or 'reversed'."
        )
