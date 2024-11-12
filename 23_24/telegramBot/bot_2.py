
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import time

class Bot:
	def __init__(self, token):
		self.bot = telepot.Bot(token)
		self.token = token
		callback_dict = {'chat':self.on_chat_message,
						 'callback_query':self.pippo}
		MessageLoop(self.bot,callback_dict).run_as_thread()


	def on_chat_message(self,msg):
		content_type, chat_type, chat_ID = telepot.glance(msg)
		cmd = msg ['text']
		date = msg ['date']

		if cmd == '/lights':
			keyboard = InlineKeyboardMarkup(inline_keyboard =[[InlineKeyboardButton(text='light1', callback_data='light1'),InlineKeyboardButton(text='light2', callback_data='light2'),InlineKeyboardButton(text='light3', callback_data='light3')]])
			self.bot.sendMessage(chat_ID, 'these are the lights: chose one', reply_markup=keyboard)


		else:
			self.bot.sendMessage(chat_ID, 'command not found!')


	def pippo(self,msg):
		query_id, ch_id, query = telepot.glance(msg, flavor='callback_query')
		print(query)
		if query.startswith('light'):
			keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='ON', callback_data='ON_light%s'%query)],[InlineKeyboardButton(text='OFF', callback_data='OFF_light_%s'%query)]])
			self.bot.sendMessage(ch_id,'ON or OFF light_%s'%query ,reply_markup=keyboard)

		elif query.startswith('ON'):
			#prepare the topi
			#publish
		pass


if __name__ == '__main__':

	token = '6917457682:AAFOvyebrA6V4Ev9UXIjQK6e0UXdSj5_zLc'
	bot = Bot(token)
	while True:
		time.sleep(1)

