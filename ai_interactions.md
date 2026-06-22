# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Copilot, I said " need advanced edge case testing, what happens if inputs are large numbers, negative numbers, zero, or letters or special characters?  generate a suite of `pytest` cases that verify your game handles these inputs gracefully. i will then need the test output "

**What did the agent do?**

Copi said "I’m reproducing the game logic and reading the tests now so I can trace how inputs are validated before adding edge-case coverage" , then investigated and reviewed 4 files, then said "The edge cases are clear now; I’m adding targeted tests that cover extreme numeric values and malformed text inputs so the behavior is explicit."

Edge-case test suite added
The new coverage in test_game_logic.py now checks that the game logic gracefully handles:

zero, negative, and very large integers
malformed inputs like 1.5, 1,000, 12abc, @#, and 1e3
extreme comparison behavior for values far below and above the secret
🧪 Test run
I verified the suite with: pytest

Output:

.........                                                                [100%]
9 passed in 0.01s

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
|zero |0 |Go Higher |Y |No more hints necessary as the range is specified |
|negative |-100 | Go LOWER|Y |No more hints necessary as the range is specified|
|very large numbers |6000000 | Go LOWER | Y | No more hints necessary as the range is specified |

also if non numbers are entered it says: "That is not a number"
---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
