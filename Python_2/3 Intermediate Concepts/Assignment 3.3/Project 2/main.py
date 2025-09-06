import argparse
from cleaner import capitalize_name, remove_inactive_users, lowercase_email


parser = argparse.ArgumentParser()

parser.add_argument('--file', required=True)

args = parser.parse_args()


capitalize_name(args.file)
lowercase_email(args.file)

status = remove_inactive_users(args.file)

for key, value in status.items():
    print(f'{key}: {value}')
