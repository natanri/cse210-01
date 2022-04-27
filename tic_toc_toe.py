import random
from turtle import position

#TIC TAC TOE assignment
#Jhonatan Rios

board = ["1", "2" , "3",
       "4", "5", "6",
       "7", "8", "9"]

Player = "x"
winner = None
gameRun = True


# print the game board

def print_board(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("+-+-+-+-+")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("+-+-+-+-+")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()



#taking player input

def playerInp(board):
    num = int(input(f"{Player}'s turn to choose a square buddy (1-9): "))
    if num >= 1 and num <= 9 and board[num-1] == "1" or"2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
        board[num-1] = Player
        
    else:
        print("Oops player is already in that spot!")

#Check for winner 

def check_winner(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[3]
        return True
    elif board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[3]
        return True

    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True
    elif board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[3]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[3]
        return True
    
def checkIfWinner(board):
    global gameRun 
    if check_winner(board):
        print_board(board)
        print(f"The winner is {winner}!")
        print("Good game. Thanks for playing!")
        gameRun = False

def Player1():
    global Player
    if Player == "x":
        Player = "o"
      
    else:
        Player = "x"



#Run the game calling functions

while gameRun:
    print_board(board)
    playerInp(board)
    check_winner(board)
    checkIfWinner(board)
    Player1()
    
    
