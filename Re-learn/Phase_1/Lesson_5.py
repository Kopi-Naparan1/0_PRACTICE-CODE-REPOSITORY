from random import randint

def get_random_number() -> int:
    return randint(1, 100)


def get_guess() -> int:
    
    
    while True:
        try: 
            guess = int(input("Guess a number: "))
            if 1 <= guess <= 100: 
                return guess
            else:
                print("Number must be between 1 and 100")
        except ValueError:
            print("Invalid input. Enter a number.")
        
def validate_guess(hidden_number: int, guess: int) -> bool:
    return guess == hidden_number

def message_life(life: int) -> str:
    return f"{life} remaining"

def message_win(highest_life_score: int, life: int, hidden_number) -> str:
    if life > highest_life_score:
        result = (f"Congrats you guessed {hidden_number}! you beat the highest_score with {life} remaining! ")
    else:
        result = (f"Congats You won! You guessed {hidden_number} \n Highest Life Score: {highest_life_score} \n Your Life Score: {life} ")
    
    return result
    
def message_lose(hidden) -> str:
    result = f"You lost the hidden number is {hidden}"
    return result
    
    
def message_feedback(hidden_number: int, guess: int) -> str:
    if guess > hidden_number:
        result = f"Make your guess lower"
    else:
        result = f"Make your guess Higher"
    return result

def shall_continue(choice: int) -> bool:
    return choice == 1


def main():
    highest_score = 0

    LIFE = 10
    hidden_number: int = get_random_number()

    while LIFE > 0:
        guess: int = get_guess()
        is_correct = validate_guess(hidden_number, guess)

        if not is_correct:
            LIFE -= 1
            print(message_life(LIFE))
            print(message_feedback(hidden_number, guess))

            if LIFE == 0:
                print(message_lose(hidden_number))
                hidden_number: int = get_random_number()
                return

        elif is_correct:
            if LIFE > highest_score:
                highest_score = LIFE
            print(message_win(highest_score, LIFE , hidden_number))
            
            hidden_number: int = get_random_number()
            LIFE = 10

            choice: int = int(input("Continue playing the game? 1 for yes, 0 for no: "))
            if not shall_continue(choice):
                break
main()




















