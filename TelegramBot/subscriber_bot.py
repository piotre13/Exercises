import json
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import time
from MyMQTT import MyMQTT


class Subs_bot:
	def __init__(self, token, client_id, broker, port, base_topic):
		self.token = token
		self.bot = telepot.Bot(self.token)
		self.callback_dict = {'chat': self.on_chat_message}
		self.client_mqtt = MyMQTT(client_id, broker, port, self)
		self.client_mqtt.start()
		time.sleep(1)
		self.base_topic = base_topic +'/#'
		self.client_mqtt.mySubscribe(self.base_topic)
		self.generic_keyboard = InlineKeyboardMarkup(
			inline_keyboard=[[InlineKeyboardButton(text='SwitchON', callback_data='ON_light1')],
							 [InlineKeyboardButton(text='SwitchOFF', callback_data='OFF_light1')]])

		self.chat_ids = []
	def start(self):
		MessageLoop(self.bot,self.callback_dict).run_as_thread()
		#self.client_mqtt.start()
	def notify(self,topic, payload):
		payload = json.loads(payload)
		print('notified!')
		for chat_id in self.chat_ids:
			msg = f'the sensed value is {payload["e"][0]["v"]}'
			self.bot.sendMessage(chat_id,msg)
			self.bot.sen

	def on_chat_message(self,msg):
		if msg['text'] == '/start':
			#register chat and use id
			content_type, chat_type, chat_ID = telepot.glance(msg)
			self.chat_ids.append(chat_ID)


if __name__ == '__main__':
	token = '8029768001:AAFmvlbcxCPLUPpJKhVwkSd9YtK-kqAcsSM'
	client_id = 'Pietro13'
	broker = 'mqtt.eclipseprojects.io'
	port = 1883
	base_topic = 'Iot_project/BUi100'
	bot = Subs_bot(token, client_id, broker, port, base_topic)
	bot.start()
	while True:
		time.sleep(1)
