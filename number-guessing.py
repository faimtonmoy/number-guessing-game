import random
import time
import os

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")


attempted_chances = 0


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_user_difficulty_choice():
    user_input = input("Enter your difficulty choice: ")
    if user_input == "1":
        print(
            "Great! You have selected the Easy difficulty level. "
            "You have 10 chances to guess the correct number."
        )
        return 10
    elif user_input == "2":
        print(
            "Great! You have selected the Medium difficulty level. "
            "You have 5 chances to guess the correct number."
        )
        return 5

    else:
        print(
            "Great! You have selected the Hard difficulty level. "
            "You have 3 chances to guess the correct number."
        )
        return 3


def get_valid_guess():
    while True:
        user_input = input("Enter your guess: ")

        if not user_input.isdigit():
            print("❌ Please enter a valid number.")
            continue

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("❌ Number must be between 1 and 100.")
            continue

        return guess


def main_game(attempted_chances):
    won = False
    rand_number = random.randint(1, 100)
    print(rand_number)
    user_choice = get_user_difficulty_choice()
    start_time = time.time()
    while attempted_chances < user_choice:
        attempted_answer = get_valid_guess()
        if attempted_answer == rand_number:
            print(
                f"Congratulations! You guessed the correct number in {attempted_chances + 1} attempts."
            )
            won = True
            end_time = time.time()
            print(
                f"It took you {end_time-start_time} seconds to guess the answer correctly"
            )
            break

        elif attempted_answer > rand_number:
            print(f"Incorrect! The number is less than {attempted_answer}.")

        else:
            print(f"Incorrect! The number is greater than {attempted_answer}.")

        attempted_chances += 1

    if not won:
        print("You have used all your chances, better luck next time")


while True:
    main_game(attempted_chances)
    user_quit_choice = input("Do you want to continue?(Y/N): ")
    if user_quit_choice == "N":
        break
    clear_screen()
