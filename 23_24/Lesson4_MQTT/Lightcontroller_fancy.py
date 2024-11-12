from MyMQTT import MyMQTT
import time
import cherrypy
import os

class Light_controller():
	exposed = True
	def __init__(self, client_id, broker, port, topic):
		self.client_mqtt = MyMQTT(client_id,broker,port)
		self.client_mqtt.start()
		self.msg = {"bn":client_id,
					"e":[
						{"n": "command",
						 "u": None,
						 "t": 0,
						 "v": None},

					]}
		self.topic = topic

	def GET (self, *uri, **params):

		return open('index.html')

	def PUT (self, *uri, **params):
		self.msg['e'][0]['v'] = uri[0]
		self.msg['e'][0]['t'] = time.time()
		self.client_mqtt.myPublish(self.topic, self.msg)
		print('published')







if __name__ == '__main__':
	client_id = 'pippo233444'
	broker = 'mqtt.eclipseprojects.io'
	port = 1883
	topic = 'Iot/Pietro/led_23'
	controller = Light_controller(client_id, broker, port, topic)
	#controller.run()

	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
			'tools.staticdir.root': os.path.abspath(os.getcwd())
		},
		'/css': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': './css'
		}
	}

	cherrypy.tree.mount(controller, '/', conf)
	cherrypy.engine.start()
	cherrypy.engine.block()

