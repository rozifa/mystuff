#Assigns values to variables
name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches 
weight_pounds = 180 # lbs
eyes = "Blue"
teeth = "White"
hair = "Brown"

#Prints sentences with "formatters"
print "Let's talk about %s" % name
print "He's %d inhes tall." % height
print "He's %d pounds heavy." % weight_pounds
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#Assigns kilo conversion vector to variable name
kilo_conversion = 0.453592

#Calculates weight in kilograms using conversion coefficent 
kilogram_weight = weight_pounds * kilo_conversion

#Prints weight in kilograms as calculated and assigned
print "His weight in kilograms is %d." % kilogram_weight

#This line is tricky, try to get it exactly right
#Prints if these variable values are added, the result is the addition of them.
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight_pounds, age + height + weight_pounds)