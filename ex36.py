from sys import exit

coins = 0
what_next() = print "What do you want to do next in the %s?" % what_next

def house():
	print "You enter the house."
	print "You see a cupboard, a spider in the celling and a stove."
	print "What do you interact with?"
	spider_moved = False

	while True:
		next = raw_input("> ")

		if next == "cupboard":
			print "You find 5 coins, good job!"
			coins = 5
			what_next(house)
	else:
		print "What do you want to do?"

<<<<<<< HEAD
=======


def guard(): 

def start():
	print "Enter ***"


>>>>>>> e408702e6bce0f8149bf5eb3d1a04497c8dab0df
house()