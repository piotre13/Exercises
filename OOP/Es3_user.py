from Es3 import AddressBook

Book = AddressBook()


while True:


	cmd = input("Press 's' tho show the list of contacts\n"
		  "Press 'n' to add a contact \n"
		  "Press 'u' to update a contact \n"
		  "Press 'd' to delete a contact \n"
		  "Press 'q' to save end exit\n")

	if cmd == 's':
		c = input('all or single? reply a or s\n')
		#dosomething
		if c == 'a':
			print(Book.read())
		elif c == 's':
			name = input('Name:\n')
			surname = input('Surname\n')
			print(Book.read(name, surname))

	elif cmd == 'n':
		name = input('Name:\n')
		surname = input('Surname\n')
		email = input('email\n')
		Book.create(name,surname,email)


	elif cmd == 'd':

		pass
	elif cmd == 'q':
		Book.save()

		break
	else:
		print('wrong command!')

