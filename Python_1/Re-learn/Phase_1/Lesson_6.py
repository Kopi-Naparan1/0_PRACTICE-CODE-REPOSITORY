from typing import Set, Tuple


def ask_name():
    return input("What is the student's name?  ")

def ask_age():
    return int(input("What is the student's age?  "))

def ask_grade():
    return float(input("What is the student's grade?  "))

def raw_data_formatter(name, age, grade):
    student = (name, age, grade)
    return student


def add_student(data: tuple, students: set):
    students.add(data)


def view_all_students(students: set):
    i = 0
    print("==========")
    print("=STUDENTS=")
    print("==========")
    for student in students:
        print(f"Student #{i + 1}")
        for data in student:
            print(data)
    print("==========")

def search_student(students: set, name: str):
    print("===========")
    for student in students:
        if student[0] == name:
            for data in student:
                print(data)
    print("===========")

def crud(students: set):

    while True:
        print("[1] Add student\n"
            "[2] View all students\n"
            "[3] Search a student\n"
            "[4] Save\n")

        choice: int = int(input("Input a number: "))

        if choice == 1:
            print(f"Student #{len(students) + 1}")

            # raw data of the student
            name: str = ask_name()
            age: int = ask_age()
            grade: float = ask_grade()

            # adds the student's raw data into the set
            student = raw_data_formatter(name, age, grade)
            add_student(student, students)
            print(f"student #{len(students)} added")
 
        elif choice == 2:
            view_all_students(students)

        elif choice == 3:
            name: str = input("Input Student number: ")
            search_student(students, name)

        else:
            print(f"--- Saved {len(students)} students' data---")
            return

        


def main():
    students: Set[Tuple[str, int, float]] = set()
    crud(students)



if __name__ == "__main__":
    main()