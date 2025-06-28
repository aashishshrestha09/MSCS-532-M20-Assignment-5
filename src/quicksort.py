"""
Deterministic and Randomized Quicksort implementations.

This module provides two main Quicksort variants:
- deterministic_quicksort uses the last element as pivot.
- randomized_quicksort selects pivot randomly.
"""

from utils.partition import deterministic_partition, randomized_partition


def deterministic_quicksort(arr, low=0, high=None):
    """
    Sort the array in place using deterministic Quicksort.

    Args:
        arr (list[int]): The list to sort.
        low (int): Starting index of the sublist.
        high (int): Ending index of the sublist.
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)


def randomized_quicksort(arr, low=0, high=None):
    """
    Sort the array in place using randomized Quicksort.

    Args:
        arr (list[int]): The list to sort.
        low (int): Starting index of the sublist.
        high (int): Ending index of the sublist.
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)
