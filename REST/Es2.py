import cherrypy
from Addressbook import AddressBook




class Addresses():
	exposed= True
	def __init__(self):
		self.book = AddressBook()

	@cherrypy.tools.json_out()
	def GET(self, *uri, **params):

		if uri[0] == 'full':
			full = []
			full_list = self.book.read()
			for i in full_list:
				full.append(i.info())

			return full
		else:
			if params and 'name' in params.keys() and 'surname' in params.keys():
				return self.book.read(params['name'], params['surname']).info()

	@cherrypy.tools.json_in()
	def POST(self, *uri, **params):
		body = cherrypy.request.json
		self.book.create(body['name'], body['surname'],body['email'])
		print(str(body))

	def DELETE(self, *uri, **params):
		self.book.delete()
		pass


if __name__ == '__main__':
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True
		}
	}

	cherrypy.server.socket_host ='172.21.173.1'
	cherrypy.server.socket_port= 8080
	cherrypy.tree.mount(Addresses(), '/', conf)
	cherrypy.engine.start()
	cherrypy.engine.block()


