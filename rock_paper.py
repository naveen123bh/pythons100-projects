import random

print("Winning rules of the game ROCK PAPER SCISSORS are:\n"
      + "Rock vs Paper -> Paper wins\n"
      + "Rock vs Scissors -> Rock wins\n"
      + "Paper vs Scissors -> Scissors wins\n")

while True:
    # ask user choice
    print("Enter your choice:\n 1 - Rock \n 2 - Paper \n 3 - Scissors \n 4 - Exit")
    choice = int(input("Enter your choice: "))

    # exit condition
    if choice == 4:
        print("Thanks for playing! Goodbye 👋")
        break

    # validate input
    while choice < 1 or choice > 4:
        print("Invalid input, try again...")
        choice = int(input("Enter your choice: "))

    # map number to name
    if choice == 1:
        choice_name = 'rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissors'

    print("User choice is:", choice_name)

    # computer makes a choice
    print("Computer is making choice...")
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissors'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, "vs", comp_choice_name)

    # determine winner
    if choice == comp_choice:
        result = "tie"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = "paper"
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = "rock"
    else:
        result = "scissors"

    # print result
    if result == "tie":
        print("It is a tie!")
    elif result == choice_name:
        print("🎉 User wins!")
    else:
        print("💻 Computer wins!")

    # ask to play again
    ans = input("Do you want to play again? (y/n): ")
    if ans.lower() == 'n':
        print("Thanks for playing! Goodbye 👋")
        break
