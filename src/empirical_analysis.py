"""
Runs benchmarks on Quicksort implementations, returning raw timing data.
"""

import sys
import time
from typing import List

import pandas as pd

from quicksort import deterministic_quicksort, randomized_quicksort
from utils.dataset_utils import generate_test_data

# Increase recursion limit for large recursive calls
sys.setrecursionlimit(20000)


def time_sort(sort_func, arr: List[int]) -> float:
    """
    Time execution of a sort function on the given list.

    Args:
        sort_func: sorting function.
        arr: list of ints.

    Returns:
        runtime in seconds.
    """
    start = time.perf_counter()
    sort_func(arr.copy())  # sort a copy so original stays intact
    end = time.perf_counter()
    return end - start


def run_benchmarks(
    num_trials: int = 5,
    input_sizes: List[int] = [1000, 2000, 4000, 8000, 16000],
    data_types: List[str] = ["random", "sorted", "reversed"],
) -> pd.DataFrame:
    """
    Run timing benchmarks across algorithms, input sizes, and data types.

    Returns:
        pd.DataFrame: raw timing data with columns:
        ['Algorithm', 'InputType', 'InputSize', 'RuntimeSeconds', 'Trial']
    """
    records = []

    algorithms = {
        "deterministic": deterministic_quicksort,
        "randomized": randomized_quicksort,
    }

    for data_type in data_types:
        for size in input_sizes:
            for algo_name, algo_func in algorithms.items():
                for trial in range(1, num_trials + 1):
                    data = generate_test_data(size, data_type)
                    runtime = time_sort(algo_func, data)
                    records.append(
                        {
                            "Algorithm": algo_name,
                            "InputType": data_type,
                            "InputSize": size,
                            "RuntimeSeconds": runtime,
                            "Trial": trial,
                        }
                    )

    df = pd.DataFrame(records)
    return df
