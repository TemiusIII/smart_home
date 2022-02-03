import datetime
import json
import math
import random
import threading
import webbrowser
import keyboard
import pyautogui
from PIL import Image
from googlesearch import search
from gtts import gTTS
import os
from playsound import playsound
import serial.tools.list_ports
import speech_recognition as sr
import json
import re
from youtube_search import YoutubeSearch
from pytube import YouTube
from bs4 import BeautifulSoup
import requests
import osascript
import urllib.parse
import urllib.request
import telebot

bot = telebot.TeleBot("2022609617:AAERjqknUxED8jUks-Xuy0akUuYo0RkDX6o")

name = 'Саша'
said_name = False
name_list = ['тёма', 'сема', 'тём', 'сем', 'сём', 'тем', 'тема', 'артём', 'чем', 'что мы']

jokes = ["сидит чукча, ругает жену стуча кулаком по столу. Жена спрашиает: кто в дверь стучит, пойду открою. Чукча кричит: СТОЙ, САМ ОТКРОЮ!!!",
         "Будит как-то мама Гитлера, а он отмахиваеться. Мне ко второй",
         "Каким будет суп: рыбным или мясным, если сварить русалку?",
         "Знаете что будет если все люди встанут по экватору в цепочку? Половина утонет",
         "Штирлиц всю ночь топил камин, на утро камин утонул",
         "Бабушка переходила дорогу не на тот свет, а попала на тот"]


def urtts(text, lang='ru'):
    if 'welcome.mp3' in os.listdir():
        os.remove('/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/welcome.mp3')
    myobj = gTTS(text=text, lang=lang)
    myobj.save("welcome.mp3")
    playsound('welcome.mp3')


debug = True
config = json.load(open('../../MineIsTop/config_undecoded.json', 'r', encoding='utf-8'))

if debug:
    # x = input('Do you want to change your port?(y/n)')
    x = 1
    if x == 'y':
        print(*serial.tools.list_ports.comports())
        new_port = input('\nChoose your port\n')
        config['port'] = new_port
        write_file = open('../../MineIsTop/config.json', 'w')
        json.dump(config, write_file)
        write_file.close()

# ArduinoUnoSerial = serial.Serial(config['port'], 9600)
r = sr.Recognizer()

commands = config['commands']


class HGS(threading.Thread):
    def run(self, *args, **kwargs):
        while True:
            with sr.Microphone() as source:
                audio = r.record(source, duration=1)
                try:
                    text = r.recognize_google(audio, language='ru-ru')
                    if 'тихо' in str(text):
                        osascript.osascript("set volume output volume 0")
                    else:
                        pass
                except:
                    pass


# if debug:
#     x = input('Do you want to manually write commands to you Com port?(y/n)\n')
#     if x == 'y':
#         print('type \'exit1337\' to exit')
#         while x != 'exit1337':  # variable is same because я экономлю память на переменных
#             x = input()
#             ArduinoUnoSerial.write((x + '\r').encode('utf-8'))
#             print('Command was wrote')
if debug:
    print('Main part begins')
