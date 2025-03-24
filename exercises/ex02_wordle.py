"""Wordle Guessing game"""

__author__ = "730761985"


def contains_char(word: str, char: str) -> bool:
    """checks if a character is present in the word"""
    assert len(char) == 1, f"len('{char}') is not 1"

    i = 0
    while i < len(word):
        if word[i] == char:
            return True
        i += 1
    return False


WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """returns emojis representing the accuracy of the guess."""
    assert len(guess) == len(
        secret
    ), "the guessed word must be the same length as the secret word (5 chars)"

    result = ""
    i = 0

    while i < len(guess):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1

    return result


def input_guess(expected_length: int) -> str:
    """prompts user for a word of proper length"""
    guess = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """runs the loop until a win or loss"""
    turns = 1
    max_turns = 6
    won = False

    while turns <= max_turns and not won:
        print(f"Turn {turns}/{max_turns}")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            won = True
        else:
            turns += 1

    if won:
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
