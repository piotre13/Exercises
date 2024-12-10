from MyMQTT import MyMQTT as client
import time
import json

class Light_sub():
	def __init__(self, client_id, broker, port):
		self.client = client(client_id,broker,port,self)
		self.client.start()
		time.sleep(1)
		self.topics = []
		self.status = False

	def sub(self,topic):
		self.topics.append(topic)
		self.client.mySubscribe(topic)

	def notify(self,topic, payload):
		payload = json.loads(payload)
		print(payload)
		if payload == 'on':
			self.status = True
		elif payload == 'off':
			self.status = False
		else:
			print('wrong command!')
		print('the status is: %s' % self.status)


if __name__ == '__main__':
	client_id = 'pippo'
	broker = "mqtt.eclipseprojects.io"
	port = 1883
	light = Light_sub(client_id,broker,port)
	light.sub('IOT/Pietro/led')
	while True:
		time.sleep(1)