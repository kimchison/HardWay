from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

penis = int(raw_input("How big is your penis? (In cm please!)"))
if penis < 13:
	print ":/",
else:
	print "You good! :D"