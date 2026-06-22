# write your solution here


def matrix_line_analysis(line):
    line = line.replace("\n", "")
    elements = line.split(",")
    total = 0
    maxm = int(elements[0])
    for element in elements:
        total += int(element)
        if int(element) > maxm:
            maxm = int(element)
    return total, maxm
    

def row_sums():
    with open("matrix.txt") as matrix:
        output = []
        for line in matrix:
            output.append(matrix_line_analysis(line)[0])
        return output


def matrix_sum():
    values = row_sums()
    return sum(values)


def matrix_max():
    with open("matrix.txt") as matrix:
        maxm = None
        for line in matrix:
            line_max = matrix_line_analysis(line)[1]
            if maxm == None or maxm < line_max:
                maxm = line_max
        return maxm


if __name__ == "__main__":
    
    print(matrix_max())
    print(matrix_sum())
    print(row_sums())