
import telepot
from telepot.loop import MessageLoop
import time
from MyMQTT import MyMQTT
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import json

class Mybot():
	def __init__(self, token, client_id, broker, port):
		self.token = token
		self.bot = telepot.Bot(self.token)
		self.callback_dict = {
			'chat': self.on_chat_message,
			'callback_query': self.callback_queries
		}
		self.client = MyMQTT(client_id, broker, port, self )
		self.chat_ids = []


	def start(self):
		MessageLoop(self.bot, self.callback_dict).run_as_thread()
		self.client.start()

	def on_chat_message(self,msg):
		content_type, chat_type, chat_ID  = telepot.glance(msg)
		if content_type == 'text':
			if msg['text'] == '/start':
				self.chat_ids.append(chat_ID)
			elif msg['text'] == '/subscribe':
				keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='full building', callback_data='full'),InlineKeyboardButton(text='floor', callback_data='floor')]])
				self.bot.sendMessage(chat_ID, 'tell me a proper topic:',reply_markup=keyboard)


		print(content_type)
		print(chat_type)
		print(chat_ID)
		pass

	def callback_queries(self,msg):
		query_id, ch_id, query = telepot.glance(msg, flavor='callback_query')

		if query == 'full':
			self.client.mySubscribe('ProjectIOT/1/#')
			self.bot.sendMessage(ch_id, 'succesfully subscribed')
		elif query == 'floor':
			floors =[1,2,3,4]
			keyboard = InlineKeyboardMarkup(inline_keyboard=[
				[InlineKeyboardButton(text=i, callback_data='floor_%s'%i) for i in floors]])
			self.bot.sendMessage(ch_id, 'which floor?', reply_markup= keyboard)
		elif query.startswith('floor_'):
			floor_number = query.split('_')[1]
			topic = 'ProjectIOT/1/%s/#'%floor_number
			self.client.mySubscribe(topic)


	def notify(self,topic, payload):
		payload = json.loads(payload)
		print(payload)
		for chat_id in self.chat_ids:
			pass
			self.bot.sendMessage(chat_id, f'topic:{topic} payoload:{payload}')
		pass





if __name__ == '__main__':
	token = '6917457682:AAFOvyebrA6V4Ev9UXIjQK6e0UXdSj5_zLc'
	broker = 'mqtt.eclipseprojects.io'
	port = 1883
	client_id = 'pippo13'
	mybot = Mybot(token, client_id, broker, port)
	mybot.start()
	while True:
		time.sleep(5)