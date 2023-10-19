#modules 
#modules are just files we import to extend our functionality
#we can import modules or make our own
#many modules are built in and don't need setup
#some need to be installed with pip. brew for mac

#import math # importing the entire module

#number = 10

#answer = math.sqrt(number) #syntax for referencing an object from a module

#print(answer)

#import math
#import random

#def random_pi():
#    return math.ceil(random.randint(1,10) * math.pi)

#for i in range(5):
 #   print(random_pi())


#from math import pi, ceil, floor
#from random import randint #saves memory not importing the entire module, increases the performance

#def random_pi():
#    return floor(randint(1,10) * pi)

#for i in range(5):
#    print(random_pi())

#create 2 files, called dice.py - write a function that simulates a dice roll (number between 1 and 6)
#2nd file use the dice module to simulate throwing 2 dice and print out

#files

#read, write and edit files
#most file types will work however some may need an imported module

#file = open("filename.txt", "mode") # pass arg with filename and format, and the mode we want to open it in (r, read only. w, write. r+, read and write. a, append)

#file.close() #need to remember to close the file once opened ^, most recently open file will close

#to read a file
#open file use readline() - reads a line and moves onto next
#readlines()/read() reads all lines
#seek() - useful for making sure you are reading from beginning or from a specific line seek(0) <- places at start

file = open("teams.txt", "w")

outfile = ["vikings", "bills", "Jaguars", "dolphins", "chiefs" ]

for i in outfile:
    newline = i + "\n"
    file.write(newline)

file.close()

file = open("teams.txt", "r")

lines = file.readlines()
file.close()
lines[0] = "this is a new line"
file = open("teams.txt", "w")
for i in range(len(lines)):
    if i == len(lines)-1:
        file.write(lines[i])
    else:
        file.write(lines[i].strip() + "\n")

file.close()

file= open("teams.txt", "r")

print(file.readlines())