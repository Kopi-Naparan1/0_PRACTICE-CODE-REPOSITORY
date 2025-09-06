from datetime import datetime

def get_time():
    return datetime.now().strftime("[%Y-%m-%d %H:%M]")

def save_journal_entry(entry: str):
    try:
        with open("journal.txt", "a") as f:
            f.write(entry)
    except FileNotFoundError:
        with open("journal.txt", "w") as f:
            f.write(entry)
    finally:
        print("Journal is saved.")


def get_journal_entry(time):
    entry = input("Your journal entry: ")
    journal = (f"{time}\n{entry}\n\n")
    return journal


def read_journal():
    try:
        with open("journal.txt", "r") as f:
            journal = f.read()
            print(journal)
    except FileNotFoundError:
        print("File not found. Try again")

def crud():
    time = get_time()

    while True:
        choice: int = int(input("Do you want to (1) write a new entry or (2) read all entries? (3) quit: "))

        if choice == 1:
            journal_entry = get_journal_entry(time)
            save_journal_entry(journal_entry)

        elif choice == 2: 
            read_journal()

        else:
            print("Leaved")
            return

def main():
    crud()



if __name__ == "__main__": 
    main()