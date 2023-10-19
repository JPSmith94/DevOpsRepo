def getincometax(income):
    if income < 11850:
        print("You don't pay income tax")
    elif income < 34500:
        tax = round(income * 0.2, 2)
        print(f"You pay £{tax - 11850} in income tax")
    elif income < 150000:
        tax = round(income * 0.4, 2)
        print(f"You pay £{tax - 11850} in income tax")
    else:
        tax = round(income * 0.45, 2)
        print(f"You pay £{tax - 11850} in income tax")

x = int(input("Enter your income: "))
getincometax(x)

def getincometax2(salary):
    if salary < 11850:
        return 0
    elif 11850 <= salary <= 34500:
        return (salary - 11850) * 0.2
    elif 34501 <= salary <= 150000:
        return 4530 + ((salary - 334500) * 0.4)
    else: 
        return 50370 + ((salary - 150000) * 0.45)
    
salary = 200000
tax_amount = getincometax2(salary)
print("Tax amount you will pay on £{} is £{}".format(salary, tax_amount))