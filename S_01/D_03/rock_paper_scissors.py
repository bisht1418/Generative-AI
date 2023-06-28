import random

choices = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0
draws = 0

while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ")
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        print("It's a draw!")
        draws += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

    print(f"Score: User - {user_wins}, Computer - {computer_wins}, Draws - {draws}")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "no":
        break
