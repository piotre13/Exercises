import json
import requests
class Client(object):
	def __init__(self):
		self.baseDict={'E':'EUR','U':'USD','P':'GBP'}

	def handler(self,command):
		if command=='latest':
			self.getLatest()
		if command=='history':
			self.getHistory()

	def getLatest(self):
		base=self.baseDict[str(input('Which base currency you want:\nE:Euro\nU:USD\nP:GBP\n'))]
		r=requests.get('https://api.exchangerate.host/latest?base={}'.format(base))
		print (json.dumps(r.json(),indent=4))
		
	def getHistory(self):
		x=input('Type D for a day and I for and interval\n')
		if x=='D':
			year=input('Write the year\n')
			month=input('Write the month\n')
			day=input('Write the day\n')
			r=requests.get('https://api.exchangerate.host/{}-{}-{}'.format(year,month,day))
			print (json.dumps(r.json(),indent=4))
		if x=='I':
			s_year=input('Write the year for the start\n')
			s_month=input('Write the month for the start\n')
			s_day=input('Write the day for the start\n')
			e_year=input('Write the year for the end\n')
			e_month=input('Write the month for the end\n')
			e_day=input('Write the day for the end\n')
			r=requests.get('https://api.exchangerate.host/timeseries?start_date={}-{}-{}&end_date={}-{}-{}'.format(s_year,s_month,s_day,e_year,e_month,e_day))
			print (json.dumps(r.json(),indent=4))
		
		
def main():
	c=Client()
	while True:
		command=input('Available command:\nlatest:latest change rate\nhistory: historic exchange rates\nquit:exit\n')
		if command=='quit':
			break
		elif command=='latest' or command=='history':
			c.handler(command)
		else:
			print('Wrong command')
	
if __name__=='__main__':
	main()