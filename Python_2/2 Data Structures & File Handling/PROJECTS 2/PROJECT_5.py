import json
import os
from collections import defaultdict

folder = os.path.join(
    "C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
    "2 Data Structures & File Handling", "PROJECTS 2", "Cache_files"
)


def json_loader():
    search_file = input('Search File_name: ')
    file_path = os.path.join(folder, f"{search_file}.json")

    try:
        with open(file_path, 'r') as file:
            list_of_dictionary = json.load(file)
            print('--File found--')
            return list_of_dictionary

    except FileNotFoundError:
        print("-- File not found: Try again..--")
        return False


def num_feedback_analyzer(feedbacks):
    total_num_feedbacks = 0
    total_num_empty_feedbacks = 0
    cleaned_feedbacks = []

    for feedback in feedbacks:
        text = feedback.get("feedback", "").strip()
        if text == '':
            total_num_empty_feedbacks += 1

        else:
            total_num_feedbacks += 1
            cleaned_feedbacks.append(feedback)

    return total_num_feedbacks, total_num_empty_feedbacks, cleaned_feedbacks


def length_feedback_analyzer(feedbacks):
    sorted_list_feedbacks = sorted(feedbacks, key=lambda feedback: len(feedback["feedback"]), reverse=True)
    longest_feedback = sorted_list_feedbacks[0]
    shortest_feedback = sorted_list_feedbacks[-1]

    return longest_feedback, shortest_feedback


def sentiment_feedback_analyzer(feedbacks):
    words = []

    for feedback in feedbacks:
        if feedback["feedback"]:
            words.extend(feedback["feedback"].lower().split())
    positive_words = {'love', 'awesome', 'like', 'great', 'good', 'excellent'}
    negative_words = {'hate', 'bugs', 'bug', 'popups'}

    positive_words_count = defaultdict(int)
    negative_words_count = defaultdict(int)

    for word in words:
        word = word.strip(".!,?")
        if word in positive_words:

            positive_words_count[word] += 1
        elif word in negative_words:
            negative_words_count[word] += 1

    top_3_positive_words = sorted(positive_words_count.items(), key=lambda item: item[1], reverse=True)[:3]
    top_3_negative_words = sorted(negative_words_count.items(), key=lambda item: item[1], reverse=True)[:3]
    print(words)
    return top_3_positive_words, top_3_negative_words


def data_summarizer(num_feedback, empty_feedback, longest, shortest, top_pos, top_neg):
    full_summary = f"""
    Total number of feedback: {num_feedback}
    Total number of empty feedback: {empty_feedback}
    
    Longest feedback by: {longest['name']} {len(longest["feedback"])} characters:
                        - {longest["feedback"]}
                        
    Shortest feedback: {shortest['name']} {len(shortest["feedback"])} characters:
                        - {shortest["feedback"]}
    
    Top 3 positive words on feedbacks: {top_pos}
    Top 3 negative words on feedbacks: {top_neg}
    """

    return full_summary


def txt_saver(full_summary):
    name_file = input("Name your text file: ")

    file_path = os.path.join(folder, f"{name_file}.txt")

    with open(file_path, 'w') as file:
        file.write(full_summary)
        print('--File saved--')


def main():

    feedbacks_lists = json_loader()

    if not feedbacks_lists:
        return

    total_num_feedbacks, total_num_empty_feedbacks, cleaned_feedback = num_feedback_analyzer(feedbacks_lists)
    longest_feedback, shortest_feedback = length_feedback_analyzer(cleaned_feedback)
    top_3_positive_words, top_3_negative_words = sentiment_feedback_analyzer(feedbacks_lists)

    full_summary = data_summarizer(total_num_feedbacks, total_num_empty_feedbacks,
                                   longest_feedback, shortest_feedback,
                                   top_3_positive_words, top_3_negative_words
                                   )

    txt_saver(full_summary)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")

