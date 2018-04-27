i = 0
numbers = []

while i < 6: 
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num

print "\nNow begins function-loop\n"

#Calls function for while-loop

def loop():
	numero = []
	numb = raw_input("PLease enter starting number: ")
	numero.append(numb)

	while int(numero) < 6:
		print "At the top numero is %d" % numero
		numero.append(numero)
		
		numero = numero + 1
		print "Numero now:", numero
		print "At the bottom numero is %d" % numero

	print "The numero :"
	for nummer in numero:
		print nummer

loop()