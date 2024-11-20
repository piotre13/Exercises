import requests



class DanishInfo():
	def __init__(self):
		pass

	def data_request(self, duration):
		tot_number_rows = 12 * 24 * duration * 2
		res = requests.get(f'https://api.energidataservice.dk/dataset/ElectricityProdex5MinRealtime?limit={tot_number_rows}')
		data = res.json()
		return data


	def tot_solar_timeslot(self, duration):
		data = self.data_request(duration)
		tot_solar = 0
		for rec in data['records']:
			tot_solar+= rec['SolarPower']

		print(f'total solar power of the last {duration} days is : {tot_solar} MW')

	def  biggest_importer(self,duration):
		data = self.data_request(duration)
		print('toto')
		country_dict = {k.split('Exchange')[-1]:0 for k in data['records'][0].keys() if k.startswith('Exchange')}
		for rec in data['records']:
			for country in country_dict.keys():
				key = 'Exchange'+country
				try:
					country_dict[country]+= rec[key]
				except:
					pass



		print('wathe')







if __name__ == '__main__':
	ob = DanishInfo()
	ob.tot_solar_timeslot(1)
	ob.biggest_importer(10)
