"""Pytest fixtures.

Functions decorated with @pytest.fixture will be available
as arguments in test_ functions.
"""
from pathlib import Path

import pandas as pd
import pytest


def _test_folder() -> Path:
    return Path(__file__).parent


@pytest.fixture
def comma_csv_path() -> Path:
    """Path to example comma delimited csv file.

    Returns
    -------
    str
    """
    return _test_folder() / "assets/test_comma.csv"


@pytest.fixture
def semicolon_csv_path() -> Path:
    """Path to example semicolon delimited csv file.

    Returns
    -------
    str
    """
    return _test_folder() / "assets/test_semicolon.csv"


@pytest.fixture
def target_dataframe() -> pd.DataFrame:
    """Return Target Dataframe.

    This is how each of the CSV files should look like if loaded into a Dataframe.

    Returns
    -------
    pd.DataFrame
    """
    return pd.DataFrame(
        columns=["id", "name", "type"],
        data=[
            (1, "Test1", "alpha"),
            (2, "Test2", "beta"),
            (3, "Test3", "alpha"),
            (4, "Test4", "beta"),
            (5, "Test5", "alpha"),
            (6, "Test6", "beta"),
            (7, "Test7", "beta"),
        ],
    )
