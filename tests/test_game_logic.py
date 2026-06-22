# FIX: Refactored logic into logic_utils.py using agent mode;
# these tests verify the shared game rules directly and protect against regressions.
from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_update_score_penalizes_any_wrong_guess():
    # FIX: Added regression coverage for scoring behavior;
    # verifies that all incorrect guesses reduce the score consistently.
    assert update_score(10, "Too High", 2) == 5
    assert update_score(10, "Too Low", 3) == 5

def test_parse_guess_handles_blank_and_invalid_input():
    # FIX: Added regression checks for input validation;
    # ensures blank, whitespace-only, and malformed values are handled safely.
    assert parse_guess(None) == (False, None, "Enter a guess.")
    assert parse_guess("   ") == (False, None, "Enter a guess.")
    assert parse_guess("abc") == (False, None, "That is not a number.")
    assert parse_guess(" 42 ") == (True, 42, None)

def test_get_range_for_difficulty_hard():
    # FIX: Added a focused test for the difficulty mapping;
    # confirms the hard mode range remains correct and predictable.
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess_accepts_zero_negative_and_large_integers():
    # verifies the parser treats boundary and extreme integers as valid input.
    assert parse_guess("0") == (True, 0, None)
    assert parse_guess("-42") == (True, -42, None)
    assert parse_guess("999999999999999999999") == (
        True,
        999999999999999999999,
        None,
    )


def test_parse_guess_rejects_malformed_numeric_formats():
    # verifies malformed inputs are rejected without crashing the game.
    assert parse_guess("1.5") == (False, None, "That is not a number.")
    assert parse_guess("1,000") == (False, None, "That is not a number.")
    assert parse_guess("12abc") == (False, None, "That is not a number.")
    assert parse_guess("@#") == (False, None, "That is not a number.")
    assert parse_guess("1e3") == (False, None, "That is not a number.")


def test_check_guess_handles_extreme_values():
    # verifies comparisons stay deterministic even for boundary values.
    assert check_guess(-100, 0) == "Too Low"
    assert check_guess(0, 0) == "Win"
    assert check_guess(10**18, 0) == "Too High"
