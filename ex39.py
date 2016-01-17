def dash():
	print '-' * 20

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'POrtland'

dash()
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

dash()
print "Michigan's abriviation is: ", states['Michigan']
print "FLorida's abriviation is: ", states['FLorida']

dash()
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

dash()
f