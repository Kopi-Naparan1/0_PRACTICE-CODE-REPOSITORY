
def assignment5():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def describe(self):
            print(f'Name: {self.name}')
            print(f'Age: {self.age}')

    class Teacher(Person):
        def __init__(self, name, age, subject):
            super().__init__(name, age)
            self.subject = subject

        def describe(self):
            print('=' * 30)
            print("TEACHER")
            print(f'Name: {self.name}')
            print(f'Age: {self.age}')
            print(f'Subject: {self.subject}')



    class Student(Person):
        def __init__(self, name, age, grade):
            super().__init__(name, age)
            self.grade = grade

        def describe(self):
            print('=' * 30)
            print('STUDENT')
            print(f'Name: {self.name}')
            print(f'Age: {self.age}')
            print(f'Grade: {self.grade}')


    teacher_1 = Teacher("Ana",21,"Math" )
    student_1 = Student("Kopi", 18, 10)
    student_2 = Student("Mina", 16, 9)

    teacher_1.describe()
    student_1.describe()
    student_2.describe()















def main():
    print('STARTING THE #2\n')

    assignment5()





if __name__ == "__main__":
    main()