import random
from turtle import position

board = ["-", "-" , "-",
       "-", "-", "-",
       "-", "-", "-"]

Player = ""
winner = None
gameRun = True


# print the game board

def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("+-+-+-+-+")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("+-+-+-+-+")
    print(board[6] + " | " + board[7] + " | " + board[8])



#taking player input

def playerInp(board):
    num = int(input("Enter a number 1-9: "))
    if num >= 1 and num <= 9 and board[num-1] == "-":
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
        gameRun = False

def Player2(current):
    if current == "" or current == "o":
        return "x"
      
    elif current == "x":
        return "o"

def computer(board):
    while Player == "o":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "o"
            Player2()
    

#

while gameRun:
    print_board(board)
    playerInp(board)
    check_winner(board)
    checkIfWinner(board)
    Player2()
    computer(board)
