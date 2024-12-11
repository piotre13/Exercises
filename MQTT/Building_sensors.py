import random
from MyMQTT import MyMQTT as client
import time

class Sensor():
	def __init__(self, base_topic,id,room_id,floor_id,building_id,broker, port):
		self.sens_id = id
		self.topic = f"{base_topic}/{building_id}/{floor_id}/{room_id}/{id}"

		self.client = client(self.topic,broker, port)
		self.client.start()
		time.sleep(1)
		self.msg = {'bn': id,
					'e': [
						{'n': 'Temperature',
						 'u': 'C',
						 't': None,
						 'v': None}
					]}


	def run_loop(self, freq):
		while True:
			val = random.randint(-10,35)
			self.msg['e'][0]['v']=val
			self.msg['e'][0]['t']= time.time()
			self.client.myPublish(self.topic,self.msg)
			print(f'publish sensor:{self.sens_id}')
			time.sleep(freq)

	def run_one_shot(self):
		val = random.randint(-10,35)
		self.msg['e'][0]['v'] = val
		self.msg['e'][0]['t'] = time.time()
		print(f'publish on topic {self.topic}')
		self.client.myPublish(self.topic, self.msg)

if __name__ == '__main__':
	base_topic= 'ProjectIOT'
	broker = 'mqtt.eclipseprojects.io'
	port = 1883
	building_id = '1'
	floors_id = [0,1,2,3]
	rooms_id = [0,1]

	sensor_instances = []

	for fl in floors_id:
		for r in rooms_id:
			sens_id = '0'
			sensor_instances.append(Sensor(base_topic,sens_id,r,fl,building_id,broker,port))



	while True:
		for sens in sensor_instances:
			sens.run_one_shot()
		time.sleep(5)



