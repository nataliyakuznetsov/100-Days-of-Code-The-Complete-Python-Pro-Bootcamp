import random
from rock_paper_scissors_art import rock, paper, scissors

# creating the list of pictures
list_pictures = [rock, paper, scissors]

# receiving a user's choice and printing the picture
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# control flow and printing the picture
if user_choice >= 0 and user_choice <=2:
    print(list_pictures[user_choice])

    # receiving the random computer's choice and printing the result
    comp_choice = random.randint(0, 2)
    print("Computer choice: ")
    print(list_pictures[comp_choice])

    # conditions when the player wins
    if (user_choice - comp_choice == 1) or (user_choice - comp_choice == -2):
        print("You Win!")
    # conditions when the computer wins
    elif (comp_choice - user_choice == 1) or (comp_choice - user_choice == -2):
        print("You lose!")
    # computer's choice is equal to user's choice
    elif comp_choice == user_choice:
        print("It's a draw")

else:
    # if a number is out of range
    print("You typed an invalid number, you lose!")
