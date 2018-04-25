from sys import argv

script, user_name = argv
question = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "i'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(question)

print "Where do you live %s?" % user_name
lives = raw_input(question)

print "What kind of computer do you have?"
computer = raw_input(question)

print "How big is your dick?"
dick = raw_input(question)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Cool.
Your dick is also %r. Nice...
""" % (likes, lives, computer, dick)