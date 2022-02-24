import telebot
from telebot import types
token = "5127759086:AAFlsA6H8GUrlSf0Y-iZJlodIxrZxgsLl-E"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/start","/help","/test", "/Anime")
#RUN
    bot.send_message(message.chat.id, 'Привет! Я заядлый анимешник и готов с тобой пообщаться) Введи команду help для списка моих команд)', reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'На данный момент я могу: \n/start - начать общение \n/test - какой жанр аниме вам подойдет \n/Anime - ссылка на Джитсу')

@bot.message_handler(commands=['test'])
def start_message(message):
 markup = telebot.types.InlineKeyboardMarkup()
 markup.add(telebot.types.InlineKeyboardButton(text='Динамические битвы между персонажами', callback_data=1))
 markup.add(telebot.types.InlineKeyboardButton(text='Романтика', callback_data=2))
 bot.send_message(message.chat.id, text="Что из этого вы больше предпочитаете?", reply_markup=markup)

@bot.message_handler(commands=['Anime'])
def start_message(message):
 bot.send_message(message.chat.id, 'https://jut.su/anime/')

@bot.message_handler(content_types=['text'])
def answer(message):
 if message.text.lower() == "привет":
  bot.send_message(message.chat.id, 'Приветствую!')
 if message.text == "Что делаешь?":
  bot.send_message(message.from_user.id, "Жожо смотрю")
 if message.text == 'Как дела?':
  bot.send_message(message.chat.id, 'Олл гуд май бро')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Приятного просмотра!')
    answer = ''
    if call.data == '1':
        answer = 'Вам подходит Сёнэн!'
    elif call.data == '2':
        answer = 'Вам подходит Сёдзё!'
    bot.send_message(call.message.chat.id, answer)
bot.polling(none_stop = True)