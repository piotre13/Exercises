import json
import time

class Catalog:
	def __init__(self, file_path):
		self.file_path = file_path
		with open(file_path,'r') as fp:
			self.catalog = json.load(fp)
	def add_device(self, sens_id, sens_type, **kwargs):
		dev_dict = {
			"sens_id":sens_id,
			"sens_type": sens_type,
			"reg_ts": str(time.time())
		}
		if len(kwargs.keys())!=0:
			for k,v in kwargs.items():
				dev_dict[k]=v

		self.catalog['device_list'].append(dev_dict)

	def show_device(self,sens_id = None):
		if sens_id == None:
			print(self.catalog['device_list'])
			return
		else:
			for i in self.catalog['device_list']:
				if i['sens_id'] == sens_id:
					print(i)
					return


	def update_device (self):
		pass
	def delete_device(self):
		pass


if __name__ == '__main__':
	file_path = 'files/catalog.json'
	catalog = Catalog(file_path)
	print(catalog)

