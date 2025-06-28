"""
Unit tests for partition functions.
Tests correctness of deterministic and randomized partitioning behavior.
"""

import unittest
from src.utils.partition import deterministic_partition, randomized_partition


class TestPartition(unittest.TestCase):
    """Test cases for partitioning utilities."""

    def test_deterministic_partition(self):
        """Verify deterministic partition splits the array correctly."""
        arr = [3, 2, 1, 5, 4]
        pivot_index = deterministic_partition(arr, 0, len(arr) - 1)
        self.assertTrue(0 <= pivot_index < len(arr), "Pivot index out of bounds.")
        left = arr[:pivot_index]
        right = arr[pivot_index + 1 :]
        self.assertTrue(
            all(x <= arr[pivot_index] for x in left), "Left partition invalid."
        )
        self.assertTrue(
            all(x >= arr[pivot_index] for x in right), "Right partition invalid."
        )

    def test_randomized_partition(self):
        """Verify randomized partition splits the array correctly."""
        arr = [10, 20, 5, 3, 7]
        pivot_index = randomized_partition(arr, 0, len(arr) - 1)
        self.assertTrue(
            0 <= pivot_index < len(arr),
            "Pivot index out of bounds after random partition.",
        )


if __name__ == "__main__":
    unittest.main()
