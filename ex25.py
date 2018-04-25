def breakwords(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sortwords(words):
	"""Sorts the words"""
	return sorted(words)

def printfirstword(words):
	"""Prints the first words after popping it off"""
	word = words.pop(0)
	print word

def printlastword(words):
	"""Prints the last word after popping"""
	word = words.pop(-1)
	print word

def sortsentence(sentence):
	"""Takes full sentence and return sorted words"""
	words = breakwords(sentence)
	return sortwords(words)

def printfirstandlast(sentence):
	"""Prints thef irst and last word of sentence"""
	words = breakwords(sentence)
	printfirstword(words)
	printlastword(words)

def printfirstandlastsorted(sentence):
	"""Sorts the words then rpints first n last"""
	words = sortsentence(sentence)
	printfirstword(words)
	printlastword(words)