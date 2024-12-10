from MyMQTT import MyMQTT as client
import time
import json

class Controller():
	def __init__(self, client_id, broker,port,topic):
		self.client = client(client_id,broker,port,self)
		self.client.start()
		time.sleep(1)
		self.client.mySubscribe(topic)

	def notify(self,topic,payload):
		#payload = json.loads(payload)
		print(type(payload))
		print(f'topic {topic} with payload{payload}')
		pass





if __name__ == '__main__':
	client_id = 'xkxkxkxkx'
	broker = "mqtt.eclipseprojects.io"
	port = 1883
	topic = 'opendtu_solar_6314183758/112182839937/0/reactivepower'
	controller = Controller(client_id, broker,port, topic)

	while True:
		pass