import pytest
from pyriddles.__main__ import list_difficulties, get_riddle_by_difficulty

# test when DIFFICULTIES is empty
def test_list_difficulties_empty(monkeypatch):

    monkeypatch.setattr("pyriddles.__main__.DIFFICULTIES", [])
    assert list_difficulties() == "There are no levels of difficulty."

# test when DIFFICULTIES is not empty
def test_list_difficulties_not_empty(monkeypatch):

    sample_difficulties = ["easy", "medium", "hard"]
    monkeypatch.setattr("pyriddles.__main__.DIFFICULTIES", sample_difficulties)

    expected_output = "The available riddle difficulties are:\n"

    for difficulty in sample_difficulties:
        expected_output += difficulty + "\n"

    assert list_difficulties() == expected_output

# test when input difficulty exists and function outputs a riddle with the same difficulty
def test_get_riddle_by_difficulty_exists(monkeypatch):

    sample_difficulties = ["easy", "medium", "hard"]

    sample_riddles = {
        1: {
            "question": "I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind. What am I?",
            "answer": "An echo",
            "difficulty": "medium"
        },
        2: {
            "question": "I’m tall when I’m young, and I’m short when I’m old. What am I?",
            "answer": "A candle",
            "difficulty": "easy"
        },
        3: {
            "question": "The more of this there is, the less you see. What is it?",
            "answer": "Darkness",
            "difficulty": "easy"
        }
    }

    monkeypatch.setattr("pyriddles.__main__.DIFFICULTIES", sample_difficulties)
    monkeypatch.setattr("pyriddles.__main__.RIDDLES", sample_riddles)

    assert "Here is a medium riddle!" in get_riddle_by_difficulty("medium")
    assert "I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind. What am I?" in get_riddle_by_difficulty("medium")

# test when input difficulty is not in the DIFFICULTIES array
def get_riddle_by_difficulty_doesnt_exist(monkeypatch):

    sample_difficulties = ["easy", "medium", "hard"]

    monkeypatch.setattr("pyriddles.__main__.DIFFICULTIES", sample_difficulties)

    assert get_riddle_by_difficulty("not too hard not too easy") == "Not a valid difficulty."