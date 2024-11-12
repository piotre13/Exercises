import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import time
from MyMQTT import MyMQTT


class IcscBot():
	def __init__(self,token, client_id, broker, port, base_topic):
		self.token = token
		self.bot = telepot.Bot(self.token)
		self.callback_dict = {'chat':self.on_chat_message,
							  'callback_query': self.queries}
		self.client_mqtt = MyMQTT(client_id,broker,port)
		self.base_topic = base_topic
		self.generic_keyboard = InlineKeyboardMarkup(inline_keyboard =[[InlineKeyboardButton(text='SwitchON', callback_data='ON_light1')],[InlineKeyboardButton(text='SwitchOFF', callback_data='OFF_light1')]])


	def start(self):
		MessageLoop(self.bot,self.callback_dict).run_as_thread()
		#self.client_mqtt.start()

	def on_chat_message(self,msg):
		content_type, chat_type, chat_ID = telepot.glance(msg)
		cmd = msg['text']
		if cmd == '/light1':
			keyboard = InlineKeyboardMarkup(inline_keyboard =[[InlineKeyboardButton(text='SwitchON', callback_data='ON_light1')],[InlineKeyboardButton(text='SwitchOFF', callback_data='OFF_light1')]])
			self.bot.sendMessage(chat_ID, 'what do you want to do', reply_markup=keyboard)
		elif cmd == '/light2':
			keyboard = InlineKeyboardMarkup(
				inline_keyboard=[[InlineKeyboardButton(text='SwitchON', callback_data='ON_light2')],
								 [InlineKeyboardButton(text='SwitchOFF', callback_data='OFF_light2')]])
			self.bot.sendMessage(chat_ID, 'what do you want to do', reply_markup=keyboard)

		elif cmd == '/light3':
			keyboard = InlineKeyboardMarkup(
				inline_keyboard=[[InlineKeyboardButton(text='SwitchON', callback_data='ON_light3')],
								 [InlineKeyboardButton(text='SwitchOFF', callback_data='OFF_light3')]])
			self.bot.sendMessage(chat_ID, 'what do you want to do', reply_markup=keyboard)

		elif cmd == '/lights':
			keyboard = InlineKeyboardMarkup(
				inline_keyboard=[[InlineKeyboardButton(text='light 1', callback_data='light1')],
								 [InlineKeyboardButton(text='light2', callback_data='light2')], [InlineKeyboardButton(text='light3', callback_data='light3')]])
			self.bot.sendMessage(chat_ID, 'what do you want to do', reply_markup=keyboard)

		else:
			self.bot.sendMessage(chat_ID,'this command is not supported')

		print(cmd)


	def queries(self, msg):
		query_id, ch_id, query = telepot.glance(msg, flavor='callback_query')
		if query.startswith('ON'):
			light_id = query.split('_')[1]
			msg = {"cmd": 'ON'}
			topic = self.base_topic + light_id
			#self.client_mqtt.myPublish(topic,msg)
			print('light_switchedON')
		elif query.startswith('light'):
			keyboard = InlineKeyboardMarkup(inline_keyboard =[[InlineKeyboardButton(text='SwitchON', callback_data='ON_%s'%query)],[InlineKeyboardButton(text='SwitchOFF', callback_data='OFF_%s'%query)]])
			self.bot.sendMessage(ch_id, 'switch on or off %s'%query, reply_markup=keyboard)



		print(query)


if __name__ == '__main__':
	token = '6917457682:AAFOvyebrA6V4Ev9UXIjQK6e0UXdSj5_zLc'
	client_id = 'Pietro13'
	broker = 'mqtt.eclipseprojects.io'
	port = 1883
	base_topic = 'IOt_project/lights/'
	bot = IcscBot(token,client_id,broker,port,base_topic)
	bot.start()
	while True:
		time.sleep(1)


