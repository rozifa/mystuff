# create a dash printing function so I don't have to continuously retype it
def dash():
	print '-' * 20

# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'POrtland'

# print out some of the cities
dash()
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
dash()
print "Michigan's abriviation is: ", states['Michigan']
print "FLorida's abriviation is: ", states['Florida']

#do it by using the state then cities dict
dash()
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
dash()
<<<<<<< HEAD
f
=======
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
dash()
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
dash()
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

# safely get an abbreviation by state that might not be there
dash()
state = states.get('Texas')	

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city











>>>>>>> c1b8d291c48b4b27b694af3c2604611b8203abae
