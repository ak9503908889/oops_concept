# # # create a program for Rock paper scissors game
# # # rules : Rock wins against Scissors  0 for Rock
# #           paper wins against Rock     1 for paper
# #          Scissors wins against paper  2 for Scissors
#
# user choice   computer choice     # like that we compare and make logic or conditions.
#   0                  0
#   0                  1
#   0                  2
#
# user choice   computer choice
#   1                 0
#   1                  1
#   1                  2
# user choice   computer choice
#   2                 0
#   2                  1
#   2                   2

import random
user_choice=int(input("Enter your choice: type 0 for Rock, 1 for Paper,2 for Scissors: "))
if user_choice>=2 or user_choice<0:
    print("u have enter wrong input uou lose: ")
else:

    computer_choice = random.randint(0, 2)
    print("computer choose value: ")
    print(computer_choice)

    if computer_choice == user_choice:
        print(" its a Draw")

    elif computer_choice == 0 and user_choice == 2:
        print(" you lose")

    elif user_choice == 0 and computer_choice == 2:
        print(" you Win ")

    elif computer_choice > user_choice:
        print(" you are lose")

    elif user_choice > computer_choice:
        print(" you win")


