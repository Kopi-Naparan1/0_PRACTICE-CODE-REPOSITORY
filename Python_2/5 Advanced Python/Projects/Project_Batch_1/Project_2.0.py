import os
import json
import csv
import re

# Default folder
folder = os.path.join("C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course", "5 Advanced Python",
                      "Projects", "Project_Batch_1", "cache_files"
)


# get every html file in a directory
def html_batch_getter() -> list[str]:
    html_files = [os.path.join(folder, f)for f in os.listdir(folder) if f.endswith('.html') and os.path.isfile(os.path.join(folder, f))]
    print('Batch is ready...Opening...')
    return html_files


# read all those file in the directory -> html_file, string
def html_batch_reader(html_files):
    for html_file in html_files:
        print(f'\tOpening: {html_file}')

        try:
            with open(html_file, 'r', encoding='utf-8') as file:
                content = file.read()
                yield html_file, content

        except FileNotFoundError:
            print(f'File not found: [{html_file}]')
            yield html_file, None


# get title, and headlines by using regex
def headline_getter(html_content):
    headline_pattern = r"<(?:title|h1|h2)>(.*?)</(?:title|h1|h2)>"

    headlines = re.findall(headline_pattern, html_content)
    return headlines


def filter_headline_generator(headlines, keywords):

    for headline in headlines:
        if any(re.search(rf'\b{re.escape(k)}\b', headline, flags=re.IGNORECASE) for k in keywords):
            yield headline




def main():

    html_files = html_batch_getter()

    all_headlines = []
    filtered_headlines = []
    for file_name, content in html_batch_reader(html_files):


        if content:
            print(f'\n---{file_name} ---')
            headlines = headline_getter(content)
            all_headlines.extend(headlines)
            keywords = ['AI', 'War']
            headline = list(filter_headline_generator(headlines, keywords))
            if headlines:
                print("Headline found with tags 'AI', 'War': ")
                print(headline)
            else:
                print('No Headline/s are found. ')

        else:
            print(f"Skipping: {file_name} (no content)")

    output_folder = os.path.join(folder, "output")
    os.makedirs(output_folder, exist_ok=True)


    json_path = os.path.join(output_folder, "headlines.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"headlines": all_headlines}, f, indent=2)

    csv_path = os.path.join(output_folder, "headlines.csv")
    with open(csv_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["headline"])
        for h in all_headlines:
            writer.writerow([h])

    from collections import Counter

    keyword_counts = Counter()
    for h in all_headlines:
        for k in keywords:
            if k.lower() in h.lower():
                keyword_counts[k] += 1

    stats_path = os.path.join(output_folder, "stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(keyword_counts, f, indent=2)


if __name__ == "__main__":
    main()