import os.path




def get_file_size(data) -> int:
    """Use recursion"""
    try:
        if os.path.exists(data):
            total = 0

            for file in os.listdir(data):
                full_path = os.path.join(data, file)

                if os.path.isfile(full_path):
                    total += os.path.getsize(full_path)

                elif os.path.isdir(full_path):
                    total += get_file_size(full_path)
            return total

    except FileNotFoundError as x:
        print(f'Error: {x}')




