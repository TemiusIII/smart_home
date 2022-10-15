import telebot
import find
bot = telebot.TeleBot('2022609617:AAERjqknUxED8jUks-Xuy0akUuYo0RkDX6o')

@bot.message_handler(commands=["start"])
def start_command(m, res=False):
    bot.send_message(m.chat.id, 'Пришли мне номер телефона, я его пробью.')

@bot.message_handler(commands=["find"])
def get_number(message):
     bot.send_message(message.chat.id, 'Напиши номер или email:')
     bot.register_next_step_handler(message, find_number)
def find_number(message):
    number = message.text.replace(' ','').replace("+",'')
    id = bot.send_message(message.chat.id, 'Начинаю поиск...').message_id
    result = find.find_gemotest(number)
    if result:
        bot.delete_message(id)
        bot.send_message(message.chat.id, f"Результат:"
                                          f"\nФИО: {result.get('surname'), result.get('name'), result.get('middle_name')}"
                                          f"\nДата рождения: {result.get('birthday')}"
                                          f"\nПол: {result.get('sex')}"
                                          f"\nАдрес: {result.get('address')}"
                                          f"\nEmail: {result.get('email')}"
                                          f"\nНомер телефона: {result.get('phone')}")
    else:
        bot.delete_message(id)
        bot.send_message(message.chat.id, "Увы, ничего не найдено(")
bot.polling(none_stop=True, interval=0)