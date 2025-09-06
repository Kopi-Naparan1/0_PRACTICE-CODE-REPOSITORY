import datetime
from todo_functions import tasks_loader, task_saver


def add_task(i, tasks: dict):
    task = input(f'Task [{i}]: ').lower().strip()
    tasks[str(i)] = f'Date: [{datetime.datetime.now().strftime("%A, %B %d, %Y")}] - {task}'

    print(f'{task} is added.')


def view_tasks(tasks: dict):
    print('=' * 30)
    print('====== TASKS ======\n')
    j = 1
    for task in tasks.values():
        print(f'Task [{j}]: {task}')
        j += 1
    print('=' * 30)
    print('')


def done_marker(tasks: dict):
    try:
        task = int(input('Number of task done: '))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 0 < task <= len(tasks):
        if ": Done" not in tasks[str(task)]:
            tasks[str(task)] += ": Done"
            print(f'Task [{task}] marked as done.')
        else:
            print(f'Task [{task}] is already marked as done.')
    else:
        print("Invalid task number.")



def task_remover(tasks: dict):
    task = int(input('Number of task to remove: '))
    if 0 < task <= len(tasks):
        task = tasks.pop(task)
        print(f'Task: {task} is removed ')
    else:
        print("Invalid task number.")


def main(username):
    i = 1
    tasks_dict = tasks_loader(username)

    while True:

        choice = input("""
        [1] Add a task
        [2] View tasks
        [3] Mark task as done
        [4] Remove a task
        [5] Quit
        choice: """)

        if choice == '1':
            add_task(i, tasks_dict)
            i += 1

        elif choice == '2':
            view_tasks(tasks_dict)

        elif choice == '3':
            done_marker(tasks_dict)

        elif choice == '4':
            task_remover(tasks_dict)

        elif choice == '5':
            print('Quiting...')
            task_saver(username, tasks_dict)
            break
