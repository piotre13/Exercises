import requests
import json









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
			res = requests.get('http://172.21.173.1:8080/full')
			print(res.text)
		elif c == 's':
			name = input('Name:\n')
			surname = input('Surname\n')
			res = requests.get('http://127.0.0.1:8080/djdjwsksh?name=%s&surname=%s'%(name,surname))
			print(res.text)

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














res = requests.post('http://127.0.0.1:8080/', json={"name": "Pippo", "surname": "Pluto", "email": "pippo@"})






print(res)