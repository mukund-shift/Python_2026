# Write your solution here
def print_sudoku(sudoku: list):
    row_ctr = 0
    for i in range(len(sudoku)):
        col_ctr = 0
        for j in range(len(sudoku[0])):
            col_ctr += 1
            if sudoku[i][j] == 0:
                print("_ ", end = "")
            else:
                print(str(sudoku[i][j]) + " ", end = "")
            if  col_ctr == 3:
                col_ctr = 0
                print(" ", end = "")
        row_ctr += 1
        print()
        if row_ctr == 3:
            row_ctr = 0
            print()


def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

