#create mapping of state abbreviations

states = {
	'Oregon': 'OR',
	'Florida': ' FL',
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