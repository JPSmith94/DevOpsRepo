number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))

print("1. Add +,", "2. Subtract -,", "3. Multiple *,", "4. Divide /,", "5. Square s" )

value = input("Select operation to perform(+,-,*,/,s)")

if value == ("+"):
    print(number1 + number2)
elif value == ("-"):
    print(number1 - number2)
elif value == ("*"):
    print(number1 * number2)
elif value == ("/"):
    print(number1 / number2)
elif value == ("s"):
    print(number1 ** number2)
else:
    print("Invalid operator")