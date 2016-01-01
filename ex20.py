#Imports the argv module from the sys package
from sys import argv

#Unpacks arguments
script, input_file = argv

#Defines the functon print all to take one argument, f, and tells it to print
#the read version of the f argument
def print_all(f):
	print f.read()

#Defines the rewind function to take one argument, f, and tells it to seek the
#0th byte of the input argument (goes to beggining of the file)
def rewind(f):
	f.seek(0)

#Defines the print a line function to take two arguments, first the line count
#then f (a file)
#This function reads the current line in the file after the line number
def print_a_line(line_count, f):
	print line_count, f.readline()

#Assigns the opened input file to the current file variable
current_file = open(input_file)

#Prints string
print "First let's print the whole file:\n"

#Prints the entire file
print_all(current_file)

#Prints string
print "Now let's rewind, kind of like a tape."

#Moves back to byte zero of the current input file
rewind(current_file)

#Prints string
print "Let's print three lines:"

#Advances through the three lines printing each one after its line number
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)