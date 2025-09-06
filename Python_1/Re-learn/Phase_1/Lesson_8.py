from collections import defaultdict
import string

def get_paragraph() -> str:
    return input("Input a paragraph: ")

def count_words(paragraph: str) -> int:
    words = paragraph.split(" ")
    return len(words)

def get_unique_words(paragraph: str) -> set:
    unique_words = set(paragraph.split())
    return unique_words

def get_three_common_words(paragraph: str) -> dict[str, int]:
    words = paragraph.split()

    word_counts = defaultdict(int)

    for word in words:
        word_counts[word] += 1

    top_three =  list(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))[:3]
    return dict(top_three)

def format_paragraph_no_punctuation(paragraph: str) -> str:
    return "".join(character for character in paragraph if character not in string.punctuation)
    

def print_summary(cleaned_text, word_count, unique_words, top_three: dict):
    print("========================")
    summary = (f"Cleaned Text: {cleaned_text}\n\n"
               f"Word Count: {word_count}\n\n"
               f"Unique Words: {unique_words}\n\n"
               f"Top Three: {top_three}\n")
    
    print(summary)
    print("========================")

def main():
    paragraph = get_paragraph()
    clean_paragraph = format_paragraph_no_punctuation(paragraph)

    word_count = count_words(clean_paragraph)
    unique_words = get_unique_words(clean_paragraph)
    top_three_words = get_three_common_words(clean_paragraph)

    print_summary(clean_paragraph, word_count, unique_words, top_three_words)



if __name__ == "__main__": 
    main()