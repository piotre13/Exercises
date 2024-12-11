
from MyMQTT import MyMQTT as client
import time

class Building_sub():
	def __init__(self,client_id,broker, port, topic):
		self.client= client(client_id,broker, port,self)
		self.client.start()
		time.sleep(1)
		self.client.mySubscribe(topic)


	def notify (self,topic, payload):
		print(f'msg received on topic {topic}, with payload:{payload} ')


if __name__ == '__main__':
	client_id = 'pippo'
	broker = 'mqtt.eclipseprojects.io'
	port = 1883
	topic = 'ProjectIOT/1/+/0/0'
	client_bui = Building_sub(client_id, broker, port ,topic)


	while True:
		pass