grade = int(input("Enter Exam Grade: "))

if grade >= 71:
    print("Distinction")
elif grade >= 61:
    print("Merit")
elif grade >= 50:
    print("Pass")
else:
    print("Fail")