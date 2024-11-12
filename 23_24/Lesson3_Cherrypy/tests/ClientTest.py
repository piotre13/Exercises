import requests
import json
# Create a new resource
#response = requests.post('localhost/8080', data = {'key':'value'})

# Update an existing resource
#body = json.dumps({'key':'value'})
#r = requests.put('http://127.0.0.1:8080/', data = body)

#print(r)
#print(r.text)

class ClientTest():
	def __init__(self):
		print('this is a REST Client')
		
		
	def get (self, uri, params):
		r = requests.get(uri, params=params)
		return f'''
		response code: {r},\n
		response content: {r.text}\n  
		'''
	def post (self, uri, body):
		r= requests.post(uri, data=body)
		return r

	def put (self, uri, body):
		#remember in this case always specify keys with double quotes in the body
		body = json.dumps(json.loads(body)) # this is necessary because original body is a string and we cannot dump a string
		r = requests.put(uri,data=body)
		return f'''
		response code: {r},\n
		response content: {r.text}\n  
		''' #NB text work only with the right encoding

if __name__ == '__main__':
	Client = ClientTest()
	uri = input('Please specify the URI of a web service you want to interact with:\n')
	while True:
		helpMessage="Type 'GET' to perform a GET request\nType 'PUT' to perfrom a PUT request\nType exit to quit the Client"
		print(helpMessage)
		command=input()
		if command=='GET':
			params = input ('Insert the params in a dict like form:\n')
			response = Client.get(uri,params)
			print(response)
		elif command=='PUT':
			body = input ('Insert the body in a dict like form:\n')
			response = Client.put(uri, body)
			print(response)
		elif command ==  'POST':
			body=input('insert the body:\n')
			response=Client.post(uri, body)
		elif command=='exit':
			print('Bye Bye!')
			break
			
		else:
			print('Command not available')


		