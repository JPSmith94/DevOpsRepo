shakes = {"1, Chocolate": 4, "2, Strawberry":3, "3, Banana":3, "4, Vanilla":20}
budget = int(input("Enter your budget: "))


for milk in shakes:
    print(milk)

    sam_shake = int(input("Which Shake do you want: "))

    if sam_shake == 1:
        print(f"Here is your chocolate milkshake")
        budget -= shakes[1]
#    elif sam_shake == 2:
 #       budget -= shakes[2]
 #   elif sam_shake == 3:
 #       budget -= shakes[3]
 #   elif sam_shake == 4:
 #       budget -= shakes[4]
    elif budget < 2:
        print("Please Leave")
    else:
        break
    
                        

    