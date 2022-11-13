"""Test module for wetech CSV Parser."""
import logging
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal

from python_datalib.csv_tools import pandas_read_csv

LOGGER = logging.getLogger(__name__)


def test_read_comma_csv_str(comma_csv_path: str, target_dataframe: pd.DataFrame) -> None:
    """Test if Dataframe can be read using a path as String."""
    assert_frame_equal(pandas_read_csv(comma_csv_path), target_dataframe)


def test_read_comma_csv_path(comma_csv_path: str, target_dataframe: pd.DataFrame) -> None:  #
    """Test if Dataframe can be read using a pathlib Path."""
    path = Path(comma_csv_path)
    assert_frame_equal(pandas_read_csv(path), target_dataframe)


def test_read_semicolon_csv_str(semicolon_csv_path: str, target_dataframe: pd.DataFrame) -> None:
    """Test if Dataframe can be read using a path as String."""
    assert_frame_equal(pandas_read_csv(semicolon_csv_path), target_dataframe)


def test_read_semicolon_csv_path(semicolon_csv_path: str, target_dataframe: pd.DataFrame) -> None:  #
    """Test if Dataframe can be read using a pathlib Path."""
    path = Path(semicolon_csv_path)
    assert_frame_equal(pandas_read_csv(path), target_dataframe)
