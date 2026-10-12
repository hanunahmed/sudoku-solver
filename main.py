board = [
    [0, 0, 6, 0, 0, 0, 5, 0, 8],
    [1, 0, 2, 3, 8, 0, 0, 0, 4],
    [0, 0, 0, 2, 0, 0, 1, 9, 0],
    [0, 0, 0, 0, 6, 3, 0, 4, 5],
    [0, 6, 3, 4, 0, 5, 8, 7, 0],
    [5, 4, 0, 9, 2, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 4, 0, 0, 0],
    [2, 0, 0, 0, 9, 8, 4, 0, 7],
    [4, 0, 9, 0, 0, 0, 3, 0, 0],
]


def display_board(board):
    for row_index, row in enumerate(board):
        if row_index in (3, 6):
            print("-" * 21)
        row_values = []
        for col_index, value in enumerate(row):
            if value == 0:
                row_values.append(".")
            else:
                row_values.append(str(value))

            if col_index in (2, 5):
                row_values.append("|")

        print(" ".join(row_values))


def find_empty(boardArr):
    for index, n in enumerate(boardArr):
        for i, j in enumerate(n):
            if j == 0:
                return (index, i)
    return None


def check_column(boardArr, column, number):
    for n in boardArr:
        if n[column] == number:
            return False
    return True


def checkBox(boardArr, row, column, number):
    start_row = (row // 3) * 3
    start_column = (column // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_column, start_column + 3):
            if boardArr[r][c] == number:
                return False
    return True


def is_valid(boardArr, row, column, number):
    if number in boardArr[row]:
        return False
    if check_column(boardArr, column, number) == False:
        return False
    if checkBox(boardArr, row, column, number) == False:
        return False

    return True


def solve(board):
    empty = find_empty(board)

    if empty is None:
        return True
    row, column = empty

    for n in range(1, 10):
        if is_valid(board, row, column, n):
            board[row][column] = n
            if solve(board):
                return True
            board[row][column] = 0
    return False


if solve(board):
    print("Solved Sudoku:\n")
    display_board(board)
else:
    print("No solution exists.")
