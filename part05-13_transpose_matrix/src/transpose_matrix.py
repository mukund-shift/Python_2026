
def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if i != j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
