
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print(r.recognize_sphinx(audio, language="ru-RU"))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# import os
# from pocketsphinx import LiveSpeech, get_model_path
#
# model_path = get_model_path()
#
# speech = LiveSpeech(
#     #verbose=False,
#     #sampling_rate=16000,
#     #buffer_size=4096,
#     #no_search=False,
#     #full_utt=False,
#     #hmm=os.path.join(model_path, 'en-us'),
#     #lm=os.path.join(model_path, 'en-us.lm.bin'),
#     #dic=os.path.join(model_path, 'cmudict-en-us.dict')
#     #hmm=os.path.join(model_path, 'zero_ru.cd_cont_4000'),
#     #lm=os.path.join(model_path, 'ru.lm'),
#     #dic=os.path.join(model_path, 'ru.dic')
# )
#
# print("Say something!")
#
# for phrase in speech:
#     print(phrase)