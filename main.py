import serial
import speech_recognition as sr
import json
import serial.tools.list_ports
import os

debug = False
if debug:
    print(os.system('python3 -m serial.tools.list_ports'))
    ArduinoUnoSerial = serial.Serial(input('Ur port: '), 9600)
else:
    ArduinoUnoSerial = serial.Serial('/dev/cu.usbmodem141401', 9600)
r = sr.Recognizer()


while 1:
    with sr.Microphone(0) as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='ru-ru')
            if debug:
                print(text)
            text = str(text).lower()

            if text in comms.keys():
                ArduinoUnoSerial.write(comms[text].encode('utf-8'))
            else:
                print('No such command')
        except:
            pass
while 1:
    inp = input()
