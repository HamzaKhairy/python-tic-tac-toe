# main.py
# HamzaKhairy/python-tic-tac-toe
# Start: 21-Dec-20
# This program is a simple text-based tic-tac-toe game.

import random

CurrentPlayer = "X"
AgainChoice = " "
Player1, Player2 = "X", "O"
GamesPlayed, position = 0, 0
Player1Score, Player2Score, TieGames = 0, 0, 0
PlayAgain, Valid = True, True
GameEnd = False
Board = ["", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
Phrases = ["Nice move!", "Smart", "Good job", "Nice!", "good move"]


def intro():
    global Player1, Player2
    print("\n ~~ Welcome to Hamza's tic-tac-toe. Have fun! ~~ \n")

    print("The grid is organized as shown below, you will enter the respective number to make a move. \n")

    print("1 | 2 | 3\n--+---+--")
    print("4 | 5 | 6\n--+---+--")
    print("7 | 8 | 9\n")

    Player1 = input("Enter Player 1's name (X): ")
    Player2 = input("\n* Type 'pc' for single player * \nEnter Player 2's name (O): ")
    print("\nThe first game starts now, good luck!\n")


def display_board():
    print(Board[1] + " | " + Board[2] + " | " + Board[3] + "\n--+---+--")
    print(Board[4] + " | " + Board[5] + " | " + Board[6] + "\n--+---+--")
    print(Board[7] + " | " + Board[8] + " | " + Board[9] + "\n")


def turn():
    global CurrentPlayer, position
    position = input(CurrentPlayer + "'s turn: ")
    position = int(position)
    while (position > 9) or (position < 1):
        position = int(input("Invalid! Please input an integer from 1 to 9: "))
    while Board[position] != "*":
        position = int(input("Occupied! Please select an empty position: "))
    check_game_status()
    Board[position] = CurrentPlayer
    print("\n")
    display_board()
    print(Phrases[random.randint(0, 4)], "\n")


def check_game_status():
    global GameEnd, TieGames
    # Checking for a horizontal win
    if ("*" != Board[1] == Board[2] == Board[3]) or ("*" != Board[4] == Board[5] == Board[6]) or ("*" != Board[7] == Board[8] == Board[9]):
        print(CurrentPlayer, "has made a horizontal win. Congratulations!")
        update_score()
    # Checking for a vertical win
    elif ("*" != Board[1] == Board[4] == Board[7]) or ("*" != Board[2] == Board[5] == Board[8]) or ("*" != Board[3] == Board[6] == Board[9]):
        print(CurrentPlayer, "has made a vertical win. Congratulations!")
        update_score()
    # Checking for a diagonal win
    elif ("*" != Board[1] == Board[5] == Board[9]) or ("*" != Board[7] == Board[5] == Board[3]):
        print(CurrentPlayer, " has made a diagonal win. Congratulations!")
        update_score()
    elif "*" not in Board:
        print("     It's a tie!")
        TieGames += 1
        GameEnd = True


def turn_flip():
    global CurrentPlayer
    if CurrentPlayer == "X":
        CurrentPlayer = "O"
    else:
        CurrentPlayer = "X"


def display_scoreboard():
    global GamesPlayed
    GamesPlayed = Player1Score + Player2Score + TieGames
    print("------------------------- \n    ~ Scoreboard ~")
    print("|", Player1, ":", Player1Score, "||", Player2, ":", Player2Score, "|")
    print("Games Played:", GamesPlayed, "| \n Tied Games:", TieGames, "\n------")


def update_score():
    global GameEnd
    global Player1Score, Player2Score
    if CurrentPlayer == "X":
        Player1Score += 1
    elif CurrentPlayer == "O":
        Player2Score += 1
    GameEnd = True


def play_again():
    global PlayAgain, Board, GameEnd, AgainChoice
    Board = ["", "*", "*", "*", "*", "*", "*", "*", "*", "*"]

    AgainChoice = input("Do you want to play again? (Y/N): ")

    while (AgainChoice != "N") or (AgainChoice != "Y"):
        AgainChoice = input("Please input ('Y' or 'N'): ")

    if AgainChoice == "N":
        PlayAgain = False
        print("\nThank you for playing, I hope you enjoyed :)")
    if AgainChoice == "Y":
        PlayAgain = True
        GameEnd = False
        print("Another game is starting, good luck!\n------------------")


intro()
while PlayAgain:
    display_board()
    while not GameEnd:
        turn()
        check_game_status()
        turn_flip()
    display_scoreboard()
    play_again()
