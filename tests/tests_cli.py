from pyriddles.cli import get_answer

def test_get_answer_valid():
    assert get_answer(1) == "An echo"

def test_get_answer_invalid():
    assert get_answer(999) == "Riddle not found."

def test_get_answer_multiple():
    assert get_answer(2) == "A candle"
    assert get_answer(3) == "Darkness"
