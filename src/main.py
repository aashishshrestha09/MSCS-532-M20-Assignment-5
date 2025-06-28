"""
Orchestrates running benchmarks, generating summaries, and plotting results.
"""

import logging
import os

from empirical_analysis import run_benchmarks
from utils.metrics_utils import generate_summaries
from plot_results import plot_mean_runtimes

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

OUTPUT_DATA_DIR = "outputs/data"
OUTPUT_PLOTS_DIR = "outputs/plots"


def main() -> None:
    logging.info("Starting benchmark pipeline...")

    # Ensure output directories exist
    os.makedirs(OUTPUT_DATA_DIR, exist_ok=True)
    os.makedirs(OUTPUT_PLOTS_DIR, exist_ok=True)

    # Step 1: Run benchmarks and save raw data
    df_raw = run_benchmarks()
    detailed_csv_path = os.path.join(OUTPUT_DATA_DIR, "benchmark_detailed.csv")
    df_raw.to_csv(detailed_csv_path, index=False)
    logging.info(f"Saved raw benchmark data to '{detailed_csv_path}'.")

    # Step 2: Generate and save summary stats
    mean_df, std_df = generate_summaries(df_raw)
    mean_csv_path = os.path.join(OUTPUT_DATA_DIR, "summary_mean_runtimes.csv")
    std_csv_path = os.path.join(OUTPUT_DATA_DIR, "summary_std_runtimes.csv")
    mean_df.to_csv(mean_csv_path, index=False)
    std_df.to_csv(std_csv_path, index=False)
    logging.info(f"Saved summary statistics to '{mean_csv_path}' and '{std_csv_path}'.")

    # Step 3: Plot results
    plot_path = os.path.join(OUTPUT_PLOTS_DIR, "quicksort_mean_runtimes.png")
    plot_mean_runtimes(mean_df, output_path=plot_path)
    logging.info(f"Saved benchmark plot to '{plot_path}'.")
    logging.info("Benchmark pipeline completed successfully.")


if __name__ == "__main__":
    main()
