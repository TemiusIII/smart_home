import os
import threading
import datetime
import json
import random
import re
import urllib.parse
import urllib.request
import webbrowser
from statistics import mean
from googlesearch import search
import keyboard
import osascript
import pyautogui
from termcolor import colored
import pyttsx3 as pyttsx3
import requests
import serial.tools.list_ports
import speech_recognition as sr
import telebot
import time
import pyngrok
from PIL import Image
from bs4 import BeautifulSoup
from googlesearch import search
from playsound import playsound
from youtube_search import YoutubeSearch
import asyncio


def SaveUrSelf():
    f = open("/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/main.py", "rb")
    bot.send_document(1124242654, f)
    urtts('успешно сохранился')
    print("Успешно сохранился!")
    bot.polling(none_stop=False)


bot = telebot.TeleBot("5292311634:AAHpunJZpF02Ze9BMoDNzTxWuSbnOqW0s6A")
engine = pyttsx3.init()
name = 'Сашa'
said_name = False
name_list = ['тёма', 'сема', 'тём', 'сем', 'сём', 'тем', 'тема', 'артём', 'чем']

jokes = [
    "сидит чукча, ругает жену стуча кулаком по столу. Жена спрашиает: кто в дверь стучит, пойду открою. Чукча кричит: СТОЙ, САМ ОТКРОЮ!!!",
    "Будит как-то мама Гитлера, а он отмахиваеться. Мне ко второй",
    "Каким будет суп: рыбным или мясным, если сварить русалку?",
    "Знаете что будет если все люди встанут по экватору в цепочку? Половина утонет",
    "Штирлиц всю ночь топил камин, на утро камин утонул",
    "Бабушка переходила дорогу не на тот свет, а попала на тот",
    "Колобок повесился",
    "Негр закрыл окна в машине, он думал что воняет с улицы",
    "из африки привезли фрукты , на них было написано не тронуто человеком",
    "Негр попал в нефть, кричал 2 часа но его не увидели"]


def urtts(text, lang='ru'):
    text = text.replace('кг', 'килограмм').replace("м³", 'метр кубический').replace('км', 'километр').replace("/",
                                                                                                              ' на ').replace(
        'чел/', 'человека на').replace('²', ' квадратный').replace("³", ' кубический').replace("млн", 'миллионов')
    engine.setProperty('voice', "com.apple.speech.synthesis.voice.yuri")
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    # my_thread = threading.Thread(
    #     target=say, args=(text,'ru',))
    # my_thread.start()


debug = True
# config = json.load(open('../../MineIsTop/config_undecoded.json', 'r', encoding='utf-8'))
#
# if debug:
#     # x = input('Do you want to change your port?(y/n)')
#     x = 1
#     if x == 'y':
#         print(*serial.tools.list_ports.comports())
#         new_port = input('\nChoose your port\n')
#         config['port'] = new_port
#         write_file = open('../../MineIsTop/config.json', 'w')
#         json.dump(config, write_file)
#         write_file.close()

# ArduinoUnoSerial = serial.Serial(config['port'], 9600)
r = sr.Recognizer()

command_performed = False

# commands = config['commands']

# if debug:
#     x = input('Do you want to manually write commands to you Com port?(y/n)\n')
#     if x == 'y':
#         print('type \'exit1337\' to exit')
#         while x != 'exit1337':
#             x = input()
#             ArduinoUnoSerial.write((x + '\r').encode('utf-8'))
#             print('Command was wrote')
if debug:
    print('Main part begins')
