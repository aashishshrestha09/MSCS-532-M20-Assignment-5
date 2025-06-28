"""
File I/O utilities for reading and writing JSON data.

Used for saving and loading benchmark results.
"""

import json
from typing import Any


def save_json(data: Any, filepath: str) -> None:
    """
    Save Python object to a JSON file with indentation.

    Args:
        data (Any): Python data to save.
        filepath (str): Destination file path.
    """
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


def load_json(filepath: str) -> Any:
    """
    Load Python object from a JSON file.

    Args:
        filepath (str): Source file path.

    Returns:
        Any: Python object loaded from file.
    """
    with open(filepath, "r") as f:
        return json.load(f)
