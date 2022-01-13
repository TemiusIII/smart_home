import serial
import speech_recognition as sr
import json
import serial.tools.list_ports
import os
import time

debug = True

config = json.load(open('config.json', 'r', encoding='windows-1251'))

if debug:
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
    print('Main part begins')
while 1:
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='ru-ru')
            if not commands['name'] in text:
                pass
            else:
                print(text)
                text = str(text).lower()

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
                    print('No such command')
        except:
            pass

'''
a 97
b 98
c 99
d 100
e 101
f 102
g 103
h 104
i 105
j 106
k 107
l 108
m 109
n 110
o 111
p 112
q 113
r 114
s 115
t 116
u 117
v 118
w 119
x 120
y 121
z 122
'''
