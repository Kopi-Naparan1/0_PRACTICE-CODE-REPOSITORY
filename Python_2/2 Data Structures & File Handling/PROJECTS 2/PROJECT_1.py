import datetime
import os


def info():
    name = input("Name: ")
    email = input("Email: ")
    feedback = input("Feedback: ")

    userinfo = {"Name": name, "Email": email, "Feedback": feedback}
    return userinfo


def save_to_txt(userinfo):
    folder = os.path.join(
        "C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
        "2 Data Structures & File Handling", "PROJECTS 2", "Cache_files"
    )

    file_name = os.path.join(folder, 'feedback.txt')
    feedback = f'[{datetime.datetime.now().strftime("%A, %B %d, %Y")}] {userinfo["Name"]} - {userinfo["Email"]} Said: {userinfo["Feedback"]}\n'

    # os.makedirs(folder, exist_ok=True)

    with open(file_name, 'a') as file:
        file.write(feedback)
        print('File is saved')


def main():
    information = info()
    save_to_txt(information)


if __name__ == '__main__':
    main()