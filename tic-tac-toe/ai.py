import random
from game_req import check, neat_board
print("Tic tac toe")
board = []

dim = 3
# create board to be dim * dim
for y in range(0,dim):
    row = []
    for x in range(0,dim):
        row.append("")

    board.append(row)


current_move = 1
move_counter = 1
while True:

    neat_board(board)
    if current_move == 1:
        x = input("X position to move: ")
        y = input("Y position to move: ")

        if x == "q" or y == "q":
            break

        y = int(y)
        x = int(x)
        board[y][x] = current_move
    else:
        # ai's move

        availible_pos = []
        for i in range (0,len(board)):
            collumn = board[i]
            for j in range (0, len(collumn)):
                square = board[i][j]
                if square == "":
                    availible_pos.append({ "y" : i, 'x' : j})

        print(availible_pos)

        # generate an index
        index = random.randint(0, len(availible_pos))
        print(availible_pos[index])

        board[availible_pos[index]["y"]][availible_pos[index]["x"]] = current_move



        


    status, player = check(board, move_counter)
    
    if status != "continue":
        print(status)
        neat_board(board)
        break

    current_move = current_move * -1
    move_counter = move_counter + 1

print("Thanks for playing!")