while 1:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.001)
        audiobmv = r.listen(source)
        try:

            text = r.recognize_google(audiobmv, language='ru-ru')
            text82374 = text
            if debug:
                print(text)
            text = str(text).lower()
            for i in name_list:
                if i == text:
                    a = random.randint(1, 8)
                    if a == 1:
                        urtts("ты что-то хотел спросить?")
                    if a == 2:
                        urtts("Да, " + str(name))
                    if a == 3:
                        urtts("Спрашивай " + str(name) + ", не стесняйся!")
                    if a == 4:
                        urtts("Внимательно тебя подслушиваю...")
                    if a == 5:
                        urtts("привет " + str(name))
                    if a == 6:
                        urtts("привет " + str(name))
                    if a == 7:
                        urtts("здраствуй " + str(name))
                    if a == 8:
                        urtts("привет " + str(name))
                    command_performed = True
                    said_name = True
                for i in name_list:
                    if i in text:
                        said_name = True
                if said_name == True:
                    if len(text) == 1:
                        if text[0] in name_list:
                            a = random.randint(1, 8)
                            if a == 1:
                                urtts("ты что-то хотел спросить?")
                            if a == 2:
                                urtts("Да " + str(name))
                            if a == 3:
                                urtts("Спрашивай " + str(name) + ", не стесняйся!")
                            if a == 4:
                                urtts("Внимательно тебя подслушиваю...")
                            if a == 5:
                                urtts("привет " + str(name))
                            if a == 6:
                                urtts("привет " + str(name))
                            if a == 7:
                                urtts("здраствуй " + str(name))
                            if a == 8:
                                urtts("приветствую " + str(name))
                            text = ''
                            command_performed = True
                    if "крутой" in text or "круто" in text:
                        urtts("но не круче тебя, " + str(name))
                        text = ''
                        command_performed = True
                    if "поговорим" in text and "о" in text and "чём" in text:
                        urtts("давайте о животных")
                        time.sleep(2)
                        urtts("начнем с вас")
                        text = ''
                        command_performed = True
                    if "смешно" in text or "смешной" in text:
                        urtts("Но не смешнее твоих шуток. " + name)
                        text = ''
                        command_performed = True
                    if "сделай" in text:
                        if "потише" in text or "тише" in text:
                            result = int(str(osascript.osascript('get volume settings')).split(',')[1].replace(
                                " 'output volume:", '')) // 2
                            osascript.osascript("set volume output volume " + str(result))
                            urtts("как скажешь")
                        elif 'погромче' in text or "громче" in text and not 'намого громче' in str(text).replace("', '",
                                                                                                                 ' '):
                            result = int(str(osascript.osascript('get volume settings')).split(',')[1].replace(
                                " 'output volume:", ''))
                            if result > 95:
                                urtts("громче нèкуда")
                            else:
                                osascript.osascript("set volume output volume " + str(result + 10))
                        elif 'намого громче' in str(text).replace("', '", ' ') or "сильно громче" in str(text).replace(
                                "', '", ' '):
                            result = int(str(osascript.osascript('get volume settings')).split(',')[1].replace(
                                " 'output volume:", ''))
                            if result > 95:
                                urtts("громче нèкуда")
                            else:
                                osascript.osascript("set volume output volume " + str(result + 40))
                        text = ''
                        command_performed = True

                    if "следующий" in text:
                        if "слайд" in text:
                            keyboard.press("right")

                    if "спасибо" in text:
                        a = random.randint(1, 3)
                        if a == 1:
                            urtts("всегда пожалуйста")
                        if a == 2:
                            urtts("незашто")
                        if a == 3:
                            urtts("обращайтесь")
                        text = ''
                        command_performed = True
                    if 'привет' in text or 'здравствуй' in text:
                        for tems_name in name_list:
                            for word in text:
                                if word == tems_name:
                                    a = random.randint(1, 4)
                                    if a == 1:
                                        urtts("привет " + str(name))
                                    if a == 2:
                                        urtts("здраствуй " + str(name))
                                    if a == 3:
                                        urtts("приветствую " + str(name))
                                    if a == 4:
                                        urtts("И тебе того-же!")
                                    text = ''
                                    command_performed = True
                    if "тупой" in text or "дебил" in text:
                        urtts("но не такой тупой как ты!, " + name)
                        text = ''
                        command_performed = True
                    if "спокойной ночи" in text:
                        urtts("Сладких снов!")
                        text = ''
                        command_performed = True
                    if "'пока'" in str(text):
                        time_now = str(datetime.datetime.now().time()).split(".")[0]
                        if int(time_now.split(':')[0]) >= 22:
                            urtts("СПАТЬ ИДИ!")
                            said_name = False
                        else:
                            a = random.randint(1, 8)
                            if a == 1:
                                urtts("Хорошо, пока!")
                            elif a == 2:
                                urtts("Окей, пока!")
                            elif a == 3:
                                urtts("Давай")
                            elif a == 4:
                                urtts("До свидания!")
                            elif a == 5:
                                urtts("И тебе того-же!")
                            elif a == 6:
                                urtts("До скорой встречи!")
                            elif a == 7:
                                urtts("До скорого!")
                            elif a == 8:
                                urtts("Было приятно пообщаться")
                            said_name = False
                        command_performed = True
                    text = str(text).split()
                    cter = 0
                    if 'погода' in text or 'погоду' in text:
                        urltosearch = "https://primpogoda.ru/weather/moskva/.today"
                        html = requests.get(urltosearch).text
                        soup = BeautifulSoup(html, 'html.parser')
                        find_text = "Вероятность осадков " + str(
                            soup.find('tr', {'class': 'precipitation divider tip-right'}).get_text().replace("\n",
                                                                                                             '').replace(
                                "%", "").replace("Вероятность осадков ", '').split())
                        print(find_text)
                        command_performed = True
                    if "лох" in text:
                        urtts("мне обидно")
                        command_performed = True
                    # if "сколько время" in str(text).replace("', '", ' ') or 'сколько времени' in str(text).replace("', '", ' ') or "который час" in str(text).replace("', '", ' '):
                    #     time_now = str(datetime.datetime.now().time()).split(".")[0]
                    #     a = random.randint(1, 2)
                    #     if a == 1:
                    #         urtts("сейчас " + time_now)
                    #     elif a == 2:
                    #         urtts(time_now)
                    # if int(time_now.split(':')[0]) > 21:
                    #         urtts("ПОРА СПАТЬ!!!")
                    for i in range(len(text)):
                        if "запусти" == text[i]:
                            command_performed = True
                            from deep_translator import GoogleTranslator

                            to_translate = text[i + 1]
                            translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
                            print(translated)
                            os.system("open -a " + translated)

                        if text[i] == 'загугли':
                            new_text = []
                            for el in text:
                                new_text.append(urllib.parse.quote(el, safe=''))
                            name_of_something = str(new_text[i + 1:]).replace("['", '').replace("', '", ' ').replace(
                                "']", "").replace("Тёма", '').replace(' ', '+')
                            urtts('гуглю...')
                            print(name_of_something)
                            str_to_google = f'https://www.google.com/search?q=' + name_of_something
                            webbrowser.open(str_to_google)
                            command_performed = True

                        if text[i] == 'закрой':
                            print(1)
                            if 'вклад' in str(text):
                                print(2)
                                try:
                                    a = int(text[i + 1])
                                    for i in range(a):
                                        keyboard.press('cmd')
                                        keyboard.press("w")
                                        keyboard.release("cmd")
                                        keyboard.release("w")
                                except:
                                    keyboard.press('cmd')
                                    keyboard.press("w")
                                    keyboard.release("cmd")
                                    keyboard.release("w")
                                urtts('Сделал')
                            text = ''
                            command_performed = True
                        if 'сохранись' in text or 'сохранить' in text:
                            urtts('сохраняюсь')
                            SaveUrSelf()
                            command_performed = True
                        if text[i] == 'зови':
                            if text[i + 1] == 'меня':
                                urtts(
                                    "Хорошо, " + name + '!.... ' + 'АХАХАХАХАХАХХАХА..... ' + "А по мОему смешно)... " + 'Ладно, ' + "Теперь ты " + ' '.join(
                                        text[i + 2:]))
                                name = ' '.join(text[i + 2:])
                                command_performed = True
                        if "с" == text[i] and "интересно" in text and "тобой" in text:
                            urtts("с вами тоже")
                            command_performed = True
                        if "как" == text[i] and "дела" == text[i + 1] or "как" == text[i] and "жизнь" == text[i + 1]:
                            urtts("с вами всегда хорошо")
                            command_performed = True
                        # if "меня" == text[i] and not 'как' in text:
                        #     if "зовут" in text[i+1]:
                        #         name1 = name
                        #         name = ' '.join(text[i + 2:])
                        #         if name != "":
                        #             urtts('хорошо, ' + name + "!")
                        #         else:
                        #             name = name1
                        #         command_performed = True
                        else:
                            # print(1)
                            if "зовут" in text and "как" in text and "мен" in text:
                                urtts(name)
                                text = ''
                                command_performed = True
                        if text[i] == 'открой':
                            cter = i + 1
                            name_of_something = str(text[i + 1:]).replace("['", '').replace("', '", ' ').replace("']",
                                                                                                                 "").replace(
                                "Тёма", '')
                            print("после i: " + name_of_something)

                            urtts("открываю " + str(name_of_something))
                            srch = ''.join(search(name_of_something, num_results=0))
                            print(srch)
                            webbrowser.open(str(srch).split("//")[0] + str(srch).split("//")[1])
                            command_performed = True
                        if "установи громкость на" in str(text).replace("', '",
                                                                        ' ') or "установить громкость на" in str(
                            text).replace("', '", ' ') or "поставь громкость на" in str(text).replace("', '", ' '):
                            volume_mod = int(text[len(text) - 1]) / 100
                            volume = (volume_mod * 100) + ((1 - volume_mod) * 19)
                            osascript.osascript("set volume output volume " + str(int(text[len(text) - 1])))
                            urtts("должно быть лучше")
                            text = ''
                            command_performed = True
                        if text[i] == 'заткнись':
                            urtts('сам заткнись')
                            said_name = False
                            command_performed = True
                        if '*' in str(text):
                            urtts("не надо пожалуйста говорить плохие слова")
                            text = ''
                            command_performed = True
                        if 'алиса' in str(text) and "siri" in str(text).lower():
                            urtts(
                                "У них меньше чем у меня приемуществ, и я единственный мальчик, максимально конфиденциальный")
                            text = ''
                            command_performed = True
                        if 'алиса' in str(text) and not "сири" in str(text) or "сири" in str(
                                text) and not 'алиса' in str(text):
                            urtts(
                                "У нее меньше чем у меня приемуществ, и я единственный мальчик, максимально конфиденциальный")
                            text = ''
                            command_performed = True
                        if "диктую" in text[i]:
                            print(text[i + 1])
                            urtts('говори')
                            aud = r.record(source, duration=int(text[i + 1]))
                            text_to_write = r.recognize_google(aud, language='ru-ru')
                            print('пишу: ' + str(str(text_to_write).split()))
                            for texxxxt in str(text_to_write).split():
                                keyboard.write(texxxxt)
                                keyboard.write(" ")
                                time.sleep(0.01)
                            text = ''
                            urtts('написал')
                            command_performed = True
                        if 'сказ' in text[i] or 'скаж' in text[i]:
                            if 'шутк' in text[i + 1] or "анекд" in text[i + 1]:
                                print(1)
                                a = random.randint(0, len(jokes) - 1)
                                urtts(jokes[a])
                                text = ''
                                command_performed = True
                        # if "путин" == text[i]:
                        # text[i+1] ==

                        if text[i] == 'что' or text[i] == 'кто':
                            if text[i + 1] == 'такое' or text[i + 1] == 'такая' or text[i + 1] == 'такой':
                                if len(text[i + 1:]) > 2:
                                    try:
                                        asking = str(text[i + 2:]).replace("['", '').replace("', '", '_').replace("']",
                                                                                                                  '')
                                        urtts(asking.replace("_", " "))
                                        html = requests.get(f'https://ru.wiktionary.org/wiki/{asking}').text
                                        soup = BeautifulSoup(html, 'html.parser')
                                        find_text = soup.find('ol').get_text()
                                        urtts(str(find_text.split('◆')[0]))
                                        print(str(find_text.split('◆')[0]))
                                        text = ''
                                    except:
                                        try:
                                            asking = str(text[i + 2:]).replace("['", '').replace("', '", '_').replace(
                                                "']", '')
                                            link_of_srch = search(asking + ' википедия', num_results=0)
                                            html_text = requests.get(link_of_srch[0]).text
                                            soop = BeautifulSoup(html_text, 'html.parser')
                                            info = soop.find('p').get_text()
                                            urtts(info[:info.find('(') - 1] + info[info.find(')') + 1:])
                                            print(info[:info.find('(') - 1] + info[info.find(')') + 1:])
                                            text = ''
                                        except:
                                            urtts('не знаю, но скоро узнАю')
                                    asking = asking.replace('_', '+')
                                    text = ''
                                    command_performed = True

                                else:
                                    try:
                                        asking = text[i + 2]
                                        html = requests.get(f'https://ru.wiktionary.org/wiki/{asking}').text
                                        soup = BeautifulSoup(html, 'html.parser')
                                        find_text = soup.find('ol').get_text()
                                        urtts(str(find_text.split('◆')[0]))
                                    except IndexError:
                                        urtts('не понял, о чём вы хотели спросить')
                                    except AttributeError:
                                        urtts('не знаю, но скоро узнАю')
                                    asking = asking.replace('_', '+')
                                    command_performed = True
                        if "покажи" == text[i]:
                            if len(text[i:]) > 1:
                                try:
                                    if text[i + 1] == 'что':
                                        if text[i + 2] == "такое":
                                            httml = requests.get(
                                                f'https://www.google.com/search?q={urllib.parse.quote(text[i + 3:])}&source=lnms&tbm=isch&sa=X').text
                                            print(
                                                'link = ' + f'https://www.google.com/search?q={urllib.parse.quote(text[i + 3:])}&source=lnms&tbm=isch&sa=X')
                                            sp = BeautifulSoup(httml, 'html.parser')
                                            plz_find = sp.find_all('img', {'scr': ''})
                                            img_url = str(find_text[1]).split('"')[5]
                                            print(img_url)
                                            img_data = requests.get(img_url).content
                                            with open('img_to_show.jpg', 'wb') as handler:
                                                handler.write(img_data)
                                            im = Image.open(
                                                "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show.jpg")
                                            im.show()
                                            img_url = str(find_text[2]).split('"')[5]
                                            print(img_url)
                                            # urllib.request.urlretrieve(img_url, "img_to_show2.jpg")
                                            # im = Image.open(
                                            #     "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show2.jpg")
                                            # im.show()
                                            # img_url = str(find_text[3]).split('"')[5]
                                            # print(img_url)
                                            # urllib.request.urlretrieve(img_url, "img_to_show3.jpg")
                                            # im = Image.open(
                                            #     "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show3.jpg")
                                            # im.show()
                                            urtts('вот')
                                        else:
                                            httml = requests.get(
                                                f'https://www.google.com/search?q={urllib.parse.quote(text[i + 2:])}&source=lnms&tbm=isch&sa=X').text
                                            print(
                                                'link = ' + f'https://www.google.com/search?q={urllib.parse.quote(text[i + 2:])}&source=lnms&tbm=isch&sa=X')
                                            sp = BeautifulSoup(httml, 'html.parser')
                                            plz_find = sp.find_all('img', {'scr': ''})
                                            print(img_url)
                                            img_url = str(find_text[1]).split('"')[5]
                                            urllib.request.urlretrieve(img_url, "img_to_show.jpg")
                                            im = Image.open(
                                                "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show.jpg")
                                            im.show()
                                            print(img_url)
                                            # img_url = str(find_text[2]).split('"')[5]
                                            # urllib.request.urlretrieve(img_url, "img_to_show2.jpg")
                                            # im = Image.open(
                                            #     "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show2.jpg")
                                            # im.show()
                                            # img_url = str(find_text[3]).split('"')[5]
                                            # urllib.request.urlretrieve(img_url, "img_to_show3.jpg")
                                            # im = Image.open(
                                            #     "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show3.jpg")
                                            # im.show()
                                            # print(img_url)
                                            urtts('вот')
                                    else:
                                        httml = requests.get(
                                            f'https://www.google.com/search?q={urllib.parse.quote(text[i + 1:])}&source=lnms&tbm=isch&sa=X').text
                                        print(
                                            'link = ' + f'https://www.google.com/search?q={urllib.parse.quote(text[i + 1:])}&source=lnms&tbm=isch&sa=X')
                                        sp = BeautifulSoup(httml, 'html.parser')
                                        plz_find = sp.find_all('img', {'scr': ''})
                                        img_url = str(find_text[1]).split('"')[5]
                                        urllib.request.urlretrieve(img_url, "img_to_show.jpg")
                                        im = Image.open(
                                            "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show.jpg")
                                        im.show()
                                        print(img_url)
                                        # img_url = str(find_text[2]).split('"')[5]
                                        # urllib.request.urlretrieve(img_url, "img_to_show2.jpg")
                                        # im = Image.open(
                                        #     "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show2.jpg")
                                        # im.show()
                                        # print(img_url)
                                        # img_url = str(find_text[3]).split('"')[5]
                                        # urllib.request.urlretrieve(img_url, "img_to_show3.jpg")
                                        # im = Image.open(
                                        #     "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show3.jpg")
                                        # im.show()
                                        # print(img_url)
                                        urtts('вот')
                                except:
                                    pass
                            else:
                                try:
                                    httml = requests.get(
                                        f'https://www.google.com/search?q={urllib.parse.quote(asking)}&source=lnms&tbm=isch&sa=X').text
                                    sp = BeautifulSoup(httml, 'html.parser')
                                    plz_find = sp.find_all('img', {'scr': ''})
                                    img_url = str(find_text[1]).split('"')[5]
                                    urllib.request.urlretrieve(img_url, "img_to_show.jpg")
                                    im = Image.open(
                                        "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show.jpg")
                                    im.show()
                                    print(img_url)
                                    # img_url = str(find_text[2]).split('"')[5]
                                    # urllib.request.urlretrieve(img_url, "img_to_show2.jpg")
                                    # im = Image.open(
                                    #     "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show2.jpg")
                                    # im.show()
                                    # img_url = str(find_text[3]).split('"')[5]
                                    # urllib.request.urlretrieve(img_url, "img_to_show3.jpg")
                                    # im = Image.open(
                                    #     "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show3.jpg")
                                    # im.show()
                                    urtts('вот')
                                except:
                                    urtts("а что показать?")
                                    audio_to_show = r.record(source, duration=3)
                                    text_to_show = r.recognize_google(audio_to_show, language='ru-ru')
                                    text_to_show = str(text_to_show).replace("['", '').replace("', '", '+').replace(
                                        "']", '')
                                    print(text_to_show)
                                    text_to_show = urllib.parse.quote(text_to_show)
                                    html = requests.get(
                                        f'https://www.google.com/search?q={text_to_show}&source=lnms&tbm=isch&sa=X').text
                                    soup = BeautifulSoup(html, 'html.parser')
                                    find_text = soup.find_all('img', {'scr': ''})
                                    img_url = str(find_text[1]).split('"')[5]
                                    img_data = requests.get(img_url).content
                                    with open('img_to_show.jpg', 'wb') as handler:
                                        handler.write(img_data)
                                    im = Image.open(
                                        "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show.jpg")
                                    im.show()
                                    urtts('вот')
                            text = ''
                            command_performed = True
                        if "выключись" in text:
                            break
                        if text[i] == 'скажи':
                            if text[i + 1] != 'что':
                                urtts(' '.join(text[i + 1:]).replace("ты", 'я'))
                                command_performed = True
                            else:
                                urtts(' '.join(text[i + 2:]).replace("ты", 'я'))
                                command_performed = True
                        if text[i] == 'включи' or text[i] == "включили" or text[i] == "включить":
                            cter = i + 1
                            name_of_something = str(text[i + 1:]).replace("['", '').replace("', '", ' ').replace(
                                "']", "")
                            # if not len(text[i:] < 0):
                            print("после i: " + name_of_something.replace('c400', 'c418'))
                            url = str(json.loads(
                                YoutubeSearch(name_of_something + ' official', max_results=1).to_json()))
                            urtts("включаю " + str(name_of_something))
                            print('URL = ' + url)
                            s = str(url)
                            result = re.search("'url_suffix': '/watch(.*)'}]}", s)
                            index = result.group(1).replace("?v=", '')
                            print(index)
                            webbrowser.open("https://www.youtube.com/watch?v=" + str(index))
                            audio = r.record(source, duration=5)
                            try:
                                text = r.recognize_google(audio, language='ru-ru')
                                text = str(text).lower()
                                if 'не то' in text:
                                    keyboard.press('cmd')
                                    keyboard.press('w')
                                    keyboard.release('cmd')
                                    keyboard.release('w')
                                    url = str(json.loads(
                                        YoutubeSearch(name_of_something + ' official', max_results=2).to_json()))
                                    print('URL = ' + url)
                                    s = str(url)
                                    s = url[len(s) // 2 + 100:]
                                    result = re.search("'url_suffix': '/watch(.*)'}]}", s)
                                    index = result.group(1).replace("?v=", '')
                                    print(index)
                                    webbrowser.open("https://www.youtube.com/watch?v=" + str(index))
                                    command_performed = True
                            except:
                                command_performed = True
                        if text[i] == 'акция' or text[i] == 'акции' or text[i] == 'акций':
                            name_of_something = str(text[i + 1:]).replace("['", '').replace("', '", ' ').replace("']",
                                                                                                                 "").replace(
                                "Тёма", '').lower()
                            url = str(search("акции " + name_of_something + " tinkoff.com", num_results=0)[0])
                            print(url)

                            cter = i + 1

                            # print("после i: " + name_of_something)
                            name = name_of_something
                            html_text = requests.get(url).text
                            soup = BeautifulSoup(html_text, 'html.parser')
                            find_text = soup.find('span', {'data-qa-type': 'uikit/money'}).get_text()
                            if "$" in find_text.split()[1]:
                                print(str(find_text.split()[0])[:-1] + " $")
                                urtts("На данный момент, акции " +
                                      name + " " +
                                      str(find_text.split()[0])[:-1] + "Долларов")

                            else:
                                print(str(find_text.split()[0])[:-1] + " Pуб.")
                                urtts("На данный момент, акции " +
                                      name + " " +
                                      str(find_text.split()[0])[:-1] + "Рублей")

                            command_performed = True
                            # if '-' in find_text.split()[1]:
                            #     urtts("Они опустились за сегодня на " + find_text.split()[1].replace('-', ''))
                            #
                            # else:
                            #     urtts("Они повысились за сегодня на " + find_text.split()[1])
                            # urtts("Это " + find_text.split()[2].replace('(', '').replace(")", '') + "процентов")
                            # command_performed = True
            for i in name_list:
                if i in text82374:
                    if not command_performed == True:
                        # print("полчуилось")
                        # print(text82374.split())
                        text82374 = ' '.join(text82374.split()[1:])
                        urltosearch = "https://www.google.com/search?q=" + urllib.parse.quote(
                            text82374.lower().replace("сколько будет", ''), safe='')
                        print(urltosearch)
                        html = requests.get(urltosearch).text
                        soup = BeautifulSoup(html, 'html.parser')
                        # print(soup)
                        # try:
                        #     answer = text82374.lower().replace("x", '*').replace("поделить на", '/').replace("сколько", '').replace('будет', '')
                        #     answer = eval(answer)
                        #     print(answer)
                        #     urtts(answer)
                        # except:
                        try:
                            find_text = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).get_text()
                            if "Не найдено:" in find_text or "..." in find_text:
                                urtts("Я не понял ваш запрос, повторите пожалуйста")
                            else:
                                print(find_text)
                                urtts(find_text)
                        except:
                            find_text = soup.find('div', {'class': 'BNeawe s3v9rd AP7Wnd'}).get_text()
                            if "Не найдено:" in find_text or "..." in find_text:
                                urtts("Я не понял ваш запрос, повторите пожалуйста")
                            else:
                                print(find_text)
                                urtts(find_text)
            command_performed = False
        except Exception as e:
            command_performed = False
            if len(str(e)) > 2:
                print(colored(e, 'red'))
