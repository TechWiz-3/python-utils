import pytest
from sys import path
path.insert(0,"../datetime-utils")
from get_day import GetDay

def test_always_passes():
    assert (1 == 1)

def test_get_weekday_from_number():
    assert GetDay().get_weekday_from_number(1) == "Tuesday"
