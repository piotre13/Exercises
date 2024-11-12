import json


class Contact():
	def __init__(self, name, sur, em):
		self.name = name
		self.surname = sur
		self.email = em

	def __repr__(self):
		return f"'name':{self.name}, 'surname':{self.surname}, 'email':{self.email}"
	def info(self):
		return {"name":self.name, "surname":self.surname,"email":self.email}


class AddressBook():
	def __init__(self):
		self.file_path = '../OOP/Contacts.json'
		self.addresses = []
		with open(self.file_path, 'r') as fp:
			addresses = json.load(fp)

		for con in addresses:
			contact = Contact(con['name'],con['surname'],con['email'])
			self.addresses.append(contact)



	def create(self,name, surname, email):
		contact = Contact(name, surname, email)
		self.addresses.append(contact)

	def update(self, name, surname, new_info):
		for i in self.addresses:
			if name == i.name and surname == i.surname:
				i.name = new_info['name']
				i.surname = new_info['surname']
				i.email = new_info['email']

	def delete(self, name, surname):
		for i in range(len(self.addresses)):
			if name == self.addresses[i].name and surname == self.addresses[i]['surname']:
				self.addresses.pop(i)


	def read(self,name=None, surname=None):
		if name == None and surname == None:
			return [i for i in self.addresses]


		else:
			if name and surname:
				#show the single contact
				for i in self.addresses:
					if name == i.name and surname == i.surname:
						return i


			else:
				print(f"some info is missing: name = {name}, surname = {surname}")
				# warning


	def save(self):
		list_of_dict = []
		for con in self.addresses:
			list_of_dict.append(con.info())


		with open(self.file_path, 'w') as fp:
			json.dump(list_of_dict, fp)















if __name__ == '__main__':
	initial_friend = [{
		"name": "Cassio",
		"surname": "Zen",
		"email": "cassiozen@gmail.com",
	},

		{
			"name": "Dan",
			"surname": "Abramov",
			"mail": "gaearon@somewhere.com"
		}
	]
	file_path = 'addressbook.json'