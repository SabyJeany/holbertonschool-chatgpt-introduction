#!/usr/bin/python3
board=[[" "]*3 for _ in range(3)]

def print_board():
    for row in board:
        print(" | ".join(row))
        print("-"*5)

def check_winner():
    for r in board:
        if r[0]==r[1]==r[2]!=" ":
            return r[0]
    for c in range(3):
        if board[0][c]==board[1][c]==board[2][c]!=" ":
            return board[0][c]
    if board[0][0]==board[1][1]==board[2][2]!=" ":
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0]!=" ":
        return board[0][2]
    return None

def play():
    player="X"
    moves=0
    while True:
        print_board()
        try:
            r=int(input(f"Player {player}, row 0-2: "))
            c=int(input(f"Player {player}, col 0-2: "))
        except:
            print("Numbers only"); continue
        if not (0<=r<=2 and 0<=c<=2):
            print("Out of bounds"); continue
        if board[r][c]!=" ":
            print("Taken!"); continue
        board[r][c]=player
        moves+=1
        winner=check_winner()
        if winner:
            print_board(); print(f"Player {winner} wins!"); break
        if moves==9:
            print_board(); print("Draw!"); break
        player="O" if player=="X" else "X"

if __name__=="__main__":
    play()

