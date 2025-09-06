
class Dog:
    dog_count = 0  # This is the Class Variable - Can be shared with everyone

    def __init__(self, name, breed):
        self.name = name # These are the instance variables
        self.breed = breed
        Dog.dog_count += 1

    def __str__(self):
        return f'Name: {self.name} Breed: {self.breed}'


dog1 = Dog("Scooby", "Aspin")
dog2 = Dog('Honey', "Golden Retriever")
dog3 = Dog("Rocky", 'Pitbull')

dogs = [dog1, dog2, dog3]

for dog in dogs:
    print(dog)

print(f'Dog count: {Dog.dog_count}')
