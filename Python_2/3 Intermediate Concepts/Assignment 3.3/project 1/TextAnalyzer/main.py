import argparse
from analyzer import word_count, top_five_common_words, lines_number, number_characters

parser = argparse.ArgumentParser()
parser.add_argument('--file', required=True)

args = parser.parse_args()

print(f'Word Count: {word_count(args.file)}')
print(f'Line Numbers: {lines_number(args.file)}')
print(f'Character Numbers: {number_characters(args.file)}')

top_words = top_five_common_words(args.file)

print(f'Top 5 words: ')
i = 1
for word, n in top_words:
    print(f"[{i}]   {word}  : {n}x")
    i += 1


"C:\KOPI ANAN PASCO NAPARAN\PROGRAMMING\Python Course\3 Intermediate Concepts\Assignment 3.3\project 1\TextAnalyzer"
