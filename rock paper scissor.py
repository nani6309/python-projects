import random

options=("rock","paper","scissor")
running = True

while running:
    player = input("Enter a choice(rock, paper, scissor)")
    computer = random.choice(options)
    if player not in options:
        print("You were not selected any option....\n Please select atleast one option....")
    else:
        print(f"player:{player}")
        print(f"computer:{computer}")
        if player == computer:
            print("It's A Tie")
        elif player == "rock" and computer == "scissor":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissor" and computer == "paper":
            print ("You win!")
        else:
            print("Computer Win!")
        play_again=input("Do you want to play Again?(y/n)")
        if play_again == 'n' or play_again == 'N':
            running = False
print("Thanks for the game!.....\n visit again!......")
