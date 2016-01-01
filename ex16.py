# imports the argv module form the sys package
from sys import argv

#unpakcs 
script, filename = argv

#prints these lines and formats in the filename that was asked as an argument 
print "We're goig to erase %r." % filename
print "If you don't want to do that, hit CTRL-C (^C)."
print "If you wnat to do that, hit RETURN."

#prompts with a qeustion mark
raw_input("?")

#prints the string 
print "Opening the file..."
#assigns the open file to the target variable in "w" (write) mode 
target = open(filename, "w")

#prints the string and truncates the contents of the target variable (delets it)
print "Trucating the file. Goodbye!"
target.truncate()

#prints string
print "Now I'm going to ask you for three lines."

#assignst he inputs to variables and provides individual prompts for each input instance
line1 = raw_input("line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

#formats all of the raw inputs into one string that splits each value into a new line
alllines = "%r \n %r \n %r" % (line1, line2, line3)

#prints string
print "I'm going to write these lines to the file."

#writes the contents of the alllines variable to the target variable (the wrtiable open file)
target.write(alllines)

#Closes the file and prints a string telling whats happening!
print "And finally, we close it."
target.close()