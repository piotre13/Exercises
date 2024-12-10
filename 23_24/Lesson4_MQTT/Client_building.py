from MyMQTT import MyMQTT as client
import time

class BuildingClient():
	def __init__(self,client_id,broker,port, topic):
		self.client = client(client_id,broker,port, self)
		self.client.start()
		time.sleep(1)
		self.client.mySubscribe(topic)

	def notify(self,topic,payload):
		print(f"received message from topic {topic} with payload {payload}")


if __name__ == '__main__':
	client_id = 'pippo'
	broker = "mqtt.eclipseprojects.io"
	port = 1883
	topic= 'Iot_project/BUi100/+/1/#'
	client_building = BuildingClient(client_id, broker, port,topic)
	while True:
		time.sleep(1)
