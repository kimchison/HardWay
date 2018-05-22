class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
	"I don't want to get sued", 
	"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
	"With pockets full of shells"])

heil = Song(["Heil to Fuhrer",
	"Heil Hitler"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

heil.sing_me_a_song()

'''
class lyri(object):
	def __init__(self, lyrica):
		self.lyrica = lyrica

	def sing_lyrica(self):
		for line in self.lyrica:
			print line
'''