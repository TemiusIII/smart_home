import json
from gtts import gTTS
import os
from playsound import playsound
import serial.tools.list_ports
import speech_recognition as sr
def urtts(text, lang='ru'):
    myobj = gTTS(text=text, lang=lang)
    myobj.save("welcome.mp3")
    playsound('welcome.mp3')
debug = True

config = json.load(open('config_undecoded.json', 'r', encoding='windows-1251'))

if debug:
    x = input('Do you want to change your port?(y/n)')
    if x == 'y':
        print(*serial.tools.list_ports.comports())
        new_port = input('\nChoose your port\n')
        config['port'] = new_port
        write_file = open('config.json', 'w')
        json.dump(config, write_file)
        write_file.close()

ArduinoUnoSerial = serial.Serial(config['port'], 9600)
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

if debug:
    x = input('Do you want to manually write commands to you Com port?(y/n)\n')
    if x == 'y':
        print('type \'exit1337\' to exit')
        while x != 'exit1337':  # variable is same because я экономлю память на переменных
            x = input()
            ArduinoUnoSerial.write((x + '\r').encode('utf-8'))
            print('Command was wrote')
if debug:
    print('Main part begins')
while 1:
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='ru-ru')
            if debug:
                print(text)
            text = str(text).lower()
            if config['name'] in text or str(config['name']).replace('ё', 'е') in text:
                if text == config['name'] or str(config['name']).replace('ё', 'е'):
                    urtts('Не понял вашей команды, вы только сказали мое имя!')
                else:
                    if text in commands.keys():
                        comm = commands[text] + '\r'
                        ArduinoUnoSerial.write(comm.encode('ascii'))
                        ans = ''
                        temppp = ''
                        while temppp != b'\r':
                            temppp = ArduinoUnoSerial.read()
                            ans += temppp
                        print(temppp)
                    else:
                        if debug:
                            print('No such command')
                        urtts('Не понял вашей команды, попробуйте ещё раз!')

        except:
            pass