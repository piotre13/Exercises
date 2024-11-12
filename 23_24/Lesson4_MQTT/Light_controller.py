from MyMQTT import MyMQTT
import time
import cherrypy

class Light_controller():
	exposed = True
	def __init__(self, client_id, broker, port, topic):
		self.client_mqtt = MyMQTT(client_id,broker,port)
		#self.client_mqtt.start()
		self.msg = {"bn":client_id,
					"e":[
						{"n": "command",
						 "u": None,
						 "t": 0,
						 "v": None},

					]}
		self.topic = topic

	def GET (self, *uri, **params):
		self.client_mqtt.start()

		if len(uri)!=0:
			self.msg['e'][0]['v'] = uri[0]
			self.msg['e'][0]['t'] = time.time()
			self.client_mqtt.myPublish(self.topic, self.msg)

		time.sleep(5)
		self.client_mqtt.stop()

		return 'command sent!'


	def run(self):
		print('you can write commands or stop by writing "q"')
		while True:
			cmd = input('type a command between ON or OFF or q')
			if cmd == 'q':
				break
			else:
				self.msg['e'][0]['v'] = cmd
				self.msg['e'][0]['t'] = time.time()
				self.client_mqtt.myPublish(self.topic, self.msg)

		self.client_mqtt.stop()
		return




if __name__ == '__main__':
	client_id = 'pippo233444'
	broker = 'mqtt.eclipseprojects.io'
	port = 1883
	topic = 'Iot/Pietro/led'
	controller = Light_controller(client_id, broker, port, topic)
	#controller.run()

	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
		}
	}

	cherrypy.tree.mount(controller, '/', conf)
	cherrypy.engine.start()
	cherrypy.engine.block()

