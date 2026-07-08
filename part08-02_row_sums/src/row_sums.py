# Write your solution here
def row_sums(my_matrix: list):
    for i in range(len(my_matrix)):
        summ = 0
        for j in range(len(my_matrix[i])):
            summ += my_matrix[i][j]
        my_matrix[i].append(summ)

if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
