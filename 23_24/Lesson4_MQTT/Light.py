from MyMQTT import MyMQTT
import time
import json

class Light():
	def __init__(self, client_id, broker, port,topic):
		self.client_mqtt = MyMQTT(client_id, broker, port, self)
		self.client_mqtt.start()
		self.client_mqtt.mySubscribe(topic)


	def notify(self, topic, msg):
		print('message received')
		msg = json.loads(msg)
		status = msg['e'][0]['v']
		print( 'the status of the light is %s and the command has been taken from %s' %(status, topic))

	def stop(self):
		self.client_mqtt.stop()

if __name__ == '__main__':
	client_id = 'pippo232'
	broker = 'mqtt.eclipseprojects.io'
	port = 1883
	topic = 'Iot/Pietro/led_23'
	light = Light(client_id, broker, port, topic)

	time_limit = 100000000000
	cnt =0
	while cnt<=time_limit:
		time.sleep(1)
		cnt+=1

	light.stop()