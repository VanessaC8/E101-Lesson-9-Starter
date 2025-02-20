from random import randrange

choices = ["Rock","Paper","Scissors"]


def play_game(player_choice, computer_choice):

    if computer_choice == player_choice:
      return "It's a tie!"
    elif computer_choice == "Rock":
      if player_choice == "Paper":
        return "You win!"
      else:
       return "You lose!"
    elif computer_choice == "Paper":
      if player_choice == "Rock":
        return "You lose!"
      else:
        return "You win!"
    elif computer_choice == "Scissors":
      if player_choice == "Rock":
        return "You win!"
      else:
        return "You lose!"

def main():
  play_again="yes"
  while play_again=="yes":
    player_choice = input("Choose: Rock, Paper, or Scissors: ").capitalize()
    computer_choice = choices[randrange(3)]
    print("The computer chose: " + computer_choice)
    print("You chose: " + player_choice)
    #print(play_game(player_choice, computer_choice))
    session= play_game(player_choice, computer_choice)
    print(session)
    print("\n\n---------------------------\n")
    play_again = input("Do you want to play again?: ").lower()

  print("Thank you for Playing!")

if __name__ =="__main__":
  main()
