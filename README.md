# Quicksort Algorithm: Implementation, Analysis, and Randomization

## Overview

This project provides Python implementations of deterministic and randomized Quicksort algorithms. It includes a detailed theoretical analysis of their time and space complexities, as well as an empirical benchmarking framework to evaluate their performance on different input distributions (random, sorted, reversed). The results are visualized and summarized to help understand the impact of randomization on Quicksort efficiency.

## Project Structure

```bash
.
├── outputs                                 # Generated data and plots
│   ├── data
│   │   ├── benchmark_detailed.csv
│   │   ├── summary_mean_runtimes.csv
│   │   └── summary_std_runtimes.csv
│   └── plots
│       └── quicksort_mean_runtimes.png
├── pyproject.toml
├── README.md
├── src                                     # Source code
│   ├── empirical_analysis.py
│   ├── main.py                             # Orchestrates benchmarks, summaries, plotting
│   ├── plot_results.py
│   ├── quicksort.py
│   └── utils
│       ├── __init__.py
│       ├── dataset_utils.py
│       ├── file_utils.py
│       ├── metrics_utils.py
│       ├── partition.py
│       └── plot_utils.py
└── tests                                   # Unit tests (unittest)
    ├── test_metrics_utils.py
    ├── test_partition.py
    └── test_quicksort.py
```

## Setup

### Pre-requisites

- Install [`python`](https://www.python.org/downloads/).
- Install [`pip`](https://pip.pypa.io/en/stable/installation/).

### Clone the repository

```bash
git clone https://github.com/aashishshrestha09/MSCS-532-M20-Assignment-5.git
cd MSCS-532-M20-Assignment-5

```

### Create and Activate a Virtual Environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
```

### Install as editable with "dev" packages

```bash
pip install --editable ".[dev]"
```

## Usage

### Run the Full Benchmark Pipeline

The main script runs benchmarks on different input sizes and types, generates summary statistics, and creates plots:

```bash
python src/main.py
```

Outputs are saved in the `outputs/` directory:

- Detailed runtime CSVs in `outputs/data/`
- Summary CSVs in `outputs/data/`
- Performance plots in `outputs/plots/`

### Testing

Run unit tests to verify correctness of sorting algorithms and utility functions:

```bash
python -m unittest discover -s tests
```

## Design Highlights

- Deterministic Quicksort: Fixed pivot selection.
- Randomized Quicksort: Random pivot selection to reduce worst-case occurrences.
- Utils modularized: Dataset creation, file handling, metrics aggregation, plotting separated for clarity and reuse.
- Empirical analysis: Benchmarks runtime on multiple input types and sizes.
- Plots: Visualization of mean runtimes with error bars for clear comparison.

## Analysis Summary (in brief)

- Deterministic Quicksort exhibits `O(n^2)` worst-case performance on sorted or reversed data.
- Randomized Quicksort maintains expected `𝑂(𝑛log𝑛)` runtime by reducing likelihood of worst-case.
- Empirical results confirm theoretical expectations, with randomized version outperforming deterministic on sorted/reversed inputs.
- Space complexity remains `𝑂(log𝑛)` for recursive stack calls in average case.

## Dependencies

- [pandas](https://pypi.org/project/pandas/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [seaborn](https://pypi.org/project/seaborn/)
- Development tools: [black](https://pypi.org/project/black/), [pyflakes](https://pypi.org/project/pyflakes/)

All dependencies are specified in [pyproject.toml](pyproject.toml).
