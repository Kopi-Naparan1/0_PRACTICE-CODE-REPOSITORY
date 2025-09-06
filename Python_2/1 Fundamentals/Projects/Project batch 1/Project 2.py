class User:
    feedbacks = []

    def __init__(self, name, rating, suggestion):
        self.name = name
        self.rating = rating
        self.suggestion = suggestion
        info = {"Name": self.name,
                "Rating": self.rating,
                "Suggestion": self.suggestion,
                }
        User.feedbacks.append(info)


def collect_input():
    name = input('Name: ').strip().lower()
    while True:
        rating = int(input('Rate 1 - 5(highest): '))
        if rating > 5 or rating < 1:
            print('Error: Must be 1 - 5')
        else:
            break

    while True:
        suggestion = input(f'What is your suggestion {name}: ').strip()
        if not suggestion:
            print('Error: Add a suggestion')
        else:
            break

    return name, rating, suggestion


def display_summary():
    i = 1
    print('\n\n----- ALL FEEDBACK -----\n\n')
    for user in User.feedbacks:
        print(f'---User {i}---')
        for k, v in user.items():
            print(f'{k}: {v}')
        print('------------\n')
        i += 1
    print('-----------------------')


def main():
    i = 1

    while True:
        choice = input('''\n\nDo you want to:
        [1] view feedback/s 
        [2] Add feedback
        [3] Exit
        choice: ''').strip().lower()

        if choice == '1':
            display_summary()

        elif choice == '2':
            print(f'\n\n--- User {i} ---')
            name, rating, suggestion = collect_input()
            User(name, rating, suggestion)
            print(f'--- Feedback by {name} is added---')
            i += 1

        elif choice == '3':
            print('Exiting...')
            break




if __name__ == "__main__":
    main()
