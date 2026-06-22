import random

import streamlit as st

# FIX: Refactored game logic into logic_utils.py using agent mode;
# centralizes validation, range handling, scoring, and guess evaluation.
from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# FIX: Refactored logic into logic_utils.py using agent mode;
# if the user changes difficulty mid-session, the game state must be reset so the secret stays valid for the new range.
if "last_difficulty" not in st.session_state:
    st.session_state.last_difficulty = difficulty

if difficulty != st.session_state.last_difficulty:
    st.session_state.last_difficulty = difficulty
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.rerun()

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    # FIX: Reset attempt tracking to zero at game start;
    # this prevents the UI from showing a misleading extra attempt on first run.
    st.session_state.attempts = 0

if "score" not in st.session_state:
    # FIX: Initialize score explicitly so each session starts from a clean baseline.
    st.session_state.score = 0

if "status" not in st.session_state:
    # FIX: Track game state separately from the raw input so the UI can stop correctly after win/loss.
    st.session_state.status = "playing"

if "history" not in st.session_state:
    # FIX: Preserve a record of guesses for debugging and user feedback without leaking prior sessions.
    st.session_state.history = []

st.subheader("Make a guess")

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

with st.form("guess_form"):
    # FIX: Moved guess submission into a form to avoid accidental reloads;
    # this keeps the input value stable and makes the flow more predictable.
    raw_guess = st.text_input(
        "Enter your guess:",
        key=f"guess_input_{difficulty}",
    )
    submitted = st.form_submit_button("Submit Guess 🚀")

col1, col2 = st.columns(2)
with col1:
    new_game = st.button("New Game 🔁")
with col2:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    # FIX: Refactored logic into logic_utils.py using agent mode;
    # recompute the range from the current difficulty so the new game matches the selected settings.
    # FIX: Refactored logic into logic_utils.py using agent mode;
    # explicitly reset score, attempt count, status, and history to prevent stale values from leaking across sessions.
    low, high = get_range_for_difficulty(difficulty)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.secret = random.randint(low, high)
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submitted:
    # FIX: Refactored logic into logic_utils.py using agent mode;
    # parsing is now centralized so blank, whitespace-only, and invalid entries are handled consistently.
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        # FIX: Store the raw invalid input for debugging visibility without crashing the app.
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        # FIX: Increment attempts only after a valid guess is accepted;
        # this keeps the attempt counter accurate and avoids counting invalid entries.
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)

        # FIX: Use the shared guess evaluator so outcome logic is consistent across the whole app.
        outcome = check_guess(guess_int, st.session_state.secret)

        if outcome == "Win":
            message = "🎉 Correct!"
        elif outcome == "Too High":
            message = "📉 Go LOWER!"
        else:
            message = "📈 Go HIGHER!"

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.error(
                f"Out of attempts! "
                f"The secret was {st.session_state.secret}. "
                f"Score: {st.session_state.score}"
            )

# FIX: Recalculate remaining attempts after the submission has been processed;
# this prevents the UI from showing a stale countdown when the final guess is made.
if st.session_state.status == "playing":
    attempts_left = max(0, attempt_limit - st.session_state.attempts)
    st.info(
        f"Guess a number between {low} and {high}. "
        f"Attempts left: {attempts_left}"
    )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
