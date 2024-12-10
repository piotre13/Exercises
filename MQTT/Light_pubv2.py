from MyMQTT import MyMQTT as client
import time
import cherrypy


class Light_controller():
	exposed = True

	def __init__(self, client_id, broker, port, topic):
		self.client = client(client_id,broker,port)
		self.client.start()
		self.topic = topic
		time.sleep(1)

	def GET(self,*uri,**params):
		if uri[0] == 'on' or uri[0] == 'off':
			self.send_message(uri[0])
			return f'you succesfully set the statut of light to {uri[0]}'
		else:
			return 'wrong command try it again'

	def send_message(self, cmd):
		self.client.myPublish(self.topic,cmd)


if __name__ == '__main__':
	client_id = 'controller'
	broker = "mqtt.eclipseprojects.io"
	port = 1883
	topic = 'IOT/Pietro/led'

	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True
		}
	}

	controller = Light_controller(client_id,broker,port, topic)
	cherrypy.tree.mount(controller,'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()
