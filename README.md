# 🎯 Number Guessing Game (Python CLI)

A simple and interactive command-line number guessing game built with Python. The game generates a random number between 1 and 100, and the player must guess it within a limited number of attempts based on selected difficulty.

---

## 🚀 Features

- 🎲 Random number generation (1–100)
- 🎚️ Three difficulty levels:
  - Easy → 10 attempts
  - Medium → 5 attempts
  - Hard → 3 attempts

- 🧠 Input validation:
  - Only accepts numeric input
  - Ensures guesses are between 1 and 100

- 💬 Helpful hints after each guess:
  - "Higher" or "Lower" feedback

- ⏱️ Tracks time taken to guess correctly
- 🧹 Clears CLI screen between games for a clean experience
- 🔁 Option to replay the game

---

## 🛠️ Tech Stack

- Python 3
- Built-in modules:
  - `random` → number generation
  - `time` → performance tracking
  - `os` → clearing terminal screen

---

## 📦 How to Run

### 1. Clone or download the file

```bash
git clone https://github.com/faimtonmoy/number-guessing-game
cd number-guessing-game
https://roadmap.sh/projects/number-guessing-game
```

### 2. Run the script

```bash
python guess_game.py
```

---

## 🎮 How to Play

1. Run the program
2. Choose difficulty:
   - `1` → Easy (10 chances)
   - `2` → Medium (5 chances)
   - `3` → Hard (3 chances)

3. Enter guesses between **1 and 100**
4. Get hints after each guess:
   - "The number is greater"
   - "The number is less"

5. Win by guessing correctly within allowed attempts
6. Choose whether to play again

---

## 📊 Example Gameplay

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Enter your difficulty choice: 2
Enter your guess: 50
Incorrect! The number is greater than 50.

Enter your guess: 75
Congratulations! You guessed the correct number in 2 attempts.
It took you 4.12 seconds to guess the answer correctly

Do you want to continue?(Y/N): Y
```

---

## ⚠️ Notes

- Input validation prevents crashes from invalid inputs
- Terminal is cleared between games for better UX
- The random number is currently printed for debugging — remove this line for production:

  ```python
  print(rand_number)
  ```

---

## 🔧 Possible Improvements

- 🎯 Fix attempt counter accuracy (currently resets per loop logic improvement needed)
- 🏆 Add high score system
- 💾 Store game history locally
- 🎨 Add colored CLI output (using `colorama`)
- 📈 Add difficulty scaling (dynamic ranges)
- 🌐 Convert into a web version (Flask / Next.js API)

---

## 👨‍💻 Author

Mohammed Faim Uddin Bhuiyan

---

## 📌 Learning Outcome

This project helps practice:

- Control flow in Python
- Input validation techniques
- Loop design for games
- Basic CLI UX design
- Time measurement in programs
- Cross-platform terminal handling

---
