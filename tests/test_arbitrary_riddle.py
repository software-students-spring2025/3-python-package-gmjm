import pytest
from pyriddles.__main__ import arbitrary_riddle

def test_arbitrary_riddle_exists():
    assert callable(arbitrary_riddle), "Function 'arbitrary riddle' does not exist or is not callable"

def test_return_riddle_id(): 
    riddle_id = arbitrary_riddle()
    assert isinstance(riddle_id, int), "Returned value is not an integer"
    assert 1 <= riddle_id <= 10, "Returned value is not within the range 1-10"

def test_id_not_none():
    assert arbitrary_riddle() is not None, "Function returned None"