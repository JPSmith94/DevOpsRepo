class Student:
    average = 0
    def __init__(self, first, last, age, class_, test1, test2, test3):
        self.first = first 
        self.last = last 
        self.age = age
        self.class_ = class_
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        
        
    def fullname(self):
        return(self.first + " " + self.last)
    def averagetest(self):
       Student.average = int(self.test1 + self.test2 + self.test3) // 3

    if average <= 65:
        print("You thick as shit")
    else:
        print("You ite")

student_1 = Student("Jake", "Smith", 29, "Chemisty", 31, 44, 55)
student_2 = Student("Adam", "Groves", 30, "Physics", 70, 89, 99)
student_2.averagetest()
print(student_2.average)