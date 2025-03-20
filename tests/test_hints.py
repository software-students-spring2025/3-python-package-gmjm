# this file contains the tests for the get_hint() and other hints.py functions
import pytest
from pyriddles.hints import get_hints, get_hint, prewritten_hint, random_hint, HINT_TYPE_OPTIONS

@pytest.fixture
def sample_riddle():
    """Returns a normal sample riddle dictionary."""
    return {
        "question": "What has keys but can't open locks?",
        "answer": "A piano",
        "hints": ["It has black and white parts", "It makes music"]
    }

@pytest.fixture
def riddle_without_hints():
    """Returns a riddle dictionary without hints."""
    return {
        "question": "What has legs but doesn't walk?",
        "answer": "A table",
        "hints": []
    }

# TESTS FOR GET_HINT()

def test_default_hint_type_is_auto(sample_riddle):
    """Ensure that get_hint() defaults to 'auto'/works when no type is specified."""
    hint = get_hint(sample_riddle)
    assert isinstance(hint, str)  and hint is not None

def test_get_hint(sample_riddle):
    """Tests that get_hint returns a valid hint."""
    hint = get_hint(sample_riddle, "auto")
    assert isinstance(hint, str) and hint != ""

def test_get_hint_retries_on_same_answer(monkeypatch, sample_riddle):
    """Ensures `get_hint` retries if the generated hint is the same as the answer."""

    # mock func that always returns the answer to force retry
    def always_return_answer(answer, _hints_list=None):
        return answer

    monkeypatch.setitem(HINT_TYPE_OPTIONS, "auto", always_return_answer) # patch all HINT_TYPE_OPTIONS in pyriddles.hints, with force_fail_function using monkeypatch

    hint = get_hint(sample_riddle, "auto", max_attempts=5)

    assert hint == "Sorry, no valid hints available for this riddle. Please try another hint type or riddle."

# TESTS FOR GET_HINTS()

def test_get_hints(sample_riddle):
    """Tests that get_hints generates multiple hints."""
    hints = get_hints(sample_riddle, "auto", limit=5)
    assert len(hints) == 5 and all(isinstance(hint, str) for hint in hints)

def test_get_hints_handles_limit(sample_riddle):
    """Ensures get_hints stops at the specified limit."""
    hints = get_hints(sample_riddle, "auto", limit=3)
    assert len(hints) == 3

# TESTS FOR OTHER HELPER FUNCTIONS

def test_prewritten_hint(sample_riddle):
    """Tests prewritten_hint function with a valid hints list."""
    hint = prewritten_hint(sample_riddle["hints"])
    assert hint in sample_riddle["hints"], f"Unexpected hint: {hint}"

def test_prewritten_hint_no_hints(riddle_without_hints):
    """Tests prewritten_hint function with no available hints."""
    with pytest.raises(ValueError, match="No hints are available for this type. Please try another hint type."):
        prewritten_hint(riddle_without_hints["hints"])

def test_random_hint_does_not_return_answer(sample_riddle):
    """Ensures that random_hint does not return the same word as the answer."""
    for _ in range(10):
        hint = random_hint(sample_riddle["answer"], sample_riddle["hints"])
        assert hint != sample_riddle["answer"], f"Random hint returned the answer: {hint}"

def test_random_hint_exceeds_attempts(sample_riddle, monkeypatch):
    """Ensures random_hint stops after max_attempts when no valid hint is found.
    It does this by creating a mock function where the hint functions will always fail.
    """

    # mock func that always fails
    def force_fail_function(_answer):
        raise ValueError("Forced failure.")
    
    # needed in order to patch all these
    hint_functions = [
        "prewritten_hint",
        "wordlength_hint",
        "firstletters_hint",
        "revealrandom_hint",
        "wordscramble_hint",
        "revealvowels_hint",
        "soundsalad_hint",
        "binary_hint",
        "morse_hint",
        "synonymsalad_hint",
    ]

    for func in hint_functions:
        monkeypatch.setattr(f"pyriddles.hints.{func}", force_fail_function) # patch all hint functions in pyriddles.hints, with force_fail_function using monkeypatch

    # run random_hint() with forced failures
    hint = random_hint(sample_riddle["answer"], [])

    # ensure it stops at max attempts
    assert hint == "Sorry, no valid hints are available for this riddle."