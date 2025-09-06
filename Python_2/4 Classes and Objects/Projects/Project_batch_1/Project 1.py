# Make student report card system

class ReportCard:
    student_lists = []

    def __init__(self, name, *scores):
        self.name = name
        self.scores = list(scores)
        self.average = None
        ReportCard.student_lists.append(self)

    def calculate_average(self):
        if self.scores:
            self.average = sum(self.scores) / len(self.scores)
        else:
            self.average = 0.0
        return self.average


    def __str__(self):
        average_display = f"{self.average:.2f}" if self.average is not None else "N/A"
        return f"{self.name}: {average_display}"


student_1 = ReportCard("John",90, 89, 96, 94, 92)
student_2 = ReportCard("Rex",90, 93, 94, 91, 92)
student_3 = ReportCard("Kwexer",78, 93, 94, 91, 92)
student_4 = ReportCard("Troy",78, 93, 94, 95, 92)

to_grade = [student_1, student_2, student_3, student_4]

for grade in to_grade:
    grade.calculate_average()
    print(grade)







