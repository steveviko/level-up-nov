class Pets:
    
    dogs = []
    #initialize
    def __init__(self, dogs):
        self.dogs = dogs
       


class Dog:
    species = "mammals" 

    def __init__(self,name,age):        
        """Return a pet object whose property is """
        self.name = name
        self.age = age
        self.is_hungry = True

     # instance method
    def description(self):
        return "{} is {} ".format(self.name, self.age)
        
    def eat(self):
        self.is_hungry = False
        return "My dogs are not hungry"

class Larry(Dog):
    pass

class Tom(Dog):
    pass

class Fletcher(Dog):
    pass
# Instantiate the Pet object
dogs =[
Larry("Larry",9),
Tom("Tom", 6),
Fletcher("Fletcher", 7)
]
all_pets = Pets(dogs)
print("I have {} dogs.".format(len(all_pets.dogs)))
for dog in all_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))
# print("I have 3 dogs")
# print(Tom.description())
# print(Fletcher.description())
# print(Larry.description())

# if Tom.species and Larry.species and Fletcher.species == "mammals":
#     print("And they're all mammals, of course")

print("And they're all {}s, of course.".format(dog.species))
for dog in all_pets.dogs:
    if dog.is_hungry is None:
        
        print("My dogs are hungry.")
    else:
        print("My dogs are not hungry.")
# my_dogs=Dog.eat()
# print(my_dogs)


    



