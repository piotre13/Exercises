import cherrypy
import json
class Echo(object):
	"""docstring for Reverser"""
	exposed=True
	def __init__(self):

		pass

	def PUT(self, **params):
		body=cherrypy.request.body.read()

		#json_body=json.loads(body.decode('utf-8'))
		json_body=json.loads(body)
		response="The keys are {}, and the values are {}".format([x for x in json_body.keys()],[x for x in json_body.values()])
		return response




if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tools.sessions.on':True
		}
	}		
	cherrypy.tree.mount(Echo(),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()