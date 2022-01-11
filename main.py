import serial
import speech_recognition as sr

# pip install pyaudio

ArduinoUnoSerial = serial.Serial('/dev/cu.usbmodem141401', 9600)  # wait for 2 secounds for the communication to get established
comms = {'включи': 'on\r', 'выключи': 'off\r'}

r = sr.Recognizer()
while 1:
    with sr.Microphone(0) as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='ru-ru')
            print(text)
            text = str(text).lower()
            print(text)
            # print(text)

            if text in comms.keys():
                ArduinoUnoSerial.write(comms[text].encode('utf-8'))
            else:
                print('No such a command')
        except:
            pass
while 1:
    inp = input()