while 1:
    with sr.Microphone() as source:
        audio = r.record(source, duration=5)
        try:
            text = r.recognize_google(audio, language='ru-ru')
            if debug:
                print(text)
            text = str(text).lower()
            if "повтори" in text:
                playsound("welcome.mp3")
            # print(config["name"])
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
                    if "крутой" in text or "круто" in text:
                        urtts("но не круче тебя, " + str(name))
                        text = ''
                    if "смешно" in text or "смешной" in text:
                        urtts("Но не смешнее твоих шуток")
                        text = ''
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
                    if "спасибо" in text:
                        a = random.randint(1, 3)
                        if a == 1:
                            urtts("всегда пожалуйста")
                        if a == 2:
                            urtts("нèзачто")
                        if a == 3:
                            urtts("обращайтесь")
                        text = ''
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
                    if "тупой" in text or "пепега" in text or "дебил" in text:
                        urtts("но не такой тупой как ты!, " + name)
                        text = ''
                    if "спокойной ночи" in text:
                        urtts("Сладких снов!")
                        text = ''
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
                    text = str(text).split()
                    cter = 0
                    if 'погода' in text or 'погоду' in text:
                        # print(1)
                        html = requests.get('https://weather.com/ru-RU/weather/today/').text
                        soup = BeautifulSoup(html, 'html.parser')
                        weather = soup.find('span', {'data-testid': 'TemperatureValue'}).get_text() + 'C'
                        urtts(weather)
                        osadki = soup.find('p', {'class': 'InsightNotification--text--UxsQt'}).get_text()
                        # urtts(find_text + '. и ещё сегодня ' + soup.find('div', {'class': 'BNeawe tAd8D AP7Wnd'}).get_text().split()[2])
                        urtts(osadki)
                        cloudz = soup.find('div', {'data-testid': 'wxPhrase'}).get_text()
                        urtts(cloudz)
                        humidity = "Влажность " + soup.find('span', {'data-testid': 'PercentageValue'}).get_text()
                        urtts(humidity)
                        wind = "ветер — " + str(
                            int(soup.find('span', {'class': 'Wind--windWrapper--3aqXJ undefined'}).get_text().replace(
                                'Wind Direction', '').replace(' км/ч', '')) / 3.6)[:3] + ' м/с'
                        urtts(wind)
                    if "время" in text or 'времени' in text or "который час" in str(text).replace("', '", ' '):
                        time_now = str(datetime.datetime.now().time()).split(".")[0]
                        a = random.randint(1, 2)
                        if a == 1:
                            urtts("сейчас " + time_now)
                        elif a == 2:
                            urtts(time_now)
                        if int(time_now.split(':')[0]) > 21:
                            urtts("ПОРА СПАТЬ!!!")
                    for i in range(len(text)):
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
                        if 'сохранись' in text or 'сохранить' in text:
                            urtts('сохраняюсь')
                            f = open("/smart_home/main.py", "rb")
                            bot.send_document(1124242654, f)
                            urtts('успешно сохранился')
                            bot.stop_polling()

                        if text[i] == 'меня':
                            if text[i + 1] == 'зовут':
                                name = ' '.join(text[i + 2:])
                            urtts('привет ' + name + "!")
                        if text[i] == 'открой':
                            cter = i + 1
                            name_of_something = str(text[i + 1:]).replace("['", '').replace("', '", ' ').replace(
                                "']", "").replace("Тёма", '')
                            print("после i: " + name_of_something)
                            urtts("открываю " + str(name_of_something))
                            srch = ''.join(search(name_of_something, num_results=0))
                            print(srch)
                            webbrowser.open(str(srch).split("//")[0] + str(srch).split("//")[1])
                        if "установи громкость на" in str(text).replace("', '",
                                                                        ' ') or "установить громкость на" in str(
                            text).replace("', '", ' ') or "поставь громкость на" in str(text).replace("', '", ' '):
                            volume_mod = int(text[len(text) - 1]) / 100
                            volume = (volume_mod * 100) + ((1 - volume_mod) * 19)
                            osascript.osascript("set volume output volume " + str(int(text[len(text) - 1])))
                            urtts("должно быть лучше")
                            text = ''
                        if text[i] == 'заткнись':
                            urtts('сам заткнись')
                            said_name = False
                        if '*' in str(text):
                            urtts("не надо пожалуйста говорить плохие слова")
                            text = ''
                        if 'алиса' in str(text) and "сири" in str(text):
                            urtts("У них меньше чем у меня приемуществ, и я единственный мальчик")
                        if 'алиса' in str(text) and not "сири" in str(text) or "сири" in str(text) and not 'алиса' in str(text):
                            urtts("У нее меньше чем у меня приемуществ, и я единственный мальчик")
                        if 'сказ' in text[i] or 'скаж' in text[i]:
                            if 'шутк' in text[i+1]:
                                print(1)
                                a = random.randint(0, len(jokes)-1)
                                urtts(jokes[a])
                                text = ''
                       # if "путин" == text[i]:
                            #text[i+1] ==
                        if text[i] == 'что' or text[i] == 'кто':
                            if text[i + 1] == 'такое' or text[i + 1] == 'такая' or text[i + 1] == 'такой':
                                if len(text[i + 1:]) > 2:
                                    try:
                                        asking = str(text[i + 2:]).replace("['", '').replace("', '", '_').replace("']",
                                                                                                                  '')
                                        print(asking)
                                        html = requests.get(f'https://ru.wiktionary.org/wiki/{asking}').text
                                        soup = BeautifulSoup(html, 'html.parser')
                                        find_text = soup.find('ol').get_text()
                                        urtts(str(find_text.split('◆')[0]))
                                        print(str(find_text.split('◆')[0]))
                                    except:
                                        try:
                                            asking = str(text[i + 2:]).replace("['", '').replace("', '", '_').replace("']", '')
                                            link_of_srch = search(asking + ' википедия', num_results=0)
                                            html_text = requests.get(link_of_srch[0]).text
                                            soop = BeautifulSoup(html_text, 'html.parser')
                                            info = soop.find('p').get_text()
                                            urtts(info[:info.find('(') - 1] + info[info.find(')') + 1:])
                                            print(info[:info.find('(') - 1] + info[info.find(')') + 1:])
                                        except:
                                            urtts('не знаю, но скоро узнАю')
                                    asking = asking.replace('_', '+')

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
                        if "покажи" == text[i]:
                            if len(text[i:])>1:
                                try:
                                    if text[i+1] == 'что':
                                        if text[i+2] == "такое":
                                            httml = requests.get(
                                                f'https://www.google.com/search?q={urllib.parse.quote(text[i+3:])}&source=lnms&tbm=isch&sa=X').text
                                            print('link = ' + f'https://www.google.com/search?q={urllib.parse.quote(text[i+3:])}&source=lnms&tbm=isch&sa=X')
                                            sp = BeautifulSoup(httml, 'html.parser')
                                            plz_find = sp.find_all('img', {'scr': ''})
                                            img_url = str(find_text[1]).split('"')[5]
                                            urllib.request.urlretrieve(img_url, "img_to_show.jpg")
                                            im = Image.open(
                                                "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show.jpg")
                                            im.show()
                                            img_url = str(find_text[2]).split('"')[5]
                                            urllib.request.urlretrieve(img_url, "img_to_show2.jpg")
                                            im = Image.open(
                                                "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show2.jpg")
                                            im.show()
                                            img_url = str(find_text[3]).split('"')[5]
                                            urllib.request.urlretrieve(img_url, "img_to_show3.jpg")
                                            im = Image.open(
                                                "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show3.jpg")
                                            im.show()
                                            urtts('вот')
                                        else:
                                            httml = requests.get(
                                                f'https://www.google.com/search?q={urllib.parse.quote(text[i+2:])}&source=lnms&tbm=isch&sa=X').text
                                            print('link = ' + f'https://www.google.com/search?q={urllib.parse.quote(text[i+2:])}&source=lnms&tbm=isch&sa=X')
                                            sp = BeautifulSoup(httml, 'html.parser')
                                            plz_find = sp.find_all('img', {'scr': ''})
                                            img_url = str(find_text[1]).split('"')[5]
                                            urllib.request.urlretrieve(img_url, "img_to_show.jpg")
                                            im = Image.open(
                                                "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show.jpg")
                                            im.show()
                                            img_url = str(find_text[2]).split('"')[5]
                                            urllib.request.urlretrieve(img_url, "img_to_show2.jpg")
                                            im = Image.open(
                                                "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show2.jpg")
                                            im.show()
                                            img_url = str(find_text[3]).split('"')[5]
                                            urllib.request.urlretrieve(img_url, "img_to_show3.jpg")
                                            im = Image.open(
                                                "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show3.jpg")
                                            im.show()
                                            urtts('вот')
                                    else:
                                        httml = requests.get(
                                            f'https://www.google.com/search?q={urllib.parse.quote(text[i+1:])}&source=lnms&tbm=isch&sa=X').text
                                        print('link = ' + f'https://www.google.com/search?q={urllib.parse.quote(text[i+1:])}&source=lnms&tbm=isch&sa=X')
                                        print(3)
                                        sp = BeautifulSoup(httml, 'html.parser')
                                        plz_find = sp.find_all('img', {'scr': ''})
                                        img_url = str(find_text[1]).split('"')[5]
                                        urllib.request.urlretrieve(img_url, "img_to_show.jpg")
                                        im = Image.open(
                                            "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show.jpg")
                                        im.show()
                                        img_url = str(find_text[2]).split('"')[5]
                                        urllib.request.urlretrieve(img_url, "img_to_show2.jpg")
                                        im = Image.open(
                                            "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show2.jpg")
                                        im.show()
                                        img_url = str(find_text[3]).split('"')[5]
                                        urllib.request.urlretrieve(img_url, "img_to_show3.jpg")
                                        im = Image.open(
                                            "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show3.jpg")
                                        im.show()
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
                                    img_url = str(find_text[2]).split('"')[5]
                                    urllib.request.urlretrieve(img_url, "img_to_show2.jpg")
                                    im = Image.open(
                                        "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show2.jpg")
                                    im.show()
                                    img_url = str(find_text[3]).split('"')[5]
                                    urllib.request.urlretrieve(img_url, "img_to_show3.jpg")
                                    im = Image.open(
                                        "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show3.jpg")
                                    im.show()
                                    urtts('вот')
                                except:
                                    urtts("а что показать?")
                                    audio_to_show = r.record(source, duration=3)
                                    text_to_show = r.recognize_google(audio_to_show, language='ru-ru')
                                    text_to_show = str(text_to_show).replace("['", '').replace("', '", '+').replace(
                                        "']", '')
                                    text_to_show = urllib.parse.quote(text_to_show)
                                    html = requests.get(
                                        f'https://www.google.com/search?q={text_to_show}&source=lnms&tbm=isch&sa=X').text
                                    soup = BeautifulSoup(html, 'html.parser')
                                    find_text = soup.find_all('img', {'scr': ''})
                                    img_url = str(find_text[1]).split('"')[5]
                                    urllib.request.urlretrieve(img_url, "img_to_show.jpg")
                                    im = Image.open(
                                        "/Users/alexsukhotckii/PycharmProjects/Artem/smart_home/img_to_show.jpg")
                                    im.show()
                                    urtts('вот')
                            text = ''
                        if text[i] == 'скажи':
                            if text[i + 1] != 'что':
                                urtts(' '.join(text[i + 1:]).replace("ты", 'я'))
                            else:
                                urtts(' '.join(text[i + 2:]).replace("ты", 'я'))
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
                            except:
                                pass
                        # print(url
                        if text[i] == 'акции' or text[i] == 'акции':
                            cter = i + 1
                            name_of_something = str(text[i + 1:]).replace("['", '').replace("', '", ' ').replace("']",
                                                                                                                 "").replace(
                                "Тёма", '').lower()
                            print("после i: " + name_of_something)
                            name = name_of_something
                            html = requests.get(
                                f"https://www.google.com/search?q=акции+{name}&ei=QCHtYZ6JG9KHwPAPnf2-4A4&ved=0ahUKEwieqYaFycf1AhXSAxAIHZ2-D-wQ4dUDCA4&uact=5&oq=акции+{name}&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMgUIABCABDIECAAQQzIFCAAQgAQyBAgAEEMyCAgAEIAEEMkDMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoKCAAQRxCwAxDJAzoHCAAQsAMQQzoKCAAQ5AIQsAMYADoSCC4QxwEQ0QMQyAMQsAMQQxgBOgwILhDIAxCwAxBDGAE6EgguEMcBEKMCEMgDELADEEMYAUoECEEYAEoECEYYAVCCAlinBGCcB2gBcAJ4AIABVYgBmQGSAQEymAEAoAEByAESwAEB2gEGCAAQARgJ2gEGCAEQARgI&sclient=gws-wiz").text
                            soup = BeautifulSoup(html, 'html.parser')
                            find_text = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).get_text()
                            print(find_text)
                            urtts("На данный момент, акции " +
                                  name + " " +
                                  find_text.split()[0])
                            if '-' in find_text.split()[1]:
                                urtts("Они опустились за сегодня на " + find_text.split()[1].replace('-', ''))
                            else:
                                urtts("Они повысились за сегодня на " + find_text.split()[1])
                            urtts("Это " + find_text.split()[2].replace('(', '').replace(")", '') + "процентов")
                    # if text in commands.keys():
                    #     # comm = commands[text] + '\r'
                    #     # ArduinoUnoSerial.write(comm.encode('ascii'))
                    #     # ans = ''
                    #     # temppp = ''
                    #     # while temppp != b'\r':
                    #     #     temppp = ArduinoUnoSerial.read()
                    #     #     ans += temppp
                    #     # print(temppp)
                    #     pass
                    # else:
                    #     if debug:
                    #         print('No such command')
                    #     urtts('Не понял вашей команды, попробуйте ещё раз!')
                    # said_name = False

        except:
            pass