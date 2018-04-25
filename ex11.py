print "How old are you?",
age = int(raw_input())
print "How tall are you?",
height = int(raw_input())
print "How much do you weight?",
weight = int(raw_input())
print '''So, you're %r years old, %r cm's tall and %r kg's heavy.''' % (
	age, height, weight)