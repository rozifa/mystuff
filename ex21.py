#Defines four basic functions that each take two arguments: a, b.
#Each function prints a string formatted with each of the input arguments
#Then returns a value. This returned value can be stored in variables
#IT IS NOT PRINTED, it simply tells the function what its final output should
#be. This has to be stored or printed to be viewed. 
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

#prints a string
print "Let's do some math with just functions"

#Assigns the values of each of the functions with some differing arguments
#to four different variables.
age = add(30, 5)
height = multiply(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

#Prints string formatted with the values of the four variables. These values 
#are obtained by applying the defined functions tot heir respective arguments.
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#Puzzle for extra credit
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#This is just a chain of functions that use returned values as arguments in 
#other functions. 
print "That becomes", what, "Can you do it by hand?"


