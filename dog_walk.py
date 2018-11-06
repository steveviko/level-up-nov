class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())



class Dog:

    # Class attribute
    species = 'mammal'
    is_hungry = True

    # Initialize
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def description(self):
        return self.name, self.age

    
    
    def walk(self):
        return "%s is walking!" % (self.name)




# dogs instances 
my_dogs = [
    Dog("Tom", 6), 
    Dog("Fletcher", 7), 
    Dog("Larry", 9)
]

# Instantiate the Pet class
my_pets = Pets(my_dogs)

# Output
my_pets.walk()