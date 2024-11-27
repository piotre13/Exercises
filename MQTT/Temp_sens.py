import random
from MyMQTT import MyMQTT as client
import time

class Temperature_sensor():
	def __init__(self, client_id, broker, port, topic):
		self.client = client(client_id, broker, port)
		self.client.start()

		self.topic = topic
		self.msg = {
						"bn": client_id,
						"e": [
								{
								"n": "temperature",
								"u": "Cel",
								"t": None,
								"v":None
								} ]
						}
	def run(self, freq):

		while True:
			val = self.sense_value()
			self.msg['e'][0]['v'] = val
			self.msg['e'][0]['t'] = time.time()
			self.client.myPublish(self.topic, self.msg)
			print(val)
			time.sleep(freq)

	def sense_value(self):
		return random.randint(0,30)



if __name__ == '__main__':
	client_id = 'pippo'
	broker = "mqtt.eclipseprojects.io"
	port = 1883
	topic = 'house2/room1/temperature'
	temp = Temperature_sensor(client_id,broker,port, topic)

	temp.run(5)
