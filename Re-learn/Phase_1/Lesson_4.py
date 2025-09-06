import random
from typing import Tuple



def get_random_number() -> int:
    number = random.randint(1, 100)
    return number

def guess_feedback(hidden_number: int, guess: int) -> Tuple[str, bool]:
    if guess > hidden_number:
        return "Too High", False
    elif guess < hidden_number:
        return "Too Low", False
    else:
        return f"You got it right it is {guess}", True

def guess_hidden_number() ->int :
    while True:
        try:
            return int(input("Guess the number: "))
        except ValueError:
            print("Invalid Input. Please enter a number from 1-100.")


def main():
    LIFE = 7
    

    hidden_number = get_random_number()

    while LIFE > 0:
        print(f"Life remaining: {LIFE}")
        guess: int = guess_hidden_number()
        feedback, is_correct = guess_feedback(hidden_number, guess)
        print(feedback)
        
        if is_correct:
            break

        LIFE -= 1
    if LIFE == 0:
        print(f"You lost! The hidden number is: {hidden_number}")


if __name__ == "__main__":
    main()


# I learned the type hinting of tuple and using functions effectively
        







