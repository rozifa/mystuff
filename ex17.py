#imports the argv module fomr the sys package
from sys import argv
#imports the exists module from the os.path package
from os.path import exists 

#unpacks argument 
script, from_file, destination_file = argv

#prints formatted string with names of files input as arguments 
print "Coying %s to %s." % (from_file, destination_file)

#opens the file specified in the second argument then reads it and stores this #value in indata
indata = open(from_file).read()

#prints the leangth of the file by using the len function on the contents of #the indata variable
print "The input file is %d bytes long" % len(indata)

#i guess the "exists" function checks wether a file exists
#prints the boolean value fomratted into a string 
#uses an empty raw input to confirm (code only proceeds upon input)
print "Does the output file exist %r" % exists(destination_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#assigns the value of the destination file specified in an argument to variable
#in writable mode  (default is read when using the open function)
#writes the contents of indata to the value of the outfile variable
out_file = open(destination_file, "w")
out_file.write(indata)

#prints string to notify user that operation is finished
print "Alright, all done."

#closes the outfile
#from_file doesnt need to be closes becasue of how the ode is written for #indata
out_file.close()