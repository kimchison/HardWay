the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# goes through a list

for number in the_count:
	print "This is count %d" % number

# same
for fruit in fruits:
	print "A fruit of this type: %s" % fruit

#Mixed lists works too
# Use %r because we dont know if string or number
for i in change:
	print "I got %r" % i

#builds lists, first start with an empty
elements = []

#Use range to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	#append works on lists
	elements.append(6)

# we can print too
for i in elements:
	print "Element was: %d" % i
