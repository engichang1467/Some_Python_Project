
def Cashier2():

	think = True

	while(think):

		fileR = open("fruit-code.txt", "r")
		line = fileR.readlines()

    		# Ask user for input
		n = input("Write in the code (type Q to quit): ")

    		# this will split the list from newline (\n)
		for l in line:
			a = l.split(" ")  # and split it again from space
      
      			# This will search the number that the user input
			if (n == a[0]):
      
        			# As it found the fruit that match the number, it'll display the name of the fruit
				print("\n{}".format(a[1]))
		
    		# This will allow the user to leave the program
		if n == "q":
			think = False
			print("\nGood bye\n")		

		fileR.close()


Cashier2()
