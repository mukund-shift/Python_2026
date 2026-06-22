# Write your solution here
def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row_no in range(len(sudoku)):
        element = sudoku[row_no][column_no]
        if element in numbers:
            return False
        elif element != 0:
            numbers.append(element)
    return True