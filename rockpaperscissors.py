from random import choice

computer_choices = ["Rock", "Paper", "Scissors"]
computer_move = choice(computer_choices)
win_statement = "I win! Yay!"
lose_statement = "Rats! You beat me!"
tie_statement = "Looks like we picked the same move. No winner this time, I guess."

print ("This program is a text-based simulation of the classic game rock, paper, scissor. The player will input their selection, and the computer will resond with its move. I promise not to cheat!")

endPrgm = False
while (not endPrgm):
    difficulty = raw_input ("Would you like to play on Hard mode, or Easy mode? Please type your selection: ")

    if difficulty.lower() == "hard":
        endGame = False
        while (not endGame):
            player_move = raw_input ("Will you play Rock, Paper, or Scissors? Please type your selection: ")
            if player_move.lower() == "rock":
                print ("I choose Paper")
                print win_statement
                endGame = True
            elif player_move.lower() == "paper":
                print ("I choose Scissors")
                print win_statement
                endGame = True
            elif player_move.lower() == "scissors":
                print ("I choose Rock")
                print win_statement
                endGame = True
            else:
                print ("Please enter a valid move ")
        play_again = raw_input ('Would you like to play again? Please enter "Yes" or "No" ')
        if play_again.lower() == "yes":
            endPrgm = False
        elif play_again.lower() == "no":
            endPrgm = True
    elif difficulty.lower() == "easy":
        endGame = False
        while (not endGame):
            player_move = raw_input ("Will you play Rock, Paper, or Scissors? Please type your selection: ")
            if player_move.lower() == "rock":
                print ("I choose " + computer_move)
                if computer_move.lower() == "rock":
                    print tie_statement
                elif computer_move.lower() == "scissors":
                    print lose_statement
                else:
                    print win_statement
                endGame = True
            elif player_move.lower() == "paper":
                print ("I choose " + computer_move)
                if computer_move.lower() == "paper":
                    print tie_statement
                elif computer_move.lower() == "rock":
                    print lose_statement
                else:
                    print win_statement
                endGame = True
            elif player_move.lower() == "scissors":
                print ("I choose " + computer_move)
                if computer_move.lower() == "scissors":
                    print tie_statement
                elif computer_move.lower() == "paper":
                    print lose_statement
                else:
                    print win_statement
                endGame = True
            else:
                print ("Please enter a valid move ")
        play_again = raw_input ('Would you like to play again? Please enter "Yes" or "No" ')
        if play_again.lower() == "yes":
            endPrgm = False
        elif play_again.lower() == "no":
            endPrgm = True
    else:
        print ("Please select a valid difficulty ")

input ("Press any key to exit the program")
