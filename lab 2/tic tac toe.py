board = [" "] * 9

def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()



def check_winner(player):
    winning_combinations = [
        (0, 1, 2), 
        (3, 4, 5), 
        (6, 7, 8),  
        (0, 3, 6),  
        (1, 4, 7),  
        (2, 5, 8),  
        (0, 4, 8),  
        (2, 4, 6)   
    ]

    for a, b, c in winning_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False  


player = "X"

print("TIC-TAC-TOE")
print("Positions are:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")


for turn in range(9):

    display_board()

   
    position = int(input("Player " + player + ", enter position (1-9): "))

   
    if board[position - 1] != " ":
        print("Position already occupied! Try again.")
        continue

    
    board[position - 1] = player

    if check_winner(player):
        display_board()
        print("Player", player, "wins!")
        break


    if turn == 8:
        display_board()
        print("It's a draw!")
        break

   
    if player == "X":
        player = "O"
    else:
        player = "X"