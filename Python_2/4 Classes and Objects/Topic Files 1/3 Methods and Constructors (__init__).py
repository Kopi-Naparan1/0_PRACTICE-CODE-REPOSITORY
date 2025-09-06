




def assignment4():
    class StudentRecord:

        def __init__(self, name, grade_level, average_score):
            self.name = name
            self.grade_level = grade_level
            self.average_score = average_score

        def rating_card(self):
            if self.average_score >= 75:
                print(f'{self.name}: [Passed]')
            else:
                print(f'{self.name}: [Failed]')

        def display_info(self):
            print('=' * 30)
            print(f"Name: [{self.name}] \n"
                  f"Grade Level: [{self.grade_level}] \n"
                  f"Average Score: [{self.average_score}]")
            self.rating_card()
            







    student1 = StudentRecord("Kopi1",10,90)
    student2 = StudentRecord("Kopi2", 10, 75)
    student3 = StudentRecord("Kopi3", 10, 70)

    student1.display_info()
    student2.display_info()
    student3.display_info()











def main():
    print('STARTING THE #2\n')

    assignment4()





if __name__ == "__main__":
    main()