math = int(input("Enter maths result: "))
while math <= 0 or math >= 100:
    print("Please enter valid result")
english = int(input("Enter English result: "))
while english <= 0 or english >= 100:
    print("Please enter valid result")
ICT = int(input("Enter ICT result: "))
while ICT <= 0 or ICT >= 100:
    print("Please enter valid result")

average = (math + english + ICT)/3

if average < 65:
    print(f"You have failed, your average score was {average}")

else:
    print(f"You have passed, your average score was {average}")

