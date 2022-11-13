"""Tests for Dataset abstraction class."""
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal

from python_datalib import Dataset


def test_read_csv(comma_csv_path: str, target_dataframe: pd.DataFrame) -> None:
    """Test if we can read a comma seperated csv file."""
    dataset = Dataset(Path(comma_csv_path))
    assert_frame_equal(dataset.dataframe, target_dataframe)


def test_write_modified_csv(tmp_path: Path, target_dataframe: pd.DataFrame) -> None:
    """Test if we can write a csv file correctly."""
    target_dataframe["modification"] = True  # Add Column
    dataset = Dataset(tmp_path / "test.csv", dataframe=target_dataframe)
    dataset.save()

    assert_frame_equal(dataset.read(), target_dataframe)
