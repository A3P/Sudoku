import sys
import os

def parseInput(input_file):
    try:
        open_file = open(input_file)
    except:
        print("Can't open " + input_file)
        sys.exit(-1)

    content = open_file.read().split()

    if content[0] != "SAT":
        print("No solution")
        sys.exit(-1)

    solution = []

    for x in content:
        if x.isdigit():
            x = int(x)
            if x > 0:
                solution.append((x-1)%9+1)
    return solution

def printPuzzle(solution):
    string = ''
    for i in range(9):
        if i % 3 == 0:
            for k in range(13):
                string += '-'
            string += '\n'

        for j in range(9):
            if j % 3 == 0:
                string += '|'
            string += str(solution[i*9+j])
        string += "|\n"

    for k in range(13):
        string += '-'

    print (string)

def main():
    if len(sys.argv) < 1:
        print("Provide an input file")
        sys.exit(-1)

    solution = parseInput(sys.argv[1])

    printPuzzle(solution)

    #write the solution to a file

if __name__ == "__main__":
    main()
