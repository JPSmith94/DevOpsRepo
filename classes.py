# classes is object orientated programming (oop)
# key concepts, class - a blueprint of attributes (variables, args) and methods (functions) that we can use against an object of a class
# object: this is an instance of a class
# methods - functions internal to a class
# nice way to organise work, only methods and objects inside the class can be called
# allows us to easily make multiple objects of the same type
# 

#class Dog: # make a class for dogs, then make an object for that class
#    energy = "high" # setting an attribute

#    def speak(self): # here we are creating a method(function)
#        print("Bark") 

#fido = Dog() # sets an object of the class called fido

#fido.energy = "Low" # setting new attribute value, not default

#print(fido.energy) # calling attribute value

#fido.speak() # calls out the method inside the class using the object 'fido'

# map students in a classroom

#class Student:
#    def __init__(self, first, last, age): #__ indicates a background task__ #self refers to the object we're passing through, will always be first in the initialisation. Object gets passed through the class
#        self.first = first # init maps the object to the custom args being passed through by the object
#        self.last = last # object.arg = arg(< defined by user ie... student1.first=jake)
#        self.age = age
#        
#    def fullname(self):
#        return(self.first + " " + self.last)

#student_1 = Student("Jake", "Smith", 29)

#print(st`udent_1.fullname())
#print(Student.fullname(student_1))`

#Change an attribute with a method

#class Student:
 #   def __init__(self, first, last, age): #__ indicates a background task__ #self refers to the object we're passing through, will always be first in the initialisation. Object gets passed through the class
   #     self.first = first # init maps the object to the custom args being passed through by the object
  #      self.last = last # object.arg = arg(< defined by user ie... student1.first=jake)
    #    self.age = age
        
    #def fullname(self):
     #   return(self.first + " " + self.last)
    
    #def change_age(self):
     #   self.age = int(self.age + 1)

#student_1 = Student("Jake", "Smith", 29)

#tudent_1.change_age()

#Self Class variables

#class Student:

    #age_increase_amount = 25

    #def __init__(self, first, last, age): #__ indicates a background task__ #self refers to the object we're passing through, will always be first in the initialisation. Object gets passed through the class
        #self.first = first # init maps the object to the custom args being passed through by the object
       # self.last = last # object.arg = arg(< defined by user ie... student1.first=jake)
      #  self.age = age
     #   
    #def fullname(self):
    #    return(self.first + " " + self.last)
   # 
  #  def change_age(self):
 #       self.age = int(self.age + self.age_increase_amount)

#student_1 = Student("Jake", "Smith", 29)
#print(student_1.age)
#student_1.change_age()
#print(student_1.age)

# __dict__

#print(student_1.__dict__)
#print(Student.__dict__)

#change the variable

#Student.age_increase_amount = 20

#print(Student.__dict__)

#student_1.age_increase_amount = 10
#student_1.change_age()
#print(student_1.__dict__)


#Additional variables (non self class variable) not being used by the object

#class Student:
    # the use determines what type of variable it is self is object variable, or class used is non self class
#    age_increase_amount = 25
#    number_of_students = 0

#    def __init__(self, first, last, age): #__ indicates a background task__ #self refers to the object we're passing through, will always be first in the initialisation. Object gets passed through the class
#        self.first = first # init maps the object to the custom args being passed through by the object
#        self.last = last # object.arg = arg(< defined by user ie... student1.first=jake)
#        self.age = age
#
#        Student.number_of_students += 1
#        
#    def fullname(self):
#        return(self.first + " " + self.last)
#    
#    def change_age(self):
#        self.age = int(self.age + self.age_increase_amount)

    
#print(Student.number_of_students)
#student_1 = Student("Jake", "Smith", 29)
#print(Student.number_of_students)


# parent/child classes, child can inherit attributes/methods from parent class
#parent class, dog, child class could be breed of dogs

# parent class

#class Animal:
#    def __init__(self, name, species):
 #       self.name = name #mapping out the objects that are being passed through in args
#        self.species = species

#    def eat(self):
 #       print(f"{self.name} is eating")

# child class
#class Cat(Animal):
#    def __init__(self, name, species, breed):
#        super().__init__(name, species) #super class is another way of bringing down the attributes from the parent class
#        self.breed = breed

#    def meow(self):
#        print("meow")

#my_cat = Cat("Mittens", "Cat", "Maine Coon")

#my_cat.eat()
#my_cat.meow()

#print(my_cat)

class Animal:
    def __init__(self, name, species):
        self.name = name #mapping out the objects that are being passed through in args
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def __str__(self): #allows us to format a string to print out in child class'
        return f"{self.name} {self.species}"
    
class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species) #super class is another way of bringing down the attributes from the parent class
        self.breed = breed

    def meow(self):
        print("meow")
    
    def __str__(self):
        return f"{self.name} {self.species}, {self.breed}"
    
my_cat = Cat("Mittens", "Cat", "Maine Coon")

print(my_cat)

# __ atribute is only accessible when calling with the class name
# access by _classname__attributename
#trailing_ its a way of using python keywords without using the keyword itself
#leading _ - indicates an attribute as private (bank details ect..) lock it down further with __

class Feline:
    __family = "Something"

cat3 = Feline()

print(cat3._Feline__family)