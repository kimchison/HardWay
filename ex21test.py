def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def test(a, b):
	print "So what about %d and %d?" % (a, b)
	return a / b

adder = add(50, 10)
testing = test(15, 10)

print "Hello, %d and %d" % (adder, testing)
print "\n_______________________________\n"


