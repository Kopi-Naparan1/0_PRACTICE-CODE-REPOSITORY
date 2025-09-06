from question_loader import load_json
import random

questions = load_json()


def game_questions(data: dict) -> list[dict]:
    five_questions = []

    random_key = random.sample(list(data.keys()), 5) # Get a number from 1-8, .sample- gets unique everytime
    for n in random_key:
        random_question = data[n] # put that number here, which gets the dictionary
        five_questions.append(random_question) # append that dictionary

    return five_questions


def user_input():
    answer = input('What is your answer? ')
    return answer
