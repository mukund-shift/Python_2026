# Write your solution here


def newprint(char: str):
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        char = variables[char]
    else:
        char = int(char)
    printed.append(char)

def mov(variable: str, value: str):
    global variables
    if value in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        variables[variable] = variables[value]
    else:
        variables[variable] = int(value)

def add(variable: str, value: str):
    global variables
    if value in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        variables[variable] += variables[value]
    else:
        variables[variable] += int(value)

def sub(variable: str, value: str):
    global variables
    if value in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        variables[variable] -= variables[value]
    else:
        variables[variable] -= int(value)

def mul(variable: str, value: str):                     # mov,add,sub,mul all modify variables dict
    global variables
    if value in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        variables[variable] *= variables[value]
    else:
        variables[variable] *= int(value)

def location(location : str, line_idx : int):           # adds location to global locations list
    global locations
    locations[location[:-1]] = line_idx

def condition_checker(exp: list):                       # returns bool
    global variables
    if exp[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        val1 = variables[exp[0]]
    else:
        val1 = int(exp[0])
    if exp[2] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        val2 = variables[exp[2]]
    else:
        val2 = int(exp[2])                            # value setting for comparison

    if exp[1] == "==":
        return val1 == val2
    elif exp[1] == ">=":
        return val1 >= val2
    elif exp[1] == "<=":
        return val1 <= val2
    elif exp[1] == "!=":
        return val1 != val2
    if exp[1] == ">":
        return val1 > val2
    if exp[1] == "<":
        return val1 < val2

def operation(line: str):
    global locations
    global ctr
    parts = line.split(" ")
    if parts[0] == "PRINT":
        newprint(parts[-1])
    elif parts[0] == "MOV":
        mov(parts[1], parts[2])
    elif parts[0] == "ADD":
        add(parts[1], parts[2])
    elif parts[0] == "SUB":
        sub(parts[1], parts[2])
    elif parts[0] == "MUL":
        mul(parts[1], parts[2])
    elif parts[0] == "JUMP":
        ctr = locations[parts[-1]]
    elif parts[0] == "IF":
        if condition_checker(parts[1:4]):
            ctr = locations[parts[-1]]


def run(program: list):
    global ctr
    length = len(program)

    for k in range(length):                                 # populates locations pre-execution
        if ":" in program[k]:
            location(program[k], k)

    while True:
        line = program[ctr]
        if line == "END":
            break
        operation(line)
        ctr += 1
        if ctr >= length:
            break
    return printed

if __name__ == "__main__":
    variables = {
    "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
    "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0,
    "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0
    }                                                           # "A" : value
    locations = {}                                              # "begin" : line_index
    printed = []
    ctr = 0
    
    program4 = []
    
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)


