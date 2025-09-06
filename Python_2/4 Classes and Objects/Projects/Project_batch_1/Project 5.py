

class Animal:

    def feed_animal(self):
        pass

    def check_health(self):
        pass

    def display_animal_info(self):
        pass


class Lion(Animal):
    def __init__(self, food, health):
        self.food = food
        self.health = health

    def feed_animal(self):
        return f'Fed the Lion: {self.food}'

    def check_health(self):
        return f'{self.health}'

    def display_animal_info(self):
        info = """
        Name: Lion
        Life-span: 34 years
        Number of Species: 30
        """

        return info


class Tiger(Animal):
    def __init__(self, food, health):
        self.food = food
        self.health = health

    def feed_animal(self):
        return f'Fed the Tiger: {self.food}'

    def check_health(self):
        return f'{self.health}'

    def display_animal_info(self):
        info = """
        Name: Tiger
        Life-span: 10 years
        Number of Species: 220
        """

        return info


class Zebra(Animal):
    def __init__(self, food, health):
        self.food = food
        self.health = health

    def feed_animal(self):
        return f'Fed the Zebra: {self.food}'

    def check_health(self):
        return f'{self.health}'

    def display_animal_info(self):
        info = """
        Name: Zebra
        Life-span: 20 years
        Number of Species: 13
        """

        return info


class Eagle(Animal):
    def __init__(self, food, health):
        self.food = food
        self.health = health

    def feed_animal(self):
        return f'Fed the Eagle: {self.food}'

    def check_health(self):
        return f'{self.health}'

    def display_animal_info(self):
        info = """
        Name: Eagle
        Life-span: 30 years
        Number of Species: 242
        """

        return info


class Elephant(Animal):
    def __init__(self, food, health):
        self.food = food
        self.health = health

    def feed_animal(self):
        return f'Fed the Elephant: {self.food}'

    def check_health(self):
        return f'{self.health}'

    def display_animal_info(self):
        info = """
        Name: Elephant
        Life-span: 40 years
        Number of Species: 53
        """

        return info


def print_animal_info(animal):
    print(f'{animal.display_animal_info()}')


def print_animal_feeding(animal):
    print(f'{animal.feed_animal()}')


def print_animal_health(animal):
    print(f'{animal.check_health()}')


print_animal_info(Lion("Limb", 'Bad'))
print_animal_feeding(Tiger('limb', 'Good'))
print_animal_health(Zebra("Grass", 'Bad'))
print_animal_info(Eagle("piece of chicken", 'Excellent'))
print_animal_feeding(Elephant('Water Melon', 'Good'))