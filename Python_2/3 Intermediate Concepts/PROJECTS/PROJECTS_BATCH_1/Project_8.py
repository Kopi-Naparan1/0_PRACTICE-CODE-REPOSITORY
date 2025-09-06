import os
import json
from typing import List, Dict
from collections import defaultdict


folder = os.path.join("C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
                      "3 Intermediate Concepts", "PROJECTS", "cache_files")


def search_file_names() -> List[str]:
    """Acts as a placeholder of filenames, return list of filenames """
    file_names = []
    while True:
        file_name = input('Search Filename ["q" to quit]: ')
        if file_name == 'q':
            break
        file_names.append(file_name)
    return file_names


def json_data_processor(*file_names) -> List[Dict]:
    """Gets json filenames, loop each, put the data into a list"""

    list_data = []

    for file_name in file_names:
        file_path = os.path.join(folder, f"{file_name}.json")
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                print(f"{file_name} - File Found")
                list_data.extend(data)
        except FileNotFoundError:
            print(f'Error: {file_name} - Not Found ')
        except json.JSONDecodeError :
            print(f'Error: {file_name} - JSON_ERROR  ')
    return list_data


def contact_list_cleaner(contacts_information: List[Dict]) -> List[Dict]:

    def clean_dictionary(contact: Dict):
        contact['name'] = contact.get('name', '').strip()
        contact['email'] = contact.get('email', '').strip()
        contact['phone'] = contact.get('phone', '').strip()

        tags = contact.get('tags', [])

        if isinstance(tags, list):
            contact['tags'] = [tag.lower() for tag in tags if isinstance(tag, str)]
        else:
            contact['tags'] = []

        return contact

    cleaned_contacts = list(map(clean_dictionary, contacts_information))

    # Only Include contacts with complete information
    valid_contacts_information = list(filter(lambda info: info['name'] and info['email'] and info['phone'], cleaned_contacts))

    return valid_contacts_information


def filter_contacts(contacts: List[Dict], domain=None, required_tags=None) -> List[Dict]:

    if domain:
        valid_contacts = list(filter(lambda x: x["email"].endswith(f"@{domain}"), contacts))
    else:
        valid_contacts = contacts

    if required_tags:
        valid_contacts = [c for c in valid_contacts if all(tag in c['tags'] for tag in required_tags)]

    return valid_contacts


def summarize_contacts(contacts: List[Dict]):
    if not contacts:
        return 0, {}, {}

    domain_number = defaultdict(int)
    tag_number = defaultdict(int)
    total_contacts = len(contacts)

    for contact in contacts:
        if '@' in contact['email']:
            domain = contact['email'].split('@')[1]
            domain_number[domain] += 1

        tags = contact.get('tags', [])

        for tag in tags:
            tag_number[tag] += 1

    return total_contacts, dict(domain_number), dict(tag_number)


def string_formatter(total_contacts, domain_number, tag_number):
    domain_line = [f"{key}: {value}" for key, value in domain_number.items()]
    domain_summary = '\n'.join(domain_line)

    tag_line = [f"{key}: {value}" for key, value in tag_number.items()]
    tags_summary = '\n'.join(tag_line)

    summary = (f"=========================================\n"
               f"Total valid contacts: {total_contacts}\n\n"
               f"---Domain Summary---\n"
               f"{domain_summary}\n\n"
               f"---Tags Summary---\n"
               f"{tags_summary}\n"
               f"=========================================")

    return summary


def dictionary_formatter(total_contacts, domain_number, tag_number) -> dict:
    summary = {"Total Contacts": total_contacts,
               "Domains Summary": domain_number,
               "Tags Summary": tag_number}

    return summary


def json_or_txt_saver(summary, unformatted_data_dict, mode='txt'):
    file_name = input('Name your file: ')
    file_path = os.path.join(folder, f"{file_name}.{mode}")

    with open(file_path, 'w') as file:
        if mode == 'txt':
            file.write(summary)
        elif mode == 'json' and unformatted_data_dict is not None:
            json.dump(unformatted_data_dict, file, indent=4)
        else:
            print('Error: Unsuccessful Data Saving')
            return

    print(f'File: {file_name}.{mode} saved Successfully')


def main():
    file_names = search_file_names()
    contact_information: List[Dict] = json_data_processor(*file_names)
    valid_contact_information: List[Dict] = contact_list_cleaner(contact_information)
    filtered_contacts: List[Dict] = filter_contacts(valid_contact_information)
    total_contacts, domain_number, tag_number = summarize_contacts(filtered_contacts)
    dictionary_summary = dictionary_formatter(total_contacts, domain_number, tag_number)
    summary = string_formatter(total_contacts, domain_number, tag_number)
    json_or_txt_saver(summary, dictionary_summary, mode="json")


if __name__ == "__main__":
    main()
