import sys
import os

FILE = 0
n = 0

#Parse and format input file to an array
def parsePuzzle(input_file):
    try:
        open_file = open(input_file)
    except:
        print("Can't open " + input_file)
        sys.exit(-1)

    puzzle_string = ""
    for line in open_file.readlines():
        puzzle_string += ''.join(line.split())

    puzzle_string.replace('.', '0').replace('*', '0').replace('?', '0')

    puzzle_array = [[0 for i in range(9)] for j in range(9)]

    for i in range(9):
        for j in range(9):
            puzzle_array[i][j] = puzzle_string[i*9+j]

    return puzzle_array

#Converts base 9 ijk to base 10 + 1
def base9To10(i,j,k):
    return 81*i + 9*j + k + 1

#Creates clauses for the cells set by the input file
def genInitialVars(puzzle):
    global n
    string = "";
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != '0':
                string += str(base9To10(i,j,int(puzzle[i][j])-1)) + ' 0\n'
                n += 1
    return string


def main():

    if len(sys.argv) < 1:
        print("Provide an input file")
        sys.exit(-1)

    puzzle = parsePuzzle(sys.argv[1])

    dimacs_string = genInitialVars(puzzle)
    #dimacs_string += ... add more clauses

    print("p cnf 729 " + str(n) + "\n" + dimacs_string)

if __name__ == "__main__":
    main()
