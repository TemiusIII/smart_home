from playsound import playsound
from gtts import gTTS
import os

texts = 'я помню пенис большой, помню как он сильно входил мне в жопу, помню как текла кровь'

def urtts(text, lang='ru'):
    if 'tts.mp3' in os.listdir():
        os.remove('tts.mp3')
    myobj = gTTS(text=text, lang=lang)
    myobj.save("tts.mp3")
    playsound('tts.mp3')


for i in texts.split():
    urtts(i)