import os

folder = os.path.join(
        "C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
        "2 Data Structures & File Handling", "PROJECTS 2", "Cache_files"
    )


def txt_loader():
    name = input('Search txt filename: ').strip()
    file_name = os.path.join(folder, f"{name}.txt")

    try:
        with open(file_name, 'r') as file:
            info = [line.strip() for line in file]

            split_infos = []
            skipped = 0
            for line in info:
                line_splitted = line.split()
                if len(line_splitted) == 4:
                    split_infos.append(line_splitted)
                else:
                    skipped += 1

            print(f"Error logs: {skipped}")

            print("File is loaded.")
            return split_infos, name

    except FileNotFoundError:
        print('New File is made...')
        return [], name


def dict_formater(list_of_data) -> dict:
    dictionary = {}

    for entry in list_of_data:
        ip, _, method, endpoint = entry

        if ip not in dictionary:
            dictionary[ip] = {
                "Visited": 0,
                "Posts": {"Total number of posts": 0, "Log in": 0, "Submit": 0, "Update": 0, "Feedback": 0},
                "Get": {"Total number of get": 0, "Home": 0, "Contact": 0, "About": 0, "Dashboard": 0, "Admin": 0,
                        "Profile": 0}
            }

        if method == "POST":
            dictionary[ip]["Visited"] += 1
            dictionary[ip]["Posts"]["Total number of posts"] += 1
            if endpoint == "/login":
                dictionary[ip]["Posts"]["Log in"] += 1
            elif endpoint == "/submit":
                dictionary[ip]["Posts"]["Submit"] += 1
            elif endpoint == "/update":
                dictionary[ip]["Posts"]["Update"] += 1
            elif endpoint == "/feedback":
                dictionary[ip]["Posts"]["Feedback"] += 1

        elif method == "GET":
            dictionary[ip]["Visited"] += 1
            dictionary[ip]["Get"]["Total number of get"] += 1
            if endpoint == "/home":
                dictionary[ip]["Get"]["Home"] += 1
            elif endpoint == "/contact":
                dictionary[ip]["Get"]["Contact"] += 1
            elif endpoint == "/about":
                dictionary[ip]["Get"]["About"] += 1
            elif endpoint == "/dashboard":
                dictionary[ip]["Get"]["Dashboard"] += 1
            elif endpoint == "/admin":
                dictionary[ip]["Get"]["Admin"] += 1
            elif endpoint == "/profile":
                dictionary[ip]["Get"]["Profile"] += 1

    return dictionary


def save_summary(dictionary: dict):
    list_of_times_visited = []
    for key, value in dictionary.items():
        list_of_times_visited.append((key, value["Visited"]))
    list_of_times_visited.sort(key=lambda x: x[1], reverse=True)

    print('Top Visitors:')
    i = 1
    data = []
    for ip, times in list_of_times_visited:
        data.append(f"[{i}] {ip} - {times} visited \n")
        i += 1

    file_name = os.path.join(folder, "log_summary.txt")
    with open(file_name, 'w') as file:
        for line in data:
            file.write(line)
    print("Data is saved")


def main():
    info, name = txt_loader()
    dictionary = dict_formater(info)
    save_summary(dictionary)


if __name__ == "__main__":
    main()