import json
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
            #print(config["name"])
            if "тёма" in str(text) or "сёма" in str(text) or 'тём' in str(text) or 'тема':
                #print('Ты сказал мое имя!')
                #if text == config['name'] or str(config['name']).replace('ё', 'е'):
                #    urtts('Не понял вашей команды, вы только сказали мое имя!')
                #else:
                #if "включи" in text or "поставь" in text or "открой" in text or "включить":
                    text = str(text).split()
                    cter = 0
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

                            elif text[i] == 'включи':
                                cter = i + 1
                                name_of_something = str(text[i+1:]).replace("['", '').replace("', '", ' ').replace("']", "").replace("Тёма", '')
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

                            else:
                                if text[i] == 'поставь':
                                    cter = i + 1
                                    name_of_something = str(text[i + 1:]).replace("['", '').replace("', '", ' ').replace("']", "").replace("Тёма", '')
                                    print("после i: " + name_of_something)
                                    url = str(json.loads(YoutubeSearch(name_of_something + " official song", max_results=1).to_json()))
                                    print('URL = ' + url)
                                    yatoobe = YouTube(url)
                                    print("yatoobe = " + str(yatoobe))
                                    vid = yatoobe.streams.filter(only_audio=True).first()
                                    out_file = vid.download(
                                        output_path='/Users/alexsukhotckii/PycharmProjects/MineIsTop')
                                    base, ext = os.path.splitext(out_file)
                                    os.rename(out_file, "песня.mp3")
                                    playsound("песня.mp3")
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