

#def greet(name):
 #   print(f"hi {name}")
#
#greet("jake")

#def greet_1(first_name, second_name, age):
 #   print(f"{first_name} {second_name} is {age}")

#greet_1("Jake", "Smith", 29)

#better to use return as we can store the value in a variable
#avoid using print and inputs


#def greeter(name):
#    return(f"hello {name}")
#x = greeter("Jake")

#print(x)

# default arguments

#def greet3(name, age=10): #default args must come as last arguments
#    return(f"Hello {name}, you are {age}")
#xy = greet3("Jakey Pie", "29")
#print(xy)

#def addition(num1,num2):
#    return(f"Your sum is {num1 + num2}")
#add = addition(5,2)
#print(add)

# *args
#if we don't know how many arguments will be passed into the function we use *args
# add a * before the parameter name (basically a wildcard) 
# it recieve a tuple of arguments

#def fruit_list(*fruits):
#    print("the fruits are: ")
#    for fruit in fruits:
#        print(fruit)
#
#fruit_list("apple", "pear", "jackfruit","guava")

#def numbers_list(*numbers):
  #  for i in numbers:
 #       print(i)

#numbers_list(1,100)

#keyword arguments kwargs
#send args as key:value pairs - therefore the order does not matter
#we define the value when we pass the arguments

#def fruit_list(fruit1, fruit2, fruit3):
#    print(f"fav = {fruit1}")
#    print(f"fav2 = {fruit2}")
#    print(f"fav3 = {fruit3}")

#fruit_list(fruit1 = "apple", fruit3 = "guarva", fruit2 = "pear")

# ** kwargs
# if we don't know how many kwargs there will be

#def fav_food(**food):
 #   print("Fav food is", food["fruit"], "not", food["dinner"])

#fav_food(dessert = "ice-cream", fruit = "Apple", dinner = "Pizza")

# passing a list as an arg

#def my_function(food):
 #   for x in food:
  #      print(x)
#
#list1 = ["apple", "pear", "banana", "orange", "eggplant", "guarva"]

#my_function(list1)

# format example

name = "josh"
age = 20
height = 1.7

#print("my name is {}, i am {}, my height is {} metres".format(name, age, height))

x = "my name is {}, i am {}, my height is {} metres"

print(x.format(name, age, height))