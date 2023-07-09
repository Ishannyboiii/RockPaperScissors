import random

round_count = input("How many rounds would you like to play? ")
score = 0

for i in range(int(round_count)):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    player_choice = input("Rock, Paper, Scissors? ").lower()

    if computer_choice == player_choice:
        print("Tie")
    else:
        if computer_choice == "paper" and player_choice == "scissors":
            print("Scissors beats paper. You win!")
            score += 1
        if computer_choice == "scissors" and player_choice == "paper":
            print("Scissors beats paper. You lost.")
        if computer_choice == "rock" and player_choice == "scissors":
            print("Rock beats scissors. You lost.")
        if computer_choice == "scissors" and player_choice == "rock":
            print("Rock beats scissors. You win!")
            score += 1
        if computer_choice == "paper" and player_choice == "rock":
            print("Paper beats rock. You lost.")
        if computer_choice == "rock" and player_choice == "paper":
            print("Paper beats rock. You win!")
            score += 1


print(f"Your score is {score}/{round_count}")
