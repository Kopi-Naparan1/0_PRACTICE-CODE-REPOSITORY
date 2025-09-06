import argparse
import os.path

from organizer import renamer, deleter, file_mover, sorter
from utils import format_size
from Analyzer import get_file_size

parser = argparse.ArgumentParser()
parser.add_argument('--command', choices=['transfer', 'delete', 'rename', 'sort', 'get_file_size'])
parser.add_argument('--file')
parser.add_argument('--new')
args = parser.parse_args()
abs_path = os.path.abspath(args.file)

move = r"C:\KOPI ANAN PASCO NAPARAN\PROGRAMMING\Python Course\3 Intermediate Concepts\
Assignment 3.3\Project 5\Test Directory\here"



def functions():
    if args.command == 'transfer':
        file_mover(abs_path, move)
    elif args.command == 'delete':
        deleter(abs_path)
    elif args.command == 'sort':
        sorter(abs_path)
    elif args.command == 'rename':
        renamer(abs_path, args.new)
    elif args.command == 'get_file_size':
        size = get_file_size(abs_path)
        print(f'Total size: {format_size(size)} bytes')


def main():
    functions()


if __name__ == '__main__':
    main()
