import telebot
from telebot import types
import function
token='7117739871:AAGRujEaBFJOXSXW7NsVzSoF_k0npj6PS1w'
creatorCI = 5719001702
bot=telebot.TeleBot(token)
select = {}
dat = {}
def menu(chat):
	global select
	select[chat] = "main"
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

	fun1 = types.KeyboardButton('Найти молярную массу')
	fun2 = types.KeyboardButton('Найти массовую долю')
	markup.row(fun1,fun2)
	bot.send_message(chat,'Выберете в меню', reply_markup=markup)

@bot.message_handler(commands=['start'])
def start_message(message):
	global select
	select[message.chat.id] = "main"
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton('Начать', callback_data= "return"))
	bot.send_message(message.chat.id,'Добро пожаловать в Химический калькулятор')
	bot.send_message(message.chat.id,'Используя /help можно узнать про использование')
	bot.send_message(message.chat.id,'Используя /info можно узнать про сам калькулятор',reply_markup=markup)

@bot.message_handler(commands=['return'])
def button_message(message):
	menu(message.chat.id)

@bot.callback_query_handler(func=lambda callback: True)
def callback(calback):
	if calback.data == 'return':
		menu(calback.message.chat.id)


@bot.message_handler(content_types='text')
def message_reply(message):
	print(message.text)
	if str(message.text).startswith('/'):
		if message.text == "/info":
			bot.send_message(message.chat.id,'Этот химический калькулятор был сделан без библиотек и готовых проектов')
			bot.send_message(message.chat.id,'при ошибках и о дополнениях email gatvit@mail.ru или /bug чтобы отправить')
		elif message.text == "/back":
			select[message.chat.id] = "main"
		elif message.text == '/bug':
			select[message.chat.id] = "bug"
			bot.send_message(message.chat.id, "отправте  сообщение с описанием бага или /back чтобы отменить")

	else:
		if message.text=="return":
			menu(message.chat.id)
		elif message.text == 'Найти молярную массу':
			select[message.chat.id] = "MolarMass"
			bot.send_message(message.chat.id,'Напишите формулу')
		elif message.text == 'Найти массовую долю':
			select[message.chat.id] = "PercentageByMass1"
			bot.send_message(message.chat.id,'Напишите формулу:')
		elif select.get(message.chat.id,'main') == "MolarMass":
			bot.reply_to(message, f"Молярная масса: {function.FindMolMass(message.text)}")
		elif select.get(message.chat.id,'main') == "PercentageByMass1":
			bot.reply_to(message, "Содержание:")
			dat[message.chat.id]=message.text
			select[message.chat.id]= "PercentageByMass2"
		elif select.get(message.chat.id,'main') == "PercentageByMass2":
			print(dat[message.chat.id])
			print(message.text)
			bot.reply_to(message, f": {function.PercentageByMass(dat[message.chat.id],message.text)}")
		elif select.get(message.chat.id,'main') == "bug":
			bot.send_message(creatorCI, f"Сообщение через bug: {message.text}")
			bot.send_message(message.chat.id,"Отправлено Спасибо")
			select[message.chat.id] = "menu "
bot.infinity_polling()