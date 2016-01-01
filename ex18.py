#this is like my scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this jut takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "SHaw")
print_one("First!")
print_none()

# When making a function always make sure that you:
	# Started the function with def (defining it)
	# The function name follows using only characters and underscores
	# The function name is followed by an open parenthesis
	# The arguments seperated by commas follow the open parenthesis
	# Close parenthesis and end with a colon
	# All lines within the function are indented
	# Unindent after function is completed 

# When you call (use/run) a function make sure you:
	# Used the correct function name exactly
	# Open parenthesis after the name 
	# Put the values (arguments) after the open parenthesis seperated with
	# Close parenthesis