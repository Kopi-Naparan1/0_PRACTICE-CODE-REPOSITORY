import os.path
import shutil



# Organizing


def file_mover(data, move_to) -> None:
    try:
        if os.path.exists(data):
            shutil.move(data, move_to)
            print(f'{data} moved successfully to {move_to}.')

    except FileNotFoundError as x:
        print(f'Error: {x}')


def renamer(data, new_data) -> None:
    try:
        if os.path.exists(data):
            os.rename(data, new_data)
            print(f'{data} is renamed successfully to {new_data}')

    except FileNotFoundError as x:
        print(f'Error: {x}')


def deleter(data)-> None:
    try:
        if os.path.exists(data):
            os.remove(data)
            print(f'{data} removed successfully')
    except FileNotFoundError as x:
        print(f'Error: {x}')


def sorter(data) -> None:
    """Sort file by name or date by using lambda"""
    try:
        if os.path.exists(data):
            files = os.listdir(data)
            sorted_files = sorted(files, key=lambda f: os.path.getmtime(os.path.join(data, f)), reverse=True)
            print(f'---SORTED FILES---')
            i = 1
            for file in sorted_files:
                print(f'{i} {file}')

    except FileNotFoundError as x:
        print(f'Error: {x}')

