import datetime


class Todo:
    i = 1
    tasks = []

    @staticmethod
    def add_task():
        task = input(f'Task [{Todo.i}]: ').lower().strip()
        Todo.tasks.append(f'Date: [{datetime.datetime.now().strftime("%A, %B %d, %Y")}] - {task}')
        Todo.i += 1
        print(f'{task} is added.')

    @staticmethod
    def view_tasks():
        print('=' * 30)
        print('====== TASKS ======\n')
        j = 1
        for task in Todo.tasks:
            print(f'Task [{j}]: {task}')
            j += 1
        print('=' * 30)
        print('')

    @staticmethod
    def done_marker():
        task = int(input('Number of task done: '))

        if 0 < task <= len(Todo.tasks):
            Todo.tasks[task - 1] = f"{Todo.tasks[task - 1]}: Done"
            print(f'{Todo.tasks[task - 1]} is done.')
        else:
            print("Invalid task number.")

    @staticmethod
    def task_remover():
        task = int(input('Number of task to remove: '))
        if 0 < task <= len(Todo.tasks):
            task = Todo.tasks.pop(task-1)
            print(f'Task: {task} is removed ')
        else:
            print("Invalid task number.")


def main():
    functions = {
        "1": Todo.add_task,
        "2": Todo.view_tasks,
        "3": Todo.done_marker,
        "4": Todo.task_remover,
    }

    while True:

        choice = input("""
        [1] Add a task
        [2] View a task
        [3] Mark task as done
        [4] Remove a task
        [5] Quit
        choice: """)

        if choice == '5':
            print('Quiting...')
            break

        elif choice in "1234":
            choice = functions.get(choice)
            choice()

        else:
            print('Input [1-5] only')


if __name__ == "__main__":
    main()
