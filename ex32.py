# important to remember that lists are zero indeed in python
# if you have list = [3, 4, 5, 6] then if you wanted to insert the element 16 before the element 5 you would call the insert function on the list like so
# 	list.insert(2, 16) 2 is the position of the element in the list to insert before and 16 is the inserted value. 

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go thrugh mixed lists too
# notice we have to use %r since we don't know what's in the list
for i in change:
	print "I got %r" % i 

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i 
	# append is a funtion that lists understand
	elements.append(i)

	# Alternitvley, the for-loop can easily be avoided in this instance:
	# elements = range(0, 6)

# now we can print them out too
for i in elements:
	print "Element was: %d." % i



