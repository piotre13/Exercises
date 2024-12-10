import cherrypy
import json

class Webservice():
	exposed = True
	def __init__(self, path):
		with open(path,'r') as fp:
			self.catalog = json.load(fp)


	def GET(self,*uri,**params):
		if len(uri)>0:
			return self.catalog[uri[0]][uri[1]]
		pass

	def POST(self):
		pass




if __name__ == '__main__':
	path = 'catalog.json'
	class_instance = Webservice(path)
	catalog = {
		"catalog": {
				"device_list": [],
				"sensor_list": []
		}
		}

	cat_lev1 = catalog['catalog']
	cat_lev2 = cat_lev1['device_list']

	print('y')