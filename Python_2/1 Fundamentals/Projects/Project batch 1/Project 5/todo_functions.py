import json
import os

folder = (r"C:\KOPI ANAN PASCO NAPARAN\PROGRAMMING\Python Course\1 Fundamentals\Projects\Project batch 1\Project "
          r"5\tasks")


def task_saver(username, tasks):
    file_name = os.path.join(folder, f'{username} tasks.json')
    try:
        with open(file_name, 'w') as file:
            json.dump(tasks, file, indent=4)
            print('Tasks saved')

    except FileNotFoundError:
        print('FNF - Failed to save tasks')

    except json.JSONDecodeError:
        print('JSONDE - Failed to save tasks')


def tasks_loader(username):
    file_name = os.path.join(folder, f'{username} tasks.json')
    try:
        with open(file_name, 'r') as file:
            read = json.load(file)
            return read
    except FileNotFoundError:
        print('New File is made...')
        return {}

    except json.JSONDecodeError:
        print('Json decode error - task loader...')
        return {}
