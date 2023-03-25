import random

def is_valid_play(play):
    return play in ["rock", "scissors", "paper"]

def computer_play():
    return random.choice(["rock", "scissors", "paper"])

def determine_game_result(human, computer):
    if human == computer:
        return "tie"
    elif human == "rock":
        if computer == "paper":
            return "computer"
        else:
            return "human"
    elif human == "scissors":
        if computer == "paper":
            return "human"
        else:
            return "computer"
    else:
        if computer == "rock":
            return "human"
        else:
            return "computer"

def main():
    human = input('rock, paper or scissors? ')

    while not is_valid_play(human):
        human = input('rock, paper or scissors? ')

    computer = computer_play()

    print(computer)

    result = determine_game_result(human, computer)

    if result == "tie":
        print("it's a tie")
    elif result == "computer":
        print("You loose")
    else:
        print ("You win")

if __name__ == "__main__":
    main()


