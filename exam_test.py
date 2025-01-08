
import cherrypy


class exam:
	exposed= True
	def __init__(self):
		pass

	@cherrypy.tools.json_in
	def POST(self,*uri,**params):
		body= cherrypy.request.json

		if 'word' in body.keys() and 'list_of_words' in body.keys():
			if body['words'] in body['list_of_words']:
				i = 0
				index_found = None
				for word in body['list_of_words']:
					if word == body['word']:
						body['list_of_words'].pop(i)
						index_found = i
					i+=1
				if not index_found:
					return "not found!!!"
				else:
					return {'index': index_found, 'list': body['list_of_words']}

		else:
			return 'nothing wrong keys'



if __name__ == '__main__':
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True
		}
	}

	cherrypy.tree.mount(exam(), '/search', conf)
	cherrypy.engine.start()
	cherrypy.engine.block()