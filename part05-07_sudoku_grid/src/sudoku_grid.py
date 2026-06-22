# Write your solution here

def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if row_correct(sudoku, i) == False or column_correct(sudoku, i) == False:
            return False

    for j in range(0, 7, 3):
        for k in range(0, 7, 3):
            if block_correct(sudoku, j, k) == False:
                return False
    return True


def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    for i in range(1,10):
        if row.count(i) > 1:
            return False
    return True


def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row_no in range(len(sudoku)):
        element = sudoku[row_no][column_no]
        if element in numbers:
            return False
        elif element != 0:
            numbers.append(element)
    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            number = sudoku[i][j]
            if number > 0 and number in numbers:
                return False
            else:
                numbers.append(number)
    return True



