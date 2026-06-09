import random
import streamlit as st

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#FIX: the original code was doing string comparison and leaking the secret.
def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"
#FIXME: Now it properly compares the parsed integer guess with the secret number and returns the appropriate outcome and message without leaking the secret in the feedback.

def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score

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



if "difficulty" not in st.session_state or st.session_state.difficulty != difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    #st.session_state.attempts = 1  #FIX: The original code had a syntax error in the following line. 
    st.session_state.attempts = 0                              #FIXME:  I have corrected it to properly reset the attempts count when starting a new game. Setting num Of attempts to 0 instead of 1 to align with the logic in the rest of the code.

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")
hint_placeholder = st.empty()

debug_placeholder = st.empty()

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    #st.session_state.attempts = 1     #FIX: The original code had a syntax error in the following line. 
    st.session_state.attempts = 0                              #FIXME:  I have corrected it to properly reset the attempts count when starting a new game. Setting num Of attempts to 0 instead of 1 to align with the logic in the rest of the code.
    st.session_state.secret = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

ok, guess_int, err = False, None, None
if submit:
    ok, guess_int, err = parse_guess(raw_guess)

attempts_display = st.session_state.attempts
if submit and ok:
    attempts_display += 1
#FIX: Originally the secret would be the same for all difficulties because it was only set once when the app first loaded. Ex(secret could be 100 for all cases which is wrong)
hint_text = ""
if difficulty == "Easy":
    hint_text = f"Guess a number between 1 and 20. Attempts left: {attempt_limit - attempts_display}"
elif difficulty == "Hard":
    hint_text = f"Guess a number between 1 and 50. Attempts left: {attempt_limit - attempts_display}"
else:
    hint_text = f"Guess a number between 1 and 100. Attempts left: {attempt_limit - attempts_display}"

hint_placeholder.info(hint_text)
#FIXME: I have added a check to see if the difficulty has changed in the session state. If it has, we reset the secret number and all related game state variables to ensure that the game behaves correctly when the user changes the difficulty level.
if submit:
    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        #FIXME: Append this guess before updating the counter so the first attempt is always preserved in history.
        st.session_state.history.append(guess_int)
        st.session_state.attempts += 1

        #FIX The secret number was being compared to the raw input string instead of the parsed integer guess, which could lead to incorrect feedback. 

        outcome, message = check_guess(guess_int, st.session_state.secret)
        #FIXME: I have corrected it to compare the parsed integer guess with the secret number for accurate game logic.
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
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

with debug_placeholder.container():
    with st.expander("Developer Debug Info"):
        st.write("Secret:", st.session_state.secret)
        st.write("Attempts:", st.session_state.attempts)
        st.write("Score:", st.session_state.score)
        st.write("Difficulty:", difficulty)
        st.write("History:", st.session_state.history)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
