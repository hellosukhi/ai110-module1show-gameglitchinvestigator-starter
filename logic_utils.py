def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Refactored logic into logic_utils.py using agent mode;
    # centralizes difficulty settings so the UI and game logic stay in sync.
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: Refactored logic into logic_utils.py using agent mode;
    # validates blank, whitespace-only, and non-numeric input before the game proceeds.
    if raw is None or str(raw).strip() == "":
        return False, None, "Enter a guess."

    cleaned = str(raw).strip()

    try:
        value = int(cleaned)
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int) -> str:
    """
    Compare guess to secret and return the outcome.

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Refactored logic into logic_utils.py using agent mode;
    # uses direct integer comparison so the outcome is deterministic and avoids string-based edge cases.
    if guess < secret:
        return "Too Low"
    if guess > secret:
        return "Too High"
    return "Win"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIX: Refactored logic into logic_utils.py using agent mode;
    # keeps score rules in one place so the app's feedback and totals stay consistent.
    if outcome == "Win":
        points = max(10, 100 - 10 * (attempt_number + 1))
        return current_score + points

    if outcome in {"Too High", "Too Low"}:
        return current_score - 5

    return current_score
