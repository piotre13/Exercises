import requests
import json


res = requests.get('https://api.teleport.org/api/cities')
data = json.loads(res.text)
print(res)

class Client_cities():
	def __init__(self,base_url):
		self.base_url = base_url

	def get_city(self,city_name):
		url = self.base_url + 'cities/'
		all_cities = json.loads(requests.get(url).text)
		found=False
		for city in all_cities['_embedded']['city:search-results']:
			if city_name == city['matching_full_name'].split(',')[0]:
				res = json.loads(requests.get(city['_links']['city:item']['href']).text)
				return res
		return 'not found'

	def get_citysalaries(self, cityname):
		city_info = self.get_city(cityname)
		country_name = city_info['_links']['city:country']['name']
		url = self.base_url+'countries/'
		all_countries = json.loads(requests.get(url).text)
		for country in all_countries['_links']['country:items']:
			if country_name == country['name']:
				url = country['href']+'salaries/'
				res = json.loads(requests.get(url).text)

		max_sal=0
		max_job=None
		for job in res['salaries']:
			if job['salary_percentiles']['percentile_75'] > max_sal:
				max_sal = job['salary_percentiles']['percentile_75']
				max_job =  job['job']['id']

		return max_job





if __name__ == '__main__':
	base_url = 'https://api.teleport.org/api/'
	client=Client_cities(base_url)
	#info = client.get_city('Turin')
	salaries = client.get_citysalaries('Shanghai')