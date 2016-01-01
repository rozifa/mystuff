# imports the "argv" module 
from sys import argv

# unpacks argv into script and filename components that are specified upon running the script
script, filename = argv

# assigns the open version of the filename argument to the variable txt
txt = open(filename)

# prints name of file formatted into a string
print "Her's the file called %r:" % filename
# calls the function "read" on the contents of the txt variable (opend file)
print txt.read()

#prints a string the instructs the user what to do upon the following prompt
print "Type the filename again:"
# assigns the user input to the variable "file_again" 
# assigns ">" as the prompt for the input
file_again = raw_input("> ")

# basically a repeated instance of the "txt" variable except we open the raw input assigned to the file_again variable
txt_again = open(file_again)

# prints the opened file 
print txt_again.read()

close(txt)
close(txt_again)