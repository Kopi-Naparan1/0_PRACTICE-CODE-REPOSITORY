from game import game_questions, user_input
from question_loader import load_json

list_of_dict = load_json()
five_questions:list = game_questions(list_of_dict)

def correct_answers():
    i = 1
    print('-' * 30)
    print('-------Correct Answers---------')
    for key in five_questions:
        answer = key['answer']
        print(f'{i}. {answer}')
        i += 1
    print('-' * 30)


def game_start(display_correct):

    i = 0

    for key in five_questions: # prints the questions and the choices
        print(f'{i+1} {key['question']}')
        for k, v in key['choices'].items():
            print(f'{k}. {v}')

        answer = user_input()

        # if user answer if equals to dictionary answer then it will stay in the list
        correct_answers = [q['answer'] for q in five_questions if answer == q['answer']]

        correct = len(correct_answers)
        incorrect = len(five_questions) - len(correct_answers)

        print(f'Total correct score: {correct}')
        print(f'Total incorrect score: {incorrect}')

        i += 1
    display_correct()




def main():
    """To do:
    1. Make user know which one is correct and not
    2. Add error handling: try, except
    3. Make it user-friendly by adding more convo"""
    game_start(correct_answers)





if __name__ == "__main__":
    main()
