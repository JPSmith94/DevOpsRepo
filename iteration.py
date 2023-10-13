#iteration is another word for loops, repeating blocks of code
#saves time without having to write code multiple times
#2 types of loops, while loops and for loops
#while loops will continuously execute code whilst the condition is true

#x = 0
#while x <= 100:
#    print(x)
#    x += 1

#i= 1
#while i < 6:
#    if i == 3:
#        break
 #   print(i)
 #   i += 1

#j = 0
#while j < 6:
#    j += 1
#    if j == 3:
#        continue
#    print(j)

#while True:
#    name = input("Enter your name")
 #   if name == "Quit":
#        break
#    else:
 #       print(f"Hello {name}")

#for loops

#a for loop will iterate over any iterable collection (strings, dict, lists...)
#useful for when we want to use data from a collection
#Do things to individual items in a collection

#iterating through lists

#my_fruits = ["apple", "orange", "pear"]

#for fruits in my_fruits:
#    print(fruits)

# range

#for a in range(5):
 #   print(a)

#for a in range(1, 10, 5):
 #   print(a) #1-9 in steps of 5

#for letter in "hello":
 #   print(letter)
#
#for word in "hello world".split():
 #   print(word) #.split using space as individual strings

#list comprehension

#result = [x**2 for x in range(5)]

#print(result)

#dictionaries

#for i in {"drink": "wine"}:
#    print(i)

#for i in {"food": "Jam"}.values():
#    print(i)

#for i in {"shape": "Square"}.items():
#    print(i)

#break and continue

#for i in range(10):
#    if i == 5:
#        print("Mambo number 5")
#        continue
#    print(i)

#for i in range(1,3):
 #   for j in range(1,4):
#        print(i, "x", j, "=", i*j)

#a = 0
#while a < 5:
 #   name = input("What is your name ")
#    print(name, "How's it going")
#    a += 1

#name = input("enter your name ")
#list = ["Jake", "Adam", "Tony"]
#list.append(name)
#for name in list:
#    print(F"{name} is awesome")

for counter in range(5):
    name = input("enter name ")
    print(name + " is great")