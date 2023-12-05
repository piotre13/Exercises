import random
import time

class Sensor:
	def __init__(self, sens_id, sens_type, unit, timestamp, time_resolution):
		self.id = sens_id
		self.type = sens_type
		self.value = None
		self.unit = unit
		self.val_history = []
		self.ts = timestamp
		self.tr = time_resolution #in seconds
		self.max_val = 40
		self.min_val = 0
		self.stop = False

	def __repr__(self):
		return "sens: {}, val: {} [{}], timestamp: {}".format(self.id, self.value, self.unit, self.ts)

	def sense_data(self):
		self.value = random.randint(self.min_val, self.max_val)
		self.val_history.append(self.value)
		time.sleep(self.tr)
		self.ts += self.tr

	def write_data(self, file_path):
		with open(file_path, 'w') as fp:
			fp.write(self.val_history)


class TemperatureSensor(Sensor):
	def __init__(self, sens_id, timestamp, time_resolution, max_val, min_val):
		Sensor.__init__(self, sens_id, 'Temperature', '°C', timestamp, time_resolution)
		self.max_val = max_val
		self.min_val = min_val
		self.pippo = 10


	def run(self):
		while not self.stop:
			self.sense_data()
			print(f'the temperature is {self.value} at ts: {self.ts}')






if __name__ == '__main__':

	ts = int(time.time())
	temp_sens = TemperatureSensor('temp_01',ts, 5, 40, -10)
	temp_sens.run()