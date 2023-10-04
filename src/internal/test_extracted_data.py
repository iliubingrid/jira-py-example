import pytest

from src.internal.extracted_data import date_2_sprint


@pytest.mark.parametrize("date,sprint", [
    ("2023-03-08T15:20:59.026-0500", "B"),  # ECMS-49
    ("2023-05-16T11:39:54.848-0400", "F"),
    ("2023-09-05T18:04:41.439-0400", "O"),
])
def test_date_2_sprint(date, sprint):
    s = date_2_sprint(date)
    assert s == sprint
