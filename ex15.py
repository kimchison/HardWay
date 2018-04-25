from sys import argv

#Pulls script and filename from user input in Shell
script, filename = argv

#'opens' or 'prepares' filename to Shell
txt = open(filename)

#Prints name of the chosen file
print "Here's your file %r:" % filename 
#Reads/prints out the text in the file
print txt.read()

#Asks for another file/same file
print "Type the filename again:"
#userinput to variable file_again, can be new file
file_again = raw_input("> ")

#opens/prepares the new file
txt_again = open(file_again)

#reads out the chosen file
print txt_again.read()