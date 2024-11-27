from MyMQTT import MyMQTT as client
import time

class Controller():
	def __init__(self, client_id, broker,port,topic):
		self.client = client(client_id,broker,port,self)
		self.client.start()
		time.sleep(1)
		self.client.mySubscribe(topic)

	def notify(self,topic,payload):
		print(f'topic {topic} with payload{payload}')
		pass





if __name__ == '__main__':
	client_id = 'pippo2'
	broker = "mqtt.eclipseprojects.io"
	port = 1883
	topic = 'house2/room1/temperature'
	controller = Controller(client_id, broker,port, topic)

	while True:
		pass