investment = int(input("Enter initial investment: "))
target_value = int(input("Enter target value: "))
Years = 0
interest_rate = 0.1
while investment < target_value:
    investment *= (1 + interest_rate)
    Years += 1
print(f"It will take {Years} years to save £{target_value} with an interest rate of 10%")
