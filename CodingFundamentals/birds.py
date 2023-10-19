class Bird:
    def __init__(self, name, species):
        self.name = name 
        self.species = species

    def __str__(self): 
        return f"{self.name} {self.species}"
    
class Dodo(Bird):
    def __init__(self, name, species, breed):
        super().__init__(name, species) 
        self.breed = breed
    
    def __str__(self):
        return f"{self.name}, {self.species}, {self.breed}"

class Owl(Bird):
    def __init__(self, name, species, breed):
        super().__init__(name, species) 
        self.breed = breed
    
    def __str__(self):
        return f"{self.name} {self.species}, {self.breed}"
    
my_dodo = Dodo("Jeff", "Bird", "Dodo")

print(my_dodo)