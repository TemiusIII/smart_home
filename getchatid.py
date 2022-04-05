import telebot

bot = telebot.TeleBot("5214174938:AAHlcBsA1tZ73IeWjziSAFLJ5yWFJ2XT6n8")

@bot.message_handler(commands=['getchatid'])
def start_command(message):
    bot.send_message(message.chat.id, message.chat.id)

bot.polling()