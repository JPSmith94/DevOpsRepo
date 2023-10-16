min_value = 10
max_value = 50
attempts = 0
while attempts < 3: 
    user_value = int(input("Enter a value"))
    if min_value <= user_value <= max_value:
       print("Value correct")
       break
    else: attempts += 1