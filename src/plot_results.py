"""
Functions to generate plots from summary benchmark data.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_mean_runtimes(
    mean_df: pd.DataFrame,
    output_path: str = "quicksort_mean_runtimes.png",
) -> None:
    """
    Plot mean runtimes of deterministic and randomized Quicksort for each input type.

    Args:
        mean_df: DataFrame with mean runtimes.
        output_path: Path to save the figure.
    """
    sns.set_theme(style="darkgrid")
    algorithms = mean_df["Algorithm"].unique()
    input_types = mean_df["InputType"].unique()

    fig, axes = plt.subplots(
        len(input_types), 1, figsize=(10, 6 * len(input_types)), sharex=True
    )
    if len(input_types) == 1:
        axes = [axes]

    for ax, input_type in zip(axes, input_types):
        for algo in algorithms:
            subset = mean_df[
                (mean_df["Algorithm"] == algo) & (mean_df["InputType"] == input_type)
            ]
            ax.plot(
                subset["InputSize"],
                subset["RuntimeSeconds"],
                marker="o",
                label=algo.capitalize(),
                linewidth=2,
            )
        ax.set_title(f"Mean Runtime on {input_type.capitalize()} Data")
        ax.set_xlabel("Input Size (log scale)")
        ax.set_ylabel("Mean Runtime (seconds, log scale)")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.legend()
        ax.grid(True, which="both", linestyle="--", linewidth=0.5)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.show()
