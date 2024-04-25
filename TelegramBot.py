import telebot
from telebot import types
import function
token='7117739871:AAGRujEaBFJOXSXW7NsVzSoF_k0npj6PS1w'
creatorCI = 5719001702
bot=telebot.TeleBot(token)

def menu(chat):
    global select
    select = "main"
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    fun1 = types.KeyboardButton('Найти молярную массу')
    fun2 = types.KeyboardButton('Найти массовую долю')
    markup.row(fun1,fun2)
    bot.send_message(chat,'Выберете в меню', reply_markup=markup)

@bot.message_handler(commands=['start'])
def start_message(message):
    global select
    select = "main"
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
    if message.text[0] == '/':
        if message.text == "/info":
            bot.send_message(message.chat.id,'Этот химический калькулятор был сделан без библиотек и готовых проектов')
            bot.send_message(message.chat.id,'при ошибках и о дополнениях email gatvit@mail.ru или /bug чтобы отправить')
        elif message.text == "/back":
            select = "main"
        elif message.text == '/bug':
            select = "bug"
            bot.send_message(message.chat.id, "отправте  сообщение с описанием бага или /back чтобы отменить")

    else:
        if message.text=="return":
            menu(message.chat.id)
        elif message.text == 'Найти молярную массу':
            select = "MolarMass"
            bot.send_message(message.chat.id,'Напишите формулу')

        elif select == "bug" and '/bug' not in message and'/main' not in message and '/back' not in message:
            bot.send_message(creatorCI, f"Сообщение: {message.text}")
            bot.send_message(message.chat.id,"Отправлено Спасибо")
            select = "menu "
bot.infinity_polling()
