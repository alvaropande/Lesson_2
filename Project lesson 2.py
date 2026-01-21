import random
options = ["Rock", "Paper", "Scissors"]
player_choise = input("Choose Rock, Paper, Scissors:")
computer_choise = random.choice(options)
print(f"You chose {player_choise}")
print(f"The computer chose {computer_choise}")
if player_choise == computer_choise:
    print("Its a tie!")
elif player_choise == "Rock" and computer_choise == "Scissors":
    print("You win!")
elif player_choise == "Paper" and computer_choise == "Rock":
    print("You win!")
elif player_choise == "Scissors" and computer_choise == "Paper":
    print("You win!")
else:
    print("You lose!")


