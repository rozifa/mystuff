#Use raw input to prompt the user to input specific data. A string is used
#within the raw input function to specify a prompt.
#Each eanswer to each prompt is stored in a given specific variable.
age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")

#Prints a sentence formatted with the values assigned previously to the three
#variables. These values were assigned through the use of raw input. 
print "So, you're %r old, %r tall, and %r heavy." %(
	age, height, weight)
