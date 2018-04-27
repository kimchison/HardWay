def loop():
	numero = []
	numb = raw_input("PLease enter starting number: ")
	numero.append(numb)

	while numero < 6:
		print "At the top numero is %d" % numero
		numero.append(numero)
		
		numero = numero + 1
		print "Numero now:", numero
		print "At the bottom numero is %d" % numero

	print "The numero :"
	for nummer in numero:
		print nummer

loop()