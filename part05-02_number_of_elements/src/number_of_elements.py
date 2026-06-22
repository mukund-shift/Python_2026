# Write your solution here

def count_matching_elements(matrix: list, target: int):
    ctr = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                ctr += 1
    return ctr
