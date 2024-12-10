import cherrypy


class Webservice():
	exposed= True
	def GET(self,*uri, **params):
		empty_str =''
		for str in uri:
			empty_str+=f' {str}'
		return empty_str[::-1]

class Webservice2():
	exposed= True

	def GET(self,*uri, **params):
		empty_str=''
		for k, val in params.items():
			params[k] = params[k][::-1]
			empty_str+= f'{k} = {params[k]} \n'

		return empty_str

class Webservice3():
	exposed= True

	@cherrypy.tools.json_out()
	def GET(self,*uri, **params):
		for k, val in params.items():
			params[k] = params[k][::-1]

		return params


if __name__ == '__main__':
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True
		}
	}
	#cherrypy.quickstart(Webservice2(),'/string', conf)
	#cherrypy.tree.mount(Webservice2(), '/string', conf)
	cherrypy.tree.mount(Webservice3(), '/json', conf)
	cherrypy.engine.start()
	cherrypy.engine.block()
