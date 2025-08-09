"""Programming Tic Tac Toe with a Computer Opponent!"""

import random
from collections import Counter

def make_board(board: list[str]):
    # board is a list of each of 10 strings representing each spot of the tictactoe board
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")


def start_game():
    make_board(['0','1','2','3','4','5','6','7','8','9'])
    player: str = ""
    computer: str = ""
    # asks player to choose X or O and assigns the other to the computer
    symbol: str = input("Would you like to be X or O? ").upper()
    if symbol == "X":
        player += "X"
        computer += "O"
    else:
        player += "O"
        computer += "X"
    # randomly chooses who goes first
    order: int = random.randint(1,2)
    board: list[str] = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    if order == 1:
        print("Player goes first.")
        board = play(player,board)
        for _ in range(2,10):
            board = computer_play(computer, player, board)
            if "Draw" in board:
                print("Draw.\nType in start_game() to play again :)")
                return
            if "Computer" in board:
                print("Computer won. Better luck next time!\nType in start_game() to play again :)")
                return
            if "Player" in board:
                print("Player won. Congrats!\nType in start_game() to play again :)")
                return
            board = play(player,board)
            if "Draw" in board:
                print("Draw.\nType in start_game() to play again :)")
                return
            
    else:
        print("Computer will go first.")
        board = computer_play(computer, player, board)
        for _ in range(1,10):
            board = play(player,board)
            if "Draw" in board:
                print("Draw.\nType in start_game() to play again :)")
                return
            board = computer_play(computer, player, board)
            if "Draw" in board:
                print("Draw.\nType in start_game() to play again :)")
                return
            if "Computer" in board:
                print("Computer won. Better luck next time!\nType in start_game() to play again :)")
                return
            if "Player" in board:
                print("Player won. Congrats!\nType in start_game() to play again :)")
                return
            


def place(symbol: str, num: int, board: list[str] ) -> list[str]:
    board[num] = symbol
    make_board(board)
    new_board: list[str] = board
    counter = Counter(new_board)
    if counter[" "] == 1:
        win_msg: str = "Draw."
        return win_msg
    return new_board


def play(symbol: str, board: list[str]):
    if ' ' not in board:
        win_msg: str = "Draw."
        return win_msg
    print("Player's turn.")
    num: int = int(input("Please pick a spot on the board (number from 1-9): "))
    return place(symbol, num, board)


def computer_play(symbol: str, player_symbol: str, board: list[str]): 
    # the current board divided into sections
    row1: list[str] = [board[1], board[2], board[3]]
    row2:  list[str] = [board[4], board[5], board[6]]
    row3: list[str] = [board[7], board[8], board[9]]
    column1: list[str] = [board[1], board[4], board[7]]
    column2: list[str] = [board[2], board[5], board[8]]
    column3: list[str] = [board[3], board[6], board[9]]
    diagonal1: list[str] = [board[1], board[5], board[9]]
    diagonal2: list[str] = [board[3], board[5], board[7]]
    # just the numbers of each section on the board
    idx_row1: list[int] = [1,2,3]
    idx_row2: list[int] = [4,5,6]
    idx_row3: list[int] = [7,8,9]
    idx_column1: list[int] = [1,4,7]
    idx_column2: list[int] = [2,5,8]
    idx_column3: list[int] = [3,6,9]
    idx_diagonal1: list[int] = [1,5,9]
    idx_diagonal2: list[int] = [3,5,7]
    sums: list[str] = [row1, row2, row3, column1, column2, column3, diagonal1, diagonal2]
    indexes: list[int] = [idx_row1, idx_row2, idx_row3, idx_column1, idx_column2, idx_column3, idx_diagonal1, idx_diagonal2]
    # checks if player has won.
    for sum in sums:
        counter = Counter(sum)
        if counter[player_symbol] == 3:
            win_msg: str = "Player wins."
            return win_msg
    # checks if there is a draw
    count: int = 0 # used to count if each of the vertical/horizontal/diagonal sections have a symbol in each of the three spots. adds a number if the row/column/etc is filled.
    for sum in sums:
        counter = Counter(sum)
        if counter[symbol] + counter[player_symbol] == 3:
            count += 1
    if count == len(sums):
        win_msg: str = "Draw."
        return win_msg
    print("Computer's turn.")
    # computer goes in for the win
    idx: int = 0
    for sum in sums:
        counter = Counter(sum)
        if counter[symbol] == 2:
            i: int = 0
            while i < 3:
                if (sum[i] != symbol) and (sum[i] != player_symbol):
                    # have to find the number of the spot that will cause computer to win.
                    num: int = (indexes[idx])[i]
                    win_msg: str = "Computer wins."
                    return place(symbol, num, board) and win_msg
                i += 1
        idx += 1
    # computer blocks player
    idx: int = 0
    for sum in sums:
        counter = Counter(sum)
        if counter[player_symbol] == 2 and counter[symbol] == 0:
            i: int = 0
            while i < 3:
                if (sum[i] != player_symbol) and (sum[i] != player_symbol):
                    # have to find the number of the spot that will cause computer to win.
                    num: int = (indexes[idx])[i]
                    return place(symbol, num, board)
                i += 1
        idx += 1
    # computer places randomly --> have to switch so computer makes smart moves (makes it so that there is 2 computer symbols out of 3.)
    i : int = 1
    free_spots: list[int] = []
    while i < len(board):
        if (board[i] != symbol) and (board[i] != player_symbol):
            free_spots.append(i)
            i += 1
        i += 1
    return place(symbol, random.choice(free_spots), board)
 