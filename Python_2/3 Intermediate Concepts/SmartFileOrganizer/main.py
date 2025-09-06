from organizer import batch_rename, list_files
from reporter import folder_size, filter_files
import argparse


files = ["file1.txt", 'file2.txt', 'file3.txt']
new_files = batch_rename(*files, prefix='old_', replace_ext=".bak")

filtered = filter_files(files, '.txt')
print(filtered)

parser = argparse.ArgumentParser()
parser.add_argument("command", choices=['organize', 'report'])
parser.add_argument("--path", required=True)
args = parser.parse_args()

if args.command == 'report':
    print(f'Folder size: {folder_size(args.path)} bytes')


"C:\KOPI ANAN PASCO NAPARAN\PROGRAMMING\Python Course\3 Intermediate Concepts\SmartFileOrganizer"