from random import randrange
play_again = "yes"
choices = ["Rock","Paper","Scissors"]


while play_again=='yes':
    player_choice = input("Choose: Rock, Paper, or Scissors: ").capitalize()
    computer_choice = choices[randrange(3)]

    print("The computer chose: " + computer_choice)
    print("You chose: " + player_choice)

    if computer_choice == player_choice:
      print("It's a tie!")
    elif computer_choice == "Rock":
      if player_choice == "Paper":
        print("You win!")
      else:
        print("You lose!")
    elif computer_choice == "Paper":
      if player_choice == "Rock":
        print ("You lose!")
      else:
        print ("You win!")
    elif computer_choice == "Scissors":
      if player_choice == "Rock":
        print("You win!")
      else:
        print("You lose!")

    print("\n\n---------------------------\n")
    play_again = input("Do you want to play again?: ").lower()

print("Thank you for Playing!")
