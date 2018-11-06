class Pets:
    species = "mammals" 

    #initialize
    def __init__(self, name, age):
        """Return a pet object whose property is """
        self.name = name
        self.age = age
        
       
    # instance method
    def description(self):
        return "{} is {} ".format(self.name, self.age)

    


# Instantiate the Pet object
Larry =Pets("Larry",9)
Tom = Pets("Tom", 6)
Fletcher = Pets("Fletcher", 7)
print("I have 3 dogs")
print(Tom.description())
print(Fletcher.description())
print(Larry.description())

if Tom.species and Larry.species and Fletcher.species == "mammals":
    print("And they're all mammals, of course")

class Dog:

    def __init__(self):
        self.is_hungry = True


    def eat(self):
        self.is_hungry = False
        return "My dogs are not hungry"

my_dogs=Dog()
print(my_dogs.eat())


    



