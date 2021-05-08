import numpy as np

board = np.array([[0, 0, 0, 0, 3, 4, 9, 2, 0],
                  [9, 0, 3, 0, 0, 2, 0, 5, 1],
                  [0, 5, 0, 1, 8, 0, 0, 0, 3],
                  [2, 0, 0, 0, 4, 7, 6, 0, 5],
                  [0, 0, 0, 0, 0, 6, 7, 3, 4],
                  [4, 0, 0, 0, 5, 0, 2, 0, 0],
                  [7, 0, 0, 3, 0, 1, 0, 0, 8],
                  [0, 0, 0, 0, 6, 0, 3, 4, 2],
                  [3, 8, 6, 4, 0, 0, 1, 0, 0]])

invalidBoard = np.array([[0, 2, 0, 0, 3, 4, 9, 2, 0],
                         [9, 0, 3, 0, 0, 2, 0, 5, 1],
                         [0, 5, 0, 1, 8, 0, 0, 0, 3],
                         [2, 0, 0, 0, 4, 7, 6, 0, 5],
                         [0, 0, 0, 0, 0, 6, 7, 3, 4],
                         [4, 0, 0, 0, 5, 0, 2, 0, 0],
                         [7, 0, 0, 3, 0, 1, 0, 0, 8],
                         [0, 0, 0, 0, 6, 0, 3, 4, 2],
                         [3, 8, 6, 4, 0, 0, 1, 0, 0]])
def printBoard(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            print(str(bo[i][j]) + ' ', end='')
            if j != 0 and j != 8 and j % 3 == 2:
                print('| ', end='')
        print()
        if i != 0 and i != 8 and i % 3 == 2:
            print('---------------------')
def empty_value(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return (i, j)  # (row, col)
    return None
def valid_input(bo, val, pos_tup):


    # figure out which 3 x 3 square it's in:
    sq_row_start = pos_tup[0] // 3 * 3
    sq_col_start = pos_tup[1] // 3 * 3

    # check each column value in row AND each row value in column AND each val in local 3 x 3 square
    for i in range(len(bo)):
        sq_row = sq_row_start + i // 3
        sq_col = sq_col_start + i % 3
        if val == bo[pos_tup[0]][i] and i != pos_tup[1]:
            return False
        if val == bo[i][pos_tup[1]] and i != pos_tup[0]:
            return False
        if bo[sq_row][sq_col] == val and (sq_row, sq_col) != pos_tup:
            return False
    return True
def solveBacktrackingAlg(bo):

    empty_val_pos = empty_value(bo)
    if empty_val_pos == None:
        return True
    else:
        for i in range(1, 10):
            if valid_input(bo, i, empty_val_pos):
                bo[empty_val_pos[0]][empty_val_pos[1]] = i

                if solveBacktrackingAlg(bo):
                    return True
                bo[empty_val_pos[0]][empty_val_pos[1]] = 0
        return False
printBoard(invalidBoard)
print(solveBacktrackingAlg(invalidBoard))
print('--------------------------------------------')
printBoard(invalidBoard)
