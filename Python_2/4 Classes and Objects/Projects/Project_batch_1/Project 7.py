from abc import ABC, abstractmethod

# region Making Person Class


class Person(ABC):

    @abstractmethod
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Patient(Person):
    def __init__(self, name, age, issue):
        super().__init__(name, age)
        self.issue = issue


class Doctor(Person):
    def __init__(self, name, age, years_experience):
        super().__init__(name, age)
        self.years_experience = years_experience

# endregion


# region System Class


class PatientManagementSystem(ABC):

    @abstractmethod
    def appointment(self, patient, doctor):
        pass


class Appointment(PatientManagementSystem):
    def __init__(self, date):
        self.date = date

    def appointment(self, patient, doctor):
        return (f'--- {self.date} --- \n'
                f'Patient: {patient.name} {patient.age} years old - Issue: {patient.issue} \n'
                f'Doctor: {doctor.name} {doctor.age} years old - {doctor.years_experience} years of experience \n')


# endregion


# region making people
# Making Patients
patient_1 = Patient("Kopi", 18, "Cancer")
patient_2 = Patient("Anan", 19, "Monkey Pox")
patient_3 = Patient("Naparan", 20, "Covid 2025")


# Making Doctors
doctor_1 = Doctor("Leo", 45, 10)
doctor_2 = Doctor("McRey", 46, 15)
doctor_3 = Doctor("Pasco", 47, 20)

# endregion


# region Making Appointment

appointment_1 = Appointment("May 31").appointment(patient_1, doctor_1)
appointment_2 = Appointment("July 31").appointment(patient_2, doctor_2)
appointment_3 = Appointment("August 31").appointment(patient_3, doctor_3)

appointments = [appointment_1, appointment_2, appointment_3]

for appointment in appointments:
    print(appointment)
# endregion

