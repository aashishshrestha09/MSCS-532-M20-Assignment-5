"""
Unit tests for quicksort implementations.
This module verifies the correctness of deterministic and randomized quicksort algorithms.
"""

import unittest
from src.quicksort import deterministic_quicksort, randomized_quicksort


class TestQuicksort(unittest.TestCase):
    """Test cases for quicksort algorithms."""

    def test_deterministic_quicksort(self):
        """Test deterministic quicksort on a sample list."""
        arr = [3, 1, 4, 1, 5, 9, 2]
        expected = sorted(arr)
        deterministic_quicksort(arr)
        self.assertEqual(
            arr, expected, "Deterministic quicksort failed to sort correctly."
        )

    def test_randomized_quicksort(self):
        """Test randomized quicksort on a sample list."""
        arr = [8, 6, 7, 5, 3, 0, 9]
        expected = sorted(arr)
        randomized_quicksort(arr)
        self.assertEqual(
            arr, expected, "Randomized quicksort failed to sort correctly."
        )

    def test_empty_list(self):
        """Test quicksort behavior on an empty list."""
        arr = []
        deterministic_quicksort(arr)
        self.assertEqual(arr, [], "Deterministic quicksort failed on empty list.")

        randomized_quicksort(arr)
        self.assertEqual(arr, [], "Randomized quicksort failed on empty list.")


if __name__ == "__main__":
    unittest.main()
