class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def __str__(self):
        return f"Make is{self.make}, model is {self.model}, year of manufactur is {self.year}"
    
car = Car("Honda", "Civic", 2018)

print(car.get_make())
car.set_make("Ford")
car.set_model("Mustang")
car.set_year(2020)
print(car.get_make(), car.get_model(), car.get_year())