import os


def list_files(path):
    return os.listdir(path)

def batch_rename(*files, **option):
    prefix = option.get("prefix", "")
    suffix = option.get('suffix', '')
    replace_ext = option.get('replace_ext', '')

    renamed_files = []
    for file in files:
        name, ext = os.path.splitext(file)
        new_name = f'{prefix}{name}{suffix}{replace_ext or ext}'
        renamed_files.append(new_name)
    return renamed_files



