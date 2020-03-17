
# neatly print a board
def neat_board(board):
    #prints the board
    print("-----------")
    for i in range (0,len(board)):
        collumn = board[i]

        print("y: " + str(i) + str(collumn))
# To access board use
#board[y][x]  

def check(board, move):
    print("Checking board")
    #win means ANYBODY won, continue means there wasnt a tie or a dub, and tie means tie
    game_status  = "continue"
    player_who_won  = ""
    #checking the rows for a dub
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        if board[0][0] != "":
            game_status = "win"
            player_who_won = board[0][0] 

    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        if board[1][0] != "":
            game_status = "win"
            player_who_won = board[1][0]

    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        if board[2][0] != "":
            game_status = "win"
            player_who_won = board[2][0]

    #check the collumns for a dub
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        if board[0][0] != "":
            game_status = "win"
            player_who_won = board[0][0]

    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        if board[0][1] != "":
            game_status = "win"
            player_who_won = board[0][0]

    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        if board[0][2] != "":
            game_status = "win"
            player_who_won = board[0][0]
    #check the diagnols for a dub
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] != "":
            game_status = "win"
            player_who_won = board[0][0]

    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[1][1] != "":
            game_status = "win"
            player_who_won = board[0][0]

    elif move >= 9:
        game_status = "tie"
        player_who_won = "tie"

    return game_status, player_who_won
