"""
Partition helper functions used by Quicksort implementations.

This module contains partitioning logic for both deterministic and randomized
pivot selection strategies.
"""

import random


def deterministic_partition(arr, low, high):
    """
    Partition the array using the last element as pivot (Lomuto partition scheme).

    Args:
        arr (list[int]): The list to partition.
        low (int): The starting index of the sublist.
        high (int): The ending index of the sublist.

    Returns:
        int: The final position index of the pivot element.
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_partition(arr, low, high):
    """
    Partition the array using a randomly chosen pivot.

    Args:
        arr (list[int]): The list to partition.
        low (int): The starting index of the sublist.
        high (int): The ending index of the sublist.

    Returns:
        int: The final position index of the pivot element.
    """
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)
