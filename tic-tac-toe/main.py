print("Tic tac toe")
board = []

dim = 3
# create board to be dim * dim
for y in range(0,dim):
    row = []
    for x in range(0,dim):
        row.append("")

    board.append(row)


# neatly print a board
def neat_board(board):
    #prints the board
    print("-----------")
    for collumn in board:

        print(collumn)
# To access board use
#board[y][x]  

neat_board(board)





