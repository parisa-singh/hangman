# Hangman Game

## Overview

This is a Python implementation of the classic **Hangman** game, where the player tries to guess a randomly selected phrase, one letter at a time. The goal is to guess the phrase before the gallows are fully drawn (6 incorrect guesses).

## Features
- Random phrase selection from an external file (`phrases.txt`).
- Interactive gameplay with input validation.
- Displays the hangman figure as incorrect guesses are made.
- Tracks guessed letters and reveals correctly guessed letters in the phrase.
- Supports case-insensitive guessing.

## How to Play

1. When you start the game, you'll see a partially drawn gallows and the phrase represented as underscores (`_`), hiding unguessed letters.
2. Guess one letter at a time by typing it in when prompted.
   - Correct guesses reveal the letter in the phrase.
   - Incorrect guesses add parts to the gallows.
3. The game ends when:
   - You guess the full phrase correctly, or
   - You make 6 incorrect guesses, completing the gallows.

## Requirements

- Python 3.x

3. **Run the Game**  
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Execute the script:
     ```
     python hangman.py
     ```

## Example Gameplay

```
*** Welcome to Hangman ***
+---+
|   |
|   
|   
|    
|
|_____
Incorrect guesses made: 0/6

____ __ _______
Letters guessed: []

Please enter a letter: A
...
```

---

## Error Handling

- If `phrases.txt` is missing, a default phrase will be used:  
  `"When you gaze long into the abyss, the abyss gazes also into you"`
- If `phrases.txt` is empty, the game will notify the user and terminate.

## Contributions

Feel free to submit issues or improvements to the code via pull requests.

## License

This project is open-source and available under the MIT License.
