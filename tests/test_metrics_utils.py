"""
Unit tests for metrics_utils functions.
This module tests the correctness of summary statistic generation
from runtime benchmark data.
"""

import unittest
import pandas as pd
from src.utils.metrics_utils import generate_summaries


class TestMetricsUtils(unittest.TestCase):
    """Test cases for the metrics utility functions."""

    def test_generate_summaries_structure(self):
        """Test that the generated summary DataFrames have correct structure."""
        df = pd.DataFrame(
            {
                "Algorithm": ["deterministic"] * 5,
                "InputType": ["random"] * 5,
                "InputSize": [100, 1000, 5000, 10000, 20000],
                "RuntimeSeconds": [0.01, 0.02, 0.05, 0.08, 0.15],
            }
        )

        mean_df, std_df = generate_summaries(df)

        expected_columns = {"Algorithm", "InputType", "InputSize", "RuntimeSeconds"}
        self.assertFalse(mean_df.empty, "Mean DataFrame should not be empty.")
        self.assertFalse(
            std_df.empty, "Standard deviation DataFrame should not be empty."
        )
        self.assertEqual(
            set(mean_df.columns), expected_columns, "Mean DataFrame columns mismatch."
        )
        self.assertEqual(
            set(std_df.columns), expected_columns, "Std DataFrame columns mismatch."
        )


if __name__ == "__main__":
    unittest.main()
