import random

"""
Random Number Guessing Game

This Python script generates a random number between 1 and 100 and then prompts the user to guess the number. 
If the user's guess is incorrect, the script provides feedback and allows the user to continue guessing until the correct number is guessed.

Usage:
1. Run the script.
2. The script will generate a random number between 1 and 100.
3. The user will be prompted to guess the number.
4. If the guessed number is incorrect, the script will inform the user and prompt for another guess.
5. This process continues until the correct number is guessed.
6. The script will provide feedback on the number of attempts taken.

Example of usage:
$ python Guess_the_number.py
I want to play the game 'Guess the number'.
Please enter a number from 1 to 100: 50
Incorrect! Try again.

Please enter a number from 1 to 100: 75
Well, that is not correct, try again. Try smaller number.

Please enter a number from 1 to 100: 30
Well, that is not correct, try again. Try bigger number.

Please enter a number from 1 to 100: 60
Yes! That's correct! 60 is The Number.
"""
def ask_for_number():
    """
    The ask_for_number function prompts the user to enter a natural number in the range from 1 to 100.

    Returns:
    int: The natural number entered by the user.

    This function uses the `input()` function to collect user input. If the user enters a value that is not an
    integer, an error message is displayed, and the function requests the user to enter the data again.
    If the user enters a number that is outside the range of 1 to 100, an error message is also displayed, and the
    function asks for input again.
    Upon successful entry of a number, the function returns that number.

    Example of usage:
    >>> number = ask_for_number()
    Please enter a number from 1 to 100: 42
    >>> print(number)
    42
    """

    while True:
        number = input("Guess the number:")
        try:
            if not (int(number) > 0 and int(number) <= 100):
                print("Please enter a number from 1 to 100:")
            else:
                return int(number)
        except ValueError:
            print("Expected integer!")
        except TypeError:
            print("Expected integer!")

print("I want to play the game 'Guess the number'." )

number_to_guess = random.randint(1,100)
number = ask_for_number()

while number != number_to_guess:
    if number > number_to_guess:
        print("Well, that is not correct, try again. Try smaller number.")
    else:
        print("Well, that is not correct, try again. Try bigger number.")
    number = ask_for_number()

print(f"Yes! That's correct! {number} is The Number.")
