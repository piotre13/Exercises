import requests






class Client:
	def __init__(self):
		pass

	def show(self, host= 'localhost', port=8080):

		url =f'http://{host}:{port}/show'
		res = requests.get(url)
		print(res.text)

	def find (self,host, port, name, surname ):
		url =f'http://{host}:{port}/find?name={name}&surname={surname}'
		res = requests.get(url)
		print(res.text)

if __name__ == '__main__':
