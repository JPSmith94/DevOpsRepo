grade = int(input("Enter Exam Grade: "))
level = int(input("Input Exam Level: "))
if level == 1:
    if grade >= 71:
        print("Distinction")
    elif grade >= 61:
        print("Merit")
    elif grade >= 50:
        print("Pass")
    else:
        print("Fail")
if level == 2:
    if grade >= 66:
        print("Distinction")
    elif grade >= 51:
        print("Merit")
    elif grade >= 40:
        print("Pass")
    else:
        print("Fail")    