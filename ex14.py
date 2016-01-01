from sys import argv 

#I guess arguments are like raw inputs that occur before actually running the script?
script, user_name, last_name = argv
prompt = 'meme'

print "Hi %s from the %s family, I'm the %s script." % (user_name, last_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)