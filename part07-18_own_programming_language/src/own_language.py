# Write your solution here
import sys

variables = {}                                              # "A" : value
locations = {}                                              # "begin" : line_index
printed = []
ctr = 0

def newprint(char: str):
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        char = variables[char]
    else:
        char = int(parts[0])
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

def location(location : str, line_idx : int):                           # adds location to global locations list
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
    else:
        location(parts[0], ctr)


def run(program: list):
    length = len(program)
    global ctr
    while True:
        line = program[ctr]
        if line == "END":
            break
        operation(line)
        ctr += 1
        if ctr >= length:
            break
    return printed

program2 = []
program2.append("MOV A 1")
program2.append("MOV B 10")
program2.append("begin:")
program2.append("IF A >= B JUMP quit")
program2.append("PRINT A")
program2.append("PRINT B")
program2.append("ADD A 1")
program2.append("SUB B 1")
program2.append("JUMP begin")
program2.append("quit:")
program2.append("END")
result = run(program2)
print(result)

