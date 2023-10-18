class Bird:
    def __init__(self, name, species):
        self.name = name #mapping out the objects that are being passed through in args
        self.species = species

    def __str__(self): #allows us to format a string to print out in child class'
        return f"{self.name} {self.species}"
    
class Dodo(Bird):
    def __init__(self, name, species, breed):
        super().__init__(name, species) #super class is another way of bringing down the attributes from the parent class
        self.breed = breed
    
    def __str__(self):
        return f"{self.name}, {self.species}, {self.breed}"

class Owl(Bird):
    def __init__(self, name, species, breed):
        super().__init__(name, species) #super class is another way of bringing down the attributes from the parent class
        self.breed = breed
    
    def __str__(self):
        return f"{self.name} {self.species}, {self.breed}"
    
my_dodo = Dodo("Jeff", "Bird", "Dodo")

print(my_dodo)