import cherrypy

class SimplePOST:
	exposed=True
	def __init__(self):
		pass

	def POST(self, *uri, **params):
		body=cherrypy.request.body.read()
		output=str(type(body))+"<br>"+str(body)

		return output

class FancyPOST:
	exposed=True
	def __init__(self):
		pass
	#using this function we can directly convert the body to a dictionary using cherrypy.request.json
	@cherrypy.tools.json_in()
	def POST(self, *uri, **params):
		data=cherrypy.request.json
		output=str(type(data))+"<br>"+str(data)
		return output

if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }

	cherrypy.server.socket_host = '172.21.173.1'
    cherrypy.tree.mount(SimplePOST(), '/simple', conf)
    cherrypy.tree.mount(FancyPOST(), '/fancy', conf)
    # this is needed if you want to have the custom error page
    # cherrypy.config.update({'error_page.400': error_page_400})
    cherrypy.engine.start()
    cherrypy.engine.block()

