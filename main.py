import random;
def get_choices():
    options = ["rock", "paper", "scissors"];
    player_choice = input("Enter a choice ('rock, paper, scissors'): ");
    computer_choice = random.choice(options);
    choices = { "player": player_choice, "computer": computer_choice};
    return choices;


def check_win(player, computer):
    print(f"you chose {player} and computer chose {computer}");
    if computer == player:
        return "It is a tie no winner"
    elif player == "rock":
        if computer == "paper":
            return "Rock is wrapped by the paper you loose!"
        else: 
            return "Rock smashes the scissors you win!"
    elif player == "paper":
        if computer == "rock":
            return "Paper wraps the rock you win!"
        else:
            return "Paper is being cut by the scissors you loose!"
    elif player == "scissors":
        if computer == "rock":
            return "Scissors is smashed by the rock you loose!"
        else:
            return "Scissor cut the paper you win!"

choices = get_choices()

result = check_win(choices["player"], choices["computer"])

print(result)