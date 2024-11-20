import random

def make_phrase():
    try:
        with open("phrases.txt", "r") as fd:
            phrases = fd.read().splitlines()
        phrase = random.choice(phrases).upper()
    except FileNotFoundError:
        print("Couldn't find phrases.txt, make sure you have it in the same folder as this file.")
        return "When you gaze long into the abyss, the abyss gazes also into you".upper()
    except IndexError:
        print("phrases.txt seems to be empty. Add some phrases to it, one per line.")
    return phrase

def print_gallows(misses):
    hd, bd, ll, rl, la, ra = tuple("O|/\\\\/"[:misses] + (6 * " ")[misses:])
    print(f"+---+\n|   |\n|  {la}{hd}{ra}\n|   {bd}\n|  {ll} {rl}\n|\n|_____")
    print(f"Incorrect guesses made: {misses}/6")

def print_revealed_phrase(phrase, guessed_letters):
    revealed = [
        char if not char.isalpha() or char in guessed_letters else "_" for char in phrase
    ]
    print("".join(revealed))

def get_letter(guessed_letters):
    while True:
        guess = input("Please enter a letter: ").upper()
        if not guess.isalpha() or len(guess) != 1:
            print(f'"{guess}" is not a letter!')
        elif guess in guessed_letters:
            print(f'"{guess}" has already been guessed!')
        else:
            return guess

def won(phrase, guessed_letters):
    for char in phrase:
        if char.isalpha() and char not in guessed_letters:
            return False
    return True

def play_game():
    phrase = make_phrase()
    misses = 0
    guesses = []

    print("*** Welcome to Hangman ***")
    print_gallows(misses)
    print()

    while misses < 6:
        print_revealed_phrase(phrase, guesses)
        print("Letters guessed:", repr(sorted(guesses))) 
        print()  

        guess = get_letter(guesses)
        guesses.append(guess)

        if guess not in phrase:
            misses += 1
            print_gallows(misses)
            if misses == 6:
                print("Game Over!")
                print("Solution was:", phrase)
                return
        elif won(phrase, guesses):
            print_revealed_phrase(phrase, guesses)
            print("Congratulations!")
            return

play_game()
