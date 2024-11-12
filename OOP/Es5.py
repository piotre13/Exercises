import json


class Catalog():
	def __init__(self, file_path):
		self.path = file_path
		with open(file_path, 'r') as fp:
			self.data = json.load(fp)

		self.cnt = len(self.data['device_list'])

	def add_device(self, name, measure_type):
		tmp = {	"deviceID" :self.cnt,
				  "deviceName" :name,
				  "measureType" :measure_type
  				}
		self.data['device_list'].append(tmp)
		self.cnt+=1

	def update(self, dv_id, new_info):
		for device in self.data['device_list']:
			if device['deviceID'] == dv_id:
				for k, val in new_info.items():
					if k in device.keys():
						device[k] = val

	def delete(self):
		pass
	def read (self):
		pass

	def save(self):
		with open(self.path, 'w') as fp:
			json.dump(self.data, fp)


if __name__ == '__main__':
	catalog = Catalog('catalog.json')

	new_info = {"deviceName" :"DHT11",
      			"measureType" :["solar_radiation" ,"Humidity"],
				"ciao" :124
				}

	catalog.update(0,new_info)