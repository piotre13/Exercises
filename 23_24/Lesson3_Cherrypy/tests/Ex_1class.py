
import cherrypy

class StringRev():
	exposed = True
	def __init__(self):
		pass
	def GET (self, a, b, ):
		# if len(uri)>0:
		# 	string = uri[::-1]
		# 	string = str(string)
		# 	return string
		# if params!={}:
		# 	string = [v for v in params.values()]
		# 	string = str(string[::-1])
		# 	return string
		print(a)
		print(b)
		return 'helloworld'



if __name__ == '__main__':
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
		}
	}

	cherrypy.tree.mount(StringRev(), '/', conf)
	cherrypy.engine.start()
	cherrypy.engine.block()