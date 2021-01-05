# sodoku_solve.py
# github test #2
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


# checks to see if the inserted number is valid
def is_number_valid(brd, num, pos):
    # checks row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False
    # checks column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False
    # check squares
    sq_x = pos[1] // 3
    sq_y = pos[0] // 3
    for i in range(sq_y * 3, sq_y * 3 + 3):
        for j in range(sq_x * 3, sq_x * 3 + 3):
            if brd[i][j] == num and (i, j) != pos:
                return False
    return True


# prints nxn board
def print_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")


def find_unfilled(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return i, j  # returns array of position (size == 2)
    return None


# uses backtracking algorithm to solve puzzle
def solve(brd):
    find = find_unfilled(brd)  # finds the coordinates of the position to solve

    if not find:
        return True  # if there is no unfilled spaces the puzzle is solved
    else:
        row, col = find  # marks the position that is being checked as a valid number

    for i in range(1, 10):
        if is_number_valid(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True
            brd[row][col] = 0  # resets the number to try another solution

    return False


print_board(board)
solve(board)
print("\n\nSolving...\n\n")
print_board(board)
print("Solved!")
