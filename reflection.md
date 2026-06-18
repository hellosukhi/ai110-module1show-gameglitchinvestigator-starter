# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

It looks like a office app, not a game. There's a lot of text and developer facing info facing the user, including a drop down box that contains the secret. The vibe is like a whiteboard or an office thing, not much like a game, it was hard to find the user input box.  

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

"press enter to apply" doesnt work

"go lower" is the only hint given, even when you input the lowest number including 0 or negative numbers

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|50     | none              | hint given      | GO LOWER! |
| 5     | go higher         | hint given      | GO LOWER!/lower than 5?|
| 1     | go higher         | hint given      | GO LOWER! go lower not possible|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Claude, Gemini, VS Code AI tools which are enabled by GitHub Copilot  

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Gemini said in app.py:

1. The Logic Layer

The top of your code defines the game rules, but the bottom section contains NotImplementedError placeholders. This means your app is currently using the definitions at the top, which contain several logical inconsistencies:

    get_range_for_difficulty: For "Hard" difficulty, it returns (1, 50), but the UI text below still tells the user "1 to 100." This mismatch causes confusion.

    check_guess: This contains a major "glitch." It tries to compare an integer guess with a secret that alternates between an integer and a string (based on the attempt number). Python does not allow direct comparison between strings and integers using > or <, which is why the try/except block is there to catch errors.

    update_score: This function penalizes the player for guessing "Too Low" but rewards them for guessing "Too High" if the attempt number is even. This creates an erratic scoring system.  

2. State Management

Because Streamlit reruns the entire script every time the user interacts with a widget (like clicking "Submit"), the code uses st.session_state to "remember" variables between runs.

    secret: The number to guess.

    attempts: A counter that increments on every click of the "Submit" button.

    history: A list that tracks what the user has guessed.

3. The Execution Flow

When a user submits a guess:

    Parsing: parse_guess converts the text input into an integer.

    The "Glitch" Mechanism: Inside the main logic, there is an if statement:

    if st.session_state.attempts % 2 == 0:
    secret = str(st.session_state.secret)
else:
    secret = st.session_state.secret

This causes the comparison to fail or behave differently on every other turn because it switches the secret number's type from a number to a string.

Checking: check_guess compares the input against that toggled secret.

Scoring: update_score modifies the points based on the outcome and the attempt count.

UI Feedback: Streamlit displays st.balloons() if you win or st.error() if you run out of attempts.

Why it feels "broken"

You are experiencing issues because of these specific design choices:

    Type Mismatch: Comparing a string ("50") to an integer (50) in Python will cause the check_guess function to crash or fall into the except block every other turn.

    UI/Logic Disconnect: The attempt_limit variable is set correctly by the map, but the new_game button resets the secret to a hard-coded range (1, 100) rather than respecting the current difficulty setting.

    Hard vs. Normal Range: On "Hard" mode, the game allows for a range up to 50, but because your new_game logic uses a default 1 to 100, it makes the game feel inconsistent.

Recommended Next Steps

To stabilize the game:

    Standardize Data Types: Remove the logic that converts the secret to a string. Keep both the guess and secret as integers.

    Refactor: Move the functions at the top into a separate file named logic_utils.py as your comments suggest, and replace the NotImplementedError placeholders with the actual logic.

    Fix new_game: Ensure the new_game button uses the variables low and high derived from the selected difficulty instead of hard-coding 1 and 100.

I was kind of going back and forth between claude, copilot, and gemini, and they all seem profoundly good at coding and programming. Copilot reasons a lot and reading through it's dialogue is pretty ellucidating. 

It got a lot right and it didn't really mislead me at all. From my first impressions of the site I had good visibility into the bugs, and it never strayed outside the bugs I already knew were there, yet it did help me find better language to describe it.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I don't think AI got anything wrong.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

AI kept running pytests and i kept opening streamlit run app.py after each fix to tinker around and make sure for myself there was no unexpected behaaviors.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I continuously ran pytests, in fact Github CoPilot didn't stop writing and running tests on it's own throughout the process of debugging. I ran a few pytest in terminal and occasionally would chat back and forth in the chat window with AI to determine why I was seeing so much red.

- Did AI help you design or understand any tests? How?

No, actually, I will have to continue learning about testing and the test process, writing them, and will ready about pytest in documentation and try to find more info about the actual task and what to be focused on when in that phase.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
