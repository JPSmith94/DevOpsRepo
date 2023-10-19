print("Pythagoras' Calculator")
print("1. Find the length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")
length = int(input("Enter 1, 2 or 3"))
if length == 1:
   B = int(input("Enter length of B: "))
   C = int(input("Enter length of C: "))
   print(f"Length of A is {B**C}")
elif length == 2:
    A = int(input("Enter length of A: "))
    C = int(input("Enter length of C: "))
    print(f"Length of A is {A**C}")
elif length == 3:
    A = int(input("Enter length of A: "))
    B = int(input("Enter length of B: "))
    print(f"Length of A is {A**B}")
else:
    print("Invalid input")