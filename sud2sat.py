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

    return puzzle_string

#Converts base 9 ijk to base 10 + 1
def base9To10(i,j,k):
    return 81*i + 9*j + k + 1

#Clauses for the preset cells set by the input file
def genInitialVars(puzzle):
    global n
    string = "(Initial Clauses)\n";
    for i in range(9):
        for j in range(9):
            c = puzzle[i*9+j]
            if c != '0':
                string += str(base9To10(i,j,int(c)-1)) + ' 0\n'
                n += 1
    return string

#Clauses ensuring each cell has a number
def genCellVars():
    global n
    string = "(Cell Clauses)\n"
    for i in range(9):
        for j in range(9):
            for k in range(9):
                string += str(base9To10(i,j,k)) + ' '
            string  += "0\n"
            n += 1
    return string

#Clauses ensuring uniqueness through rows
def genRowVars():
    global n
    string = "(Row Clauses)\n"
    for j in range(9):
        for k in range(9):
            for i in range(8):
                for l in range(i+1,9):
                    string += '-' + str(base9To10(i,j,k)) + " -" + str(base9To10(l,j,k)) + " 0\n"
                    n += 1
    return string

#Clauses ensuring uniqueness through columns
def genColVars():
    global n
    string = "(Column Clauses)\n"
    for i in range(9):
        for k in range(9):
            for j in range(8):
                for l in range(j+1,9):
                    string += '-' + str(base9To10(i,j,k)) + " -" + str(base9To10(i,l,k)) + " 0\n"
                    n += 1
    return string

#Clauses ensuring uniqueness through 3x3 sub-grids
def genSubGridVars():
    global n
    string = "(Sub-Grid Clauses)\n"
    for k in range(9): #number
        for a in range(3): #grid - x
            for b in range(3): #grid - y
                for u in range(2): #cell - x
                    for v in range(3): #cell - y
                        for w in range(u+1,3): #check cell - x
                            for t in range(3): #check cell - y
                                string += '-' + str(base9To10(3*a+u,3*b+v,k)) + " -" + str(base9To10(3*a+w,3*b+t,k)) + " 0\n"
                                n += 1
    return string

def main():
    if len(sys.argv) < 1:
        print("Provide an input file")
        sys.exit(-1)

    puzzle = parsePuzzle(sys.argv[1])

    dimacs_string = genInitialVars(puzzle) + genCellVars() + genRowVars() + genColVars() + genSubGridVars()

    print("p cnf 729 " + str(n) + "\n" + dimacs_string)

if __name__ == "__main__":
    main()
