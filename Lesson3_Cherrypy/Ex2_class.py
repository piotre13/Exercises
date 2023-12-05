import sys
sys.path.append('../')
from Lesson2_OOP.Ex3 import AddressBook
import cherrypy
import json

class Address_book_service():
	exposed=True
	def __init__(self,filename):
		self.addressbook = AddressBook(filename)

	def GET(self,*uri,**params):
		if len(uri)!=0:
			if uri[0] == 'show':
				contacts = self.addressbook.show()
				contacts = str(contacts)

				return contacts

			elif uri[0] == 'find':
				if params!={}:
					res = self.addressbook.find(params['surname'])
					return res

	@cherrypy.tools.json_in()
	def POST(self, *uri, **params):
		data = cherrypy.request.json
		if 'name' in data.keys() and 'surname' in data.keys():
			self.addressbook.add_contact(data['name'],data['surname'], data['mail'])
		print(data)


	@cherrypy.tools.json_in()
	def PUT(self, *uri, **params):
		if params != {}:
			name = params['name']
			surname = params['surname']
			new_data = cherrypy.request.json
			self.addressbook.update_contact(name, surname, new_data)


	def DELETE(self, *uri, **params):
		pass


if __name__ == '__main__':
	file_path = '../Lesson2_OOP/files/address_book.json'
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True
		}
	}

	cherrypy.tree.mount(Address_book_service(file_path), '/', conf)
	cherrypy.engine.start()
	cherrypy.engine.block()