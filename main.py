# main.py
# HamzaKhairy/python-tic-tac-toe
# Start: 21-Dec-20
# This program is a text-based tic-tac-toe game.

GameNumber = 1
PlayAgain = True
Player1Score, Player2Score, GameCount = 0, 0, 0
Board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]


def display_board():
            print(Board[0] + " | " + Board[1] + " | " + Board[2], "\n", "-------")
            print(Board[3] + " | " + Board[4] + " | " + Board[5], "\n", "-------")
            print(Board[6] + " | " + Board[7] + " | " + Board[8])


def display_scoreboard():
    print("Game Number:", GameNumber)
    print("------------------------- \n    ~ Scoreboard ~")
    print("|", Player1, ":", Player1Score, "||", Player2, ":", Player2Score, "| \nGames Played:", GameCount, "\n------")


print("\n ~~ Welcome to Hamza's tic-tac-toe. Have fun! ~~ \n")
Player1 = input("Enter Player 1's name: ")
Player2 = input("\n*Type 'pc' to play against the computer* \nEnter Player 2's name: ")



