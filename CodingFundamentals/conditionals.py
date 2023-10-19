#if, elif, else, else statements. Flow control
#conditional statements used to accomodate different paths our code can follow

#my_bool = True

#if my_bool:
#    print("my Bool is true")
#else: 
#    print("My bool is not true")

#Conditionals:
# equals to: ==
# not equals to: !=
# less than: <
# more than: >
# less than or equals to: <= - >=

#money = 10

#if money >= 5: 
    
#    print("I have bare P")
#else:
#    print("I'm poor as fuck")

#elif limits the amount of if statements needed, basically elseif runs if the previous elif didn't run rather than if statements which will run all the time

#grade = int(input("What is your Grade: "))
#if grade > 85:
#    print("Distinction")
#elif grade >= 65:
#    print("Merit")
#elif grade >= 30:
#    print("Pass")
#else:
#    print("Fail")

#multiple compareters - with multiple conditions using and/or in/notin don't use and with not

#deposit = 98
#password = "Paassword"

#if 0 < deposit <= 100 and password == "Password":
#    print(f"Thank you for the deposit of £{deposit}")
#else:
#    print(f"Failed to deposit £{deposit}")

#if not (0 < deposit <= 100) or password != "Password":
#    print(f"Failed to deposit £{deposit}")
#else: 
#    print(f"Thanks for the deposit of £{deposit}")

#in is basically if it contains
#name = "root"
#if name not in ("root", "admin", "ca"):
#    print("Accepted")
#else:
#    print("Invalid User")