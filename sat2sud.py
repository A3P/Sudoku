import sys
import os
def genSudoku(s):
	output_file = ''
	for i in s.read().split(" "):
	#Handling Exceptions
		try:
			if int(i) > 110:
				if int(i[1]) == 0 or int(i[2]) == 0:
					continue
				output_file += i[2]
				if (len(output_file) - output_file.count('\n')) % 9 == 0:
					output += '\n'
		except ValueError:
			continue
	print (output_file)
f= open("miniSAT_Output.txt", "r")
genSudoku(f)
f.close() 