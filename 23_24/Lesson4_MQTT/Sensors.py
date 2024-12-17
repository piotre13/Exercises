from MyMQTT import MyMQTT
import random
import time

class Temp_sensor():
	def __init__(self, client_id, broker, port,basic_topic,floor_id,room_id):
		self.client_mqtt = MyMQTT(client_id, broker, port)
		self.client_mqtt.start()
		self.topic = basic_topic+'/'+str(floor_id)+'/'+ str(room_id)+'/'+str(client_id)
		self.msg = {"bn": client_id,
					"e": [
						{"n": "temperature",
						 "u": '°C',
						 "t": 0,
						 "v": None},

					]}

	def run(self):
		value = random.randint(0,30)
		self.msg['e'][0]['v']=value
		self.msg['e'][0]['t']=time.time()
		self.client_mqtt.myPublish(self.topic, self.msg)
		print(f'published on topic: {self.topic} the following msg: {self.msg}')

	def stop(self):
		self.client_mqtt.stop()



class Hum_sensor():
	def __init__(self):
		pass
	def run(self):
		pass




if __name__ == '__main__':

	basic_topic = 'Iot_project/BUi100'
	broker = 'mqtt.eclipseprojects.io'
	port = 1883
	floor_ids = [1,2,3]
	room_ids = [1,2]

	sensor_instances =[]

	for i in floor_ids:
		for j in room_ids:
			client_id = 'sensorPietro_%s_%s'%(i,j)
			inst = Temp_sensor(client_id,broker, port,basic_topic,i,j)
			sensor_instances.append(inst)

	while True:
		for el in sensor_instances:
			el.run()
		

		time.sleep(2)


