from typing import Dict, Union


# region get raw data

def get_name():
    return input("What is the student's name?  ")

def get_age():
    return int(input("What is the student's age?  "))

def get_grade():
    return float(input("What is the student's grade?  "))

# endregion

# region CRUD functions

def add_student(students: dict, student_data: dict):
    students.update(student_data)
    for key in student_data.keys():
        print(f"Student {key} is added.")

def update_student(students: dict, student_id):
    try: 
        new_age = int(input("Input new age: "))
        students[student_id]["age"] = new_age

        if new_age is None:
            students[student_id]["age"] = students[student_id]["age"]

    except ValueError:
        print("Please make sure that it is an integer. Try again.")
        students[student_id]["age"] = students[student_id]["age"]

    try: 
        new_grade = float(input("Input new grade: "))
        students[student_id]["grade"] = new_grade

        if new_grade is None:
            students[student_id]["grade"] = students[student_id]["grade"]

    except ValueError:
        print("Please make sure that it is an integer/float. Try again.")
        students[student_id]["grade"] = students[student_id]["grade"]

    print("---Updated---")


def search_student(students: dict, student_id):
    print(f"===== {student_id} =====")
    for key, value in students.items():
        if student_id == key:   
            for k, v in value.items():
                print(f"{k}: {v}")
    print("================")    

# endregion

# region crud helpers
def format_raw_data( student_id: int, name: str, age: int, grade: float,):
    student = {student_id : {"name": name,
                  "age": age,
                  "grade": grade}}
    return student

def get_student_id(students: dict) -> int:
    return 10000 + len(students) + 1

# endregion

def crud(students: dict):
    while True:
        print("[1] Add student\n"
            "[2] Update Student age/grade\n"
            "[3] Search a student\n"
            "[4] Save students\n")

        choice: int = int(input("Input a number: "))

        if choice == 1:
            # get student raw data
            student_id = get_student_id(students)
            name = get_name()
            age = get_age()
            grade = get_grade()

            # add student to the dictionary
            student = format_raw_data(student_id, name, age, grade)
            add_student(students, student)

        elif choice == 2:
            student_id = int(input("Search Student ID to update its age and/or grade: "))

            if not student_id:
                print("Student ID not found. Please try again.")
                return
            
            update_student(students, student_id)

        elif choice == 3:
            student_id = int(input("Search a Student by their ID : "))
            search_student(students, student_id)
        else:
            print(f"Saved {len(students)} students' data")
            return

def main():
    students: Dict[str, Union[int, str, int, float]] = {}
    crud(students)

if __name__ == "__main__": 
    main()