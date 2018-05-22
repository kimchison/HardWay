''' ,
GET X FROM Y --> Gets 'apple', (which is I am apples) from mystuff:
mystuff = {'apple': "I am apples!"}
	print mystuff['apple']
'''

#create mapping of state abbreviations
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

#basic set of states and cities
cities = {
	'CA': 'San Fransisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print dem cities
print '-' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

#print some states
print '-' * 10
print "Michigans abbreviation is: ", states['Michigan']
print "Floridas abbreviation is: ", states['Florida']

#Using states then city dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#every state abbrev
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s" % (state, abbrev)

#every city abbrev
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s " % (abbrev, city)

# both same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
#test for nonexisting abbrev
state = states.get('Texas', None)

if not state:
	print "Sorry, No texas."

# get a city default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city