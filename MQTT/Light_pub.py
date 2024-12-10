from MyMQTT import MyMQTT as client
import time

class Light_controller():
	def __init__(self, client_id, broker, port, topic):
		self.client = client(client_id,broker,port)
		self.client.start()
		self.topic = topic
		time.sleep(1)


	def send_message(self, cmd):
		self.client.myPublish(self.topic,cmd)


if __name__ == '__main__':
	client_id = 'controller'
	broker = "mqtt.eclipseprojects.io"
	port = 1883
	topic = 'IOT/Pietro/led'
	controller = Light_controller(client_id,broker,port, topic)

	while True:
		cmd = input('specify a command')
		controller.send_message(cmd)
