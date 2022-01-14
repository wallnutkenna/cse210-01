#McKenna Wall CSE 210 1.11.2022

from typing import Counter
import math

playersymbol = ["X", "O"]

boardsize = int(input("How big whould you like the board? "))
def main():
    #boardsize = 3
    board = createboard()
    win = False
    draw = False
    counter = 0
    while not (win or draw):
        # displayboard(board)
        # makemove(player, board)
        win, draw = playersturn(board, counter%2)
        if not win:
            counter += 1

    displayboard(board)
    if win:
        print("Good Game. Player " + str(playersymbol[counter%2]) +" Lets play again sometime.")
    elif draw:
        print("Draw! Good Game. Lets play again sometime.")

def createboard():
    board = []
    counter = 0
    for i in range(boardsize):
        row = []
        for j in range(boardsize):
            counter += 1
            row.append(str(counter))
        board.append(row)
    return board
    #board = [][]
    #board = [size][size]d
    #row = squares[size]
    #row1 = squares[size]
    #row2 = squares[size]
    #board = rows[size]
    
def displayboard(board):
    boardString = ""
    dividerString = ""
    for k in range(boardsize):
        dividerString += "---"

    for i in range(boardsize):
        for j in range(boardsize):
            if j == 0:
                boardString += board[i][j]
            else:
                boardString += " | " + board[i][j]
        if i == 0:
            print(boardString)
            boardString= ""
        else:
            print(dividerString)
            print(boardString)
            boardString= ""
            

def makemove(player, board):
    space = "0"
    while(int(space) < 1 or int(space) > boardsize*boardsize):
        space = input(f"{str(playersymbol[player])}'s turn to choose a square (1-{boardsize*boardsize}): ")
    
    rowIndex = math.floor((int(space)-1)/boardsize)
    columnIndex = (int(space)-1)%boardsize
    #print("tried to go to " + str(rowIndex) + " " + str(columnIndex))
    if board[rowIndex][columnIndex] not in playersymbol:
        board[rowIndex][columnIndex] = playersymbol[player]
    else:
        makemove(player, board)


def playersturn(board,player):
    displayboard(board)
    makemove(player,board)
    return checkwin(board,playersymbol[player]) or draw(board)
    

def check_diagonal(board, playertoken):
    win = False
    counter = 0
    #left to right
    for i in range(boardsize):
        if(board[i][i] == playertoken):
            counter+= 1
    if counter == boardsize:
        win = True
    else:
        counter = 0
    for i in range(boardsize):
        if(board[i][(boardsize-1)-i] == playertoken):
            counter+= 1
    if counter == boardsize:
        win = True
    return win

def checkrow(board, playertoken):
    win = False
    #right to left
    counter = 0
    for i in range(boardsize):
        for j in range(boardsize):
            if(board[i][j] == playertoken):
                counter+= 1
        if counter == boardsize:
            win = True
        else:
            counter = 0
    return win

def checkcolumn(board, playertoken):
    win = False
    #top to bottom
    counter = 0
    for i in range(boardsize):
        for j in range(boardsize):
            if(board[j][i] == playertoken):
                counter+= 1
        if counter == boardsize:
            win = True
        else:
            counter = 0
    return win

def draw(board):
    for i in range(boardsize):
        for j in range(boardsize):
            if(board[i][j] != "X" and board[i][j] != "O"):
                return False
    return True 

def checkwin(board,playertoken):
    win = False
    gamedraw = False
    win |= check_diagonal(board,playertoken)
    win |= checkcolumn(board,playertoken)
    win |= checkrow(board,playertoken)
    gamedraw |= draw(board)
    if win:
        print(playertoken + " " + str(win))
    elif draw:
        print(playertoken + " " + str(win))
    return win, gamedraw

if __name__ == "__main__":
    main()