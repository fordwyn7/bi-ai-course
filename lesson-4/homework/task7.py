import random

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "player"
    else:
        return "computer"

player_score = 0
computer_score = 0

while player_score < 5 and computer_score < 5:
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.\n")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    winner = get_winner(player_choice, computer_choice)

    if winner == "player":
        print("You win this round!\n")
        player_score += 1
    elif winner == "computer":
        print("Computer wins this round!\n")
        computer_score += 1
    else:
        print("It's a draw!\n")

    print(f"Score: You {player_score} - {computer_score} Computer\n")

if player_score == 5:
    print("🎉 Congratulations! You won the match!")
else:
    print("😞 Computer won the match. Better luck next time!")
