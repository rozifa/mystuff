#Raw input prompts the user for an input and can be used to assign the input
#value to a variable. 

#Prints questions and asks for input, once input is received, code proceeds #and continues to print. 
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight= raw_input()

#Prints formatted string using variables that were assigned using raw input. 
print "So, youre %r old, %r tall and %r heavy." %(
	age, height, weight)