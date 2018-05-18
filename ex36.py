from sys import exit

def dead(how):
	print how, "Bad luck kid..."
	exit(0)

def start():
	print "You just hopped of your boat, sending you off to new adventures!"
	print "Infront of you is: a house, a road, a guard and the bridge you're standing on."
	print "Where do you go?"
	next = raw_input("> ")

	if next == "house":
		house()
	elif next == "road":
		road()
	elif next == "guard":
		guard()
	elif next == "bridge":
		bridge()
	else:
		print "What do you want to do?"
		start()

def house():
	print "You enter the house."
	print "You see a cupboard, a spider in the celling and a stove."
	print "What do you interact with?"
	spider_moved = False

	while True:
		next = raw_input("> ")

		if next == "cupboard":
			print "You find 5 coins, good job!" # add coin and inventory
		elif next == "scare spider":
			print "The spider moves, unveiling 2 coins, good job!"
			spider_moved = True
		elif next == "spider" and not spider_moved:
			dead("The spider bites you, apparently it's a black widow")
		elif next == "spider" and spider_moved:
			print "The spider thinks of  you as it's God. Congratulations!"
		elif next == "stove":
			print "Somebody forgot to eat the stew on the stove. Fill yourself up!"
		elif next == "exit":
			start()
		else:
			print "What do you want to do? You can always exit your current location!\n"
			house()

start()