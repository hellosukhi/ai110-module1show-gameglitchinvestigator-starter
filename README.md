# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
It's a guessing game, the game keeps the secret which is a number within a range and the user guesses it. I guess the purpose of the game is entertainment, but the larger purpose of it is to present a debugging challenge to us as it came with a lot of bugs.
- [ ] Detail which bugs you found.
I wrote about them in the reflection.md app. Mostly it was an assortment of little things and simply wasn't production grade. There was some UI issues, some logic and flow issues.
- [ ] Explain what fixes you applied.
I made a couple of changes to get the game to a minimally viable state but preserving what it is overall. It's still not product grade but the code is more organized, consolidated, and the logic is operational rather than flawed or erroneous, or producing erroenous outputs.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters 50, Game gives hint "GO HIGHER!"
2. User enters 75, Game says "Go LOWER!"
3. User enters 65, Game says "Go LOWER!" it says attempts left:5, user knows its between 50 and 65 now
4. Entered 60, says Go Lower!, attempts left:4
5. Entered 55, says Go Higher, attempts left:3
6. Entered 58, says Go Lower!, atempts left:2
7. Entered 56, says Go Higher!, attempts left: 1
8. Entered 57, says Correct! You Won. The secret was 57. Final score: -25 and Balloons stream up

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

I'm not going to do that mostly because I'm not sure how.

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

============== test session starts ===============
platform darwin -- Python 3.13.0, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/star/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 6 items                                

tests/test_game_logic.py ......            [100%]

=============== 6 passed in 0.01s ================
star@Mans-Laptop ai110-module1show-gameglitchinvestiga



## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
