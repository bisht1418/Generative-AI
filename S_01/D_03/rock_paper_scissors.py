import random
import tkinter as tk

choices = ["rock", "paper", "scissors", "lizard", "spock"]
user_wins = 0
computer_wins = 0
draws = 0

def load_scores():
    global user_wins, computer_wins, draws
    try:
        with open("scores.txt", "r") as file:
            scores = file.readline().split(",")
            user_wins = int(scores[0])
            computer_wins = int(scores[1])
            draws = int(scores[2])
    except FileNotFoundError:
        pass

def save_scores():
    with open("scores.txt", "w") as file:
        file.write(f"{user_wins},{computer_wins},{draws}")

def play_game(user_choice):
    global user_wins, computer_wins, draws

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result_label.config(text="It's a draw!")
        draws += 1
    elif (
        (user_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard"))
        or (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard"))
        or (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock"))
        or (user_choice == "lizard" and (computer_choice == "paper" or computer_choice == "spock"))
        or (user_choice == "spock" and (computer_choice == "rock" or computer_choice == "scissors"))
    ):
        result_label.config(text="You win!")
        user_wins += 1
    else:
        result_label.config(text="Computer wins!")
        computer_wins += 1

    score_label.config(text=f"Score: User - {user_wins}, Computer - {computer_wins}, Draws - {draws}")

    save_scores()

def quit_game():
    window.destroy()

def load_scores():
    global user_wins, computer_wins, draws
    try:
        with open("scores.txt", "r") as file:
            scores = file.readline().split(",")
            if len(scores) == 3:
                user_wins = int(scores[0])
                computer_wins = int(scores[1])
                draws = int(scores[2])
    except (FileNotFoundError, ValueError):
        pass


window = tk.Tk()
window.title("Rock Paper Scissors Game")

choices_frame = tk.Frame(window)
choices_frame.pack(pady=10)

for choice in choices:
    button = tk.Button(choices_frame, text=choice.capitalize(), width=10, command=lambda c=choice: play_game(c))
    button.pack(side="left", padx=5)

result_label = tk.Label(window, text="Choose an option...")
result_label.pack(pady=10)

score_label = tk.Label(window, text=f"Score: User - {user_wins}, Computer - {computer_wins}, Draws - {draws}")
score_label.pack(pady=10)

quit_button = tk.Button(window, text="Quit", width=10, command=quit_game)
quit_button.pack(pady=10)

window.mainloop()
