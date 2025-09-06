

def assignment_9(): # str
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def __str__(self):
            return f"{self.name} is a {self.position}"


    employee1 = Employee("Kopi", "Manager")
    print(employee1)

def assignment_10(): # repr

    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def __repr__(self):
            return (f'Employee: {self.name}\n'
                    f'Position: {self.position}')

    employee2 = Employee('Kopi', "CEO")
    print(repr(employee2))

def assignment_11(): #add
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def __add__(self, other):
            return f'{self.position} and {other.position} are combined'

    employee1 = Employee("Kopi", "CEO")
    employee2 = Employee("Ana", "Secretary")

    print(employee1 + employee2)

def assignment_12(): #eq
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def __eq__(self, other):
            return self.position == other.position

    employee1 = Employee("Kopi", "CEO")
    employee2 = Employee("Ana", "Secretary")

    print(employee1 == employee2)

def assignment_13(): #call
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def __call__(self, *args, **kwargs):
            print(f"{self.name} is working on his/her role: {self.position}")

    employee3 = Employee("Kopi", "CEO")
    employee3()

def assignment_14(): #len
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def __len__(self):
            return len(self.name) + len(self.position)

    employee4 = Employee("Kopi", "CEO")
    print(len(employee4))

def assignment_15():
    class OfficeDay:
        def __enter__(self):
            print('---Welcome Slave---')
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('--- Good bye Slave---')

            if exc_type:
                print(f'ERROR: {exc_type.__name__} --- {exc_val}')


        def query(self):
            print('Fall-in line Slaves')

    with OfficeDay() as od:
        od.query()




def project1():
    class Freelancer:
        def __init__(self, name, skill, rating, task=None):
            self.name = name
            self.skill = skill
            self.rating = rating
            self.task = task or []

        def __str__(self):

            x =  (f'Name: {self.name}\n'
                  f'Skill: {self.skill}\n'
                  f'Rating: {self.rating}\n'
                  f'Task/s: {self.task}')
            return x

        def __add__(self, other):

            return f'{self.name} and {other.name} are collaborating'

        def __eq__(self, other):

            return  self.rating == other.rating

        def __call__(self, todo):

            self.task.append(todo)
            print(f"{self.name} accepted task: {todo}")




    class MarketPlace:
        def __enter__(self):
            print(f"\n{'-' * 30}")
            print("Logging-In")
            print(f"{'-' * 30}\n")
            return  self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print(f"\n{'-' * 30}")
            print('Logging-Out')
            print(f"{'-' * 30}\n")

        def display(self, freelancer):
            print('.' * 30)
            print(f'Your freelancer: {freelancer}')
            print('.' * 30)

        def collab(self,collab):
            print('.' * 30)
            print(f'Collaboration:\n\t\t {collab}')
            print('.' * 30)

        def rating(self, both):
            print('.' * 30)
            print(f'Rating Matching: {both} ')
            print('.' * 30)

        def calling(self, todo):
            print('.' * 30)
            print(f'Tasks: {todo} ')
            print('.' * 30)


    with MarketPlace() as market:

        # Making of Freelancers
        freelancer1 = Freelancer("Kopi", "Programming", 9, )
        freelancer2 = Freelancer("Jane", "Graphic Artist", 8, )

        freelancers = [freelancer1, freelancer2]

        # Displaying freelancers Info
        for freelancer in freelancers:
            market.display(freelancer)

        # Collaborating
        collab1 = freelancer1 + freelancer2
        market.collab(collab1)

        # Rating
        rating1 = freelancer1 == freelancer2
        market.rating(rating1)

        #call
        freelancer1("Make website")
        freelancer2('Make a 3d bear')



















def main():
    print("=" * 30)
    print('STARTING THE #8 Magic Methods')
    print("=" * 30)
    print('\n' * 5)


    # assignment_9()
    # assignment_10()
    # assignment_11()
    # assignment_12()
    # assignment_13()
    # assignment_14()
    # assignment_15()
    project1()


if __name__ == "__main__":
    main()