import wikipedia
import telebot



bot = telebot.TeleBot('1783453117:AAEISu0jBk4zmohq49_9zAGTjD5QaaedAvg')
language = 'uk'
@bot.message_handler(commands=['start'])
def handle_start(message):




    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(text="English", callback_data='smth'))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Українська", callback_data='smth1'))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Русский", callback_data='smth2'))

    a = bot.send_message(message.chat.id, 'Введіть будь ласка мову на якій будете шукати', reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global language
    if call.data == 'smth':
        language = 'en'
        bot.send_message(call.message.chat.id, 'Language is success switched, write your request!')
    elif call.data == 'smth1':
        language = 'uk'
        bot.send_message(call.message.chat.id, 'Мову успішно переключено, введіть Ваш запит!')
    elif call.data == 'smth2':
        language = 'ru'
        bot.send_message(call.message.chat.id, 'Язык успешно переключен, введите Ваш запрос!')
    wikipedia.set_lang(language)



@bot.message_handler(content_types=['text'])
def messages(message):
    if language == 'uk':
        r = f'https://uk.wikipedia.org/wiki/{message.text}'
        bot.reply_to(message, f'{r}')
    elif language == 'ru':
        r = f'https://ru.wikipedia.org/wiki/{message.text}'
        bot.reply_to(message, f'{r}')
    elif language == 'en':
        r = f'https://en.wikipedia.org/wiki/{message.text}'
        bot.reply_to(message, f'{r}')

bot.polling(none_stop=True)


















