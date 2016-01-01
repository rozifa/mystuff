# Defines the cheese and crackers funtion and its two arguments. Specifies #what the function should do (printing strings formatte with arguments). 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

#Shows that arguments can be input directly into the function
print "we can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#Shows that variables can be used to store values that are then input into the
#function
print "OR, we cna use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Arguments are mathematical expressions 
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#Uses expressions with pre assigned variables as components within the #arguments of the function. 
print "And we can combine the two, variable and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)