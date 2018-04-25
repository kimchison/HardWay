def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amountofcheese = 10
amountofcracker = 50
cheese_and_crackers(amountofcheese, amountofcracker)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amountofcheese + 100, amountofcracker + 1000)

print "We can also ask you for the numbers:"
usercheese = int(raw_input("How much cheese do we have?\n"))
usercrackers = int(raw_input("How many crackers do we have?\n"))

cheese_and_crackers(usercheese, usercrackers)