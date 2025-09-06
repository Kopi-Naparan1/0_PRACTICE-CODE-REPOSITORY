from collections import Counter


def word_count(file):
    count = []
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            count.append(len(line.split()))
        return sum(count)

def top_five_common_words(file):
    count = []
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            count.extend(line.split())
        return Counter(count).most_common(5)

def lines_number(file):
    count = []

    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            count.append(1)
        return sum(count)

def number_characters(file):
    with open(file, 'r', encoding="utf-8") as f:
        read = f.read()
        return len(read)
