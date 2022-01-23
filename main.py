import datetime
import json
import random
import webbrowser
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

name_list = ['тёма', 'сема', 'тём', 'сем', 'сём', 'тем', 'тема', 'артём', 'чем']

def urtts(text, lang='ru'):
    myobj = gTTS(text=text, lang=lang)
    myobj.save("welcome.mp3")
    playsound('welcome.mp3')

debug = True
config = json.load(open('config_undecoded.json', 'r', encoding='utf-8'))

if debug:
    x = input('Do you want to change your port?(y/n)')
    if x == 'y':
        print(*serial.tools.list_ports.comports())
        new_port = input('\nChoose your port\n')
        config['port'] = new_port
        write_file = open('config.json', 'w')
        json.dump(config, write_file)
        write_file.close()

#ArduinoUnoSerial = serial.Serial(config['port'], 9600)
r = sr.Recognizer()


commands = config['commands']

if debug:
    x = input("Do you want to perform a recognition test?(y/n)")
    if x == 'y':
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, 1)
            if debug:
                print("Listening....")
            audio = r.listen(source)

            try:
                if debug:
                    print("Recognizing...")
                query = r.recognize_google(audio, language='ru-ru')
                if debug:
                    print(f"You said: {query}\n ")

            except sr.UnknownValueError:
                if debug:
                    print("Could not hear that, Try saying again")

            except sr.RequestError:
                if debug:
                    print("Make Sure that you have a good Internet connection")

if debug:
    print(commands)

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
            if "спасибо" in text:
                urtts("всегда пожалуйста")
            #print(config["name"])
            for i in name_list:
                for word in text.split():
                    if i == word:
                        if "тупой" in text or "глупый" in text or "дебил" in text:
                            urtts("все притэнзии к саше")
                        #print(Fore.RED + "Сказали мое имя!")
                        if "спокойной ночи" in text:
                            urtts("Сладких снов!")
                        if "пока" in text or "давай" in text:
                            time_now = str(datetime.datetime.now().time()).split(".")[0]
                            if int(time_now.split(':')[0]) >= 22:
                                urtts("СПАТЬ ИДИ!")
                                exit(0)
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
                                exit(0)
                        text = str(text).split()
                        cter = 0
                        if "время" in text or 'времени' in text:
                            time_now = str(datetime.datetime.now().time()).split(".")[0]
                            a = random.randint(1, 2)
                            if a == 1:
                                urtts("сейчас " + time_now)
                            elif a == 2:
                                urtts(time_now)
                            if int(time_now.split(':')[0]) > 21:
                                urtts("ПОРА СПАТЬ!!!")
                        for i in range(len(text)):
                            if text[i] == 'открой':
                                cter = i + 1
                                name_of_something = str(text[i + 1:]).replace("['", '').replace("', '", ' ').replace(
                                    "']", "").replace("Тёма", '')
                                print("после i: " + name_of_something)
                                urtts("открываю " + str(name_of_something))
                                srch = ''.join(search(name_of_something, num_results=0))
                                print(srch)
                                webbrowser.open(str(srch))

                            if text[i] == 'включи':
                                cter = i + 1
                                name_of_something = str(text[i + 1:]).replace("['", '').replace("', '", ' ').replace(
                                    "']", "").replace("Тёма", '')
                                print("после i: " + name_of_something)
                                url = str(json.loads(
                                    YoutubeSearch(name_of_something, max_results=1).to_json()))
                                urtts("включаю " + str(name_of_something))
                                print('URL = ' + url)
                                s = str(url)
                                result = re.search("'url_suffix': '/watch(.*)'}]}", s)
                                index = result.group(1).replace("?v=", '')
                                print(index)
                                # print(url)
                                webbrowser.open("https://www.youtube.com/watch?v=" + str(index))
                            if text[i] == 'акции' or text[i] == 'акции':
                                cter = i + 1
                                name_of_something = str(text[i + 1:]).replace("['", '').replace("', '", ' ').replace("']", "").replace("Тёма", '').lower()
                                print("после i: " + name_of_something)
                                name = name_of_something
                                html = requests.get(
                                    f"https://www.google.com/search?q=акции+{name}&ei=QCHtYZ6JG9KHwPAPnf2-4A4&ved=0ahUKEwieqYaFycf1AhXSAxAIHZ2-D-wQ4dUDCA4&uact=5&oq=акции+{name}&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMgUIABCABDIECAAQQzIFCAAQgAQyBAgAEEMyCAgAEIAEEMkDMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoKCAAQRxCwAxDJAzoHCAAQsAMQQzoKCAAQ5AIQsAMYADoSCC4QxwEQ0QMQyAMQsAMQQxgBOgwILhDIAxCwAxBDGAE6EgguEMcBEKMCEMgDELADEEMYAUoECEEYAEoECEYYAVCCAlinBGCcB2gBcAJ4AIABVYgBmQGSAQEymAEAoAEByAESwAEB2gEGCAAQARgJ2gEGCAEQARgI&sclient=gws-wiz").text
                                soup = BeautifulSoup(html, 'html.parser')
                                find_text = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).get_text()
                                # print(soup)
                                print(find_text)
                                urtts("На данный момент, акции " +
                                      soup.find('div', {'class': 'BNeawe vvjwJb AP7Wnd'}).get_text().split()[2] + " " +
                                      find_text.split()[0])
                                if '-' in find_text.split()[1]:
                                    urtts("Они опустились за сегодня на " + find_text.split()[1].replace('-', ''))
                                else:
                                    urtts("Они повысились за сегодня на " + find_text.split()[1])
                                urtts("Это " + find_text.split()[2].replace('(', '').replace(")", '') + "процентов")
                            if text[i] == 'поставь':
                                cter = i + 1
                                name_of_something = str(text[i + 1:]).replace("['", '').replace("', '",
                                                                                                ' ').replace("']",
                                                                                                             "").replace(
                                    "Тёма", '')
                                print("после i: " + name_of_something)
                                url = str(json.loads(
                                    YoutubeSearch(name_of_something + " official song", max_results=1).to_json()))
                                print('URL = ' + url)
                                yatoobe = YouTube(url)
                                print("yatoobe = " + str(yatoobe))
                                vid = yatoobe.streams.filter(only_audio=True).first()
                                out_file = vid.download(
                                    output_path='/Users/alexsukhotckii/PycharmProjects/MineIsTop')
                                base, ext = os.path.splitext(out_file)
                                os.rename(out_file, "song.mp3")
                                playsound("song.mp3")
                        if text in commands.keys():
                            # comm = commands[text] + '\r'
                            # ArduinoUnoSerial.write(comm.encode('ascii'))
                            # ans = ''
                            # temppp = ''
                            # while temppp != b'\r':
                            #     temppp = ArduinoUnoSerial.read()
                            #     ans += temppp
                            # print(temppp)
                            pass
                        else:
                            if debug:
                                print('No such command')
                            urtts('Не понял вашей команды, попробуйте ещё раз!')
        except:
            pass