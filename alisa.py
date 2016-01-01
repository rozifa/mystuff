name = raw_input ("What is your name?")
print "How are you?"
mood = raw_input("Are you happy or sad?")

if mood == "happy":
	print "Hello Mr. HappyMan! AKA %r." % name
elif mood == "sad":
	print "Goodbye Mr. Sadman! AKA %r" % name
else:
	print "Sorry %r, you can only be happy or sad!" % name
  