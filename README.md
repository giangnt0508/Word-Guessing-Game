# Word Guessing Game

A word guessing game built with Python, including both a graphical user interface (GUI) and a command-line interface (CLI). Players select a difficulty level, guess individual letters, and try to find the secret word before running out of lives.

## Features

- Three difficulty levels: Easy, Medium, and Hard.
- A GUI built with Tkinter.
- Guess letters by clicking the on-screen buttons or using the physical keyboard.
- Display hints, remaining lives, score, and guessed letters.
- Hearts show the remaining lives.
- Save game history to `game_history.txt`.
- A command-line version for terminal use.

## Requirements

- Python 3.8 or later.
- Tkinter, which is usually included with Python on Windows.
- No external libraries are required.

## Project Structure

```text
Folder/
├── cli_app.py                 # Command-line version
├── engine.py                  # Core game logic
├── gui_app.py                 # Graphical interface version
├── game_history.txt           # Game history
├── words/
│   ├── easy.txt               # Easy words
│   ├── medium.txt             # Medium words
│   └── hard.txt               # Hard words
└── README.md
```

## Running the Graphical Interface

Open a terminal in the project folder and run:

```bash
python gui_app.py
```

Select a difficulty level. Once the game starts, you can click the on-screen letter buttons or press letters on the physical keyboard.

## Running the CLI Version

```bash
python cli_app.py
```

In the CLI, enter the number for your selected difficulty and then enter individual letters to guess. Enter `quit` during a game to exit the current round.

## Word File Format

Each line in the files inside the `words/` folder must use the following format:

```text
WORD|Hint for the word
```

Ví dụ:

```text
APPLE|A red or green fruit
```

The `|` character separates the word from its hint. Neither the word nor the hint can be empty.

## Game Rules

- Each round starts with 6 lives.
- Correct guesses reveal the positions of the guessed letter in the word.
- Incorrect guesses remove 1 life.
- Correct letters earn points based on the number of times they appear in the word.
- The player wins by guessing all the letters in the word.
- The player loses when there are no lives remaining.

## Game History

When a game ends, its result is appended to `game_history.txt` using the following format:

```text
timestamp|difficulty|word|result|score|number_of_guesses
```

## Author

Truong Giang Nguyen  
Student ID: 202572186
