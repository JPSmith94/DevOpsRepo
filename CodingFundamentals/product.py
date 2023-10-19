class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def totalvalue(self):
        return self.price * self.quantity
    
    def addstock(self, quantity):
        self.quantity += quantity

    def removeitem(self, quantity):
        if quantity > self.quantity:
            print("insufficent quantity")
        else:
            self.quantity -= quantity

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"
    
prod = Product("Fish Fingers", 10, 5)

print(prod.totalvalue())
prod.addstock(5)
print(prod.quantity)
prod.removeitem(9)
print(prod.quantity)
