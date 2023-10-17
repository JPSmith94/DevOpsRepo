import random

def playRound(num_of_rounds, computer_wins, user_wins):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    user_choise = input("Enter rock, paper or scissors: ").lower()
    print(f"You have chosen {user_choise}")
    if computer_choice == user_choise:
            print("ITS A DRAW!")
            return num_of_rounds + 1
    elif user_choise == "rock":
            if computer_choice == "scissors":
                   print(f"Computer chose {computer_choice} YOU WIN!")
                   return num_of_rounds + 1, user_wins + 1
            else:
                   computer_choice == "paper"
                   print(f"Computer chose {computer_choice} YOU LOSE")
                   return num_of_rounds + 1, computer_wins + 1
    elif user_choise == "paper":
            if computer_choice == "scissors":
                    print(f"Computer chose {computer_choice} YOU WIN!")
                    return num_of_rounds + 1, user_wins + 1
            else:
                    computer_choice == "rock"
                    print(f"Computer chose {computer_choice} YOU LOSE!")
                    return num_of_rounds + 1, computer_wins + 1
    elif user_choise == "scissors":
            if computer_choice == "paper":
                    print(f"Computer chose {computer_choice} YOU WIN!")
                    return num_of_rounds + 1, user_wins + 1
            else:
                    computer_choice == "rock"
                    print(f"Computer chose {computer_choice} YOU LOSE!")
                    return num_of_rounds + 1, computer_wins + 1

num_of_rounds = 0
computer_wins = 0
user_wins = 0

while True:
       playRound(num_of_rounds, computer_wins, user_wins)
       print(f"{num_of_rounds} number of rounds have been played")
       print(f"User has won {num_of_rounds} rounds")
       print(f"Computer has won {num_of_rounds} rounds")
       play_again = input("Would you like to play again? y/n: ")
       if play_again != "y":
              break
       

       
            


        



