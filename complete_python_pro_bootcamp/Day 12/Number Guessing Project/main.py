from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """ Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("🔺 Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("🔻 Too low")
        return turns - 1
    else:
        print(f"✅🏆 You got it! The number was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("🤗 Welcome to the Number Guessing Game!")
    print("🧏‍♂️ I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"🔵🟡 Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionally if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            return print("❌ 😰 You've run out of guesses, you lose!")
        elif guess != answer:
            print("🙋‍♂️🙋🏼‍♀️ Guess again!")

    # Track the number of turns and reduce by 1 if they get it wrong

game()
