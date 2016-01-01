#Assigns string value to x variable. 10 is formatted into the string using %d
x = "There are %d types of people." % 10

#Assigns string value to binary variable
binary = "binary"

#Assigns string value to do_not variable
do_not = "don't"

#Assigns string value to y variable. Binary and do_not values are formatted 
#into the string using %s and listing them after the string in parenthesis.
y = "Those who know %s and those who %s." % (binary, do_not)

#Prints x
print x

#Prints y
print y

#Prints string with value of x formatted into the string using %r "formatter".
print "I said %r." % x

#Prints string with value of y formatted into the string using %r "formatter".
print "I also said: '%s'." % y

#Assigns boolean value of false to hilarious variable
hilarious = False 

#assigns string value to joke_evaluation variable and creates placeholder for #"formatting" a value into the string. 
joke_evaluation = "Isn't that joke so funny?! %r"

#Prints value of joke evaluation variable, which is a string. This string has 
#a formatting placeholder in the form of %r. Formats the boolean value of
#hilarious into the printed string using the %.
print joke_evaluation % hilarious

#Assigns string value to variable w
w = "This is the left side of..."

#Assigns string value to variable e
e = "a string with a right side."

#Prints concatenated string by "adding" string values of w and e variable
#This renders a continous and logical string made up of two seperate strings
#That were assigned to the variables w and e. 
print w + e 


#Study drills

#There are five total places where a string is formatted into a string. 
#Adding the "w" and "e" variables with "+" creates a longer string because 
#this operation adds two strings together; 
	# x + y = z : z > x : z > y